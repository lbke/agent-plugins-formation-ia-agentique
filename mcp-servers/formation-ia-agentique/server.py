"""MCP server for the `formation-ia-agentique` plugin.

Tool names are referenced by `plugins/formation-ia-agentique/plugin.json`
(review test cases, `tools_triggered`): keep them in sync.
"""

import os
from typing import Annotated, Literal

from fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse, Response

from parcours import Profil, Recommandation, recommander
from referentiel import (
    REFERENTIEL,
    TOUS_LES_CRITERES,
    URL_CERTIFICATIONS,
    URL_FORMATION_AGENTS,
    Competence,
    ResultatEvaluation,
    calculer_scores,
)

NOM_SERVEUR = "lbke-formation-ia-agentique"

# Every tool is a pure computation on static content: no side effect, no external call.
# https://developers.openai.com/plugins/plugin-guidelines#mcp-requirements
LECTURE_SEULE = ToolAnnotations(
    read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False
)

mcp = FastMCP(
    NOM_SERVEUR,
    version="0.1.0",
    website_url="https://www.lbke.fr/formations/",
    instructions=(
        "Outils de la formation IA agentique de LBKE. Pour évaluer l'apprenant, consulte d'abord le "
        "référentiel avec `lister-criteres-competences-creation-agent-ia`, pose-lui des questions sur "
        "ses réalisations, puis calcule le score avec `scorer-competences-creation-agent-ia`. "
        "Pour l'orienter vers une technologie et une formation, utilise `recommander-parcours-ia-agentique`."
    ),
)

CritereChamp = Literal[tuple(c.champ for c in TOUS_LES_CRITERES)]  # type: ignore[valid-type]
_DESCRIPTION_CRITERES = "\n".join(f"- {c.champ} : {c.code} {c.libelle}" for c in TOUS_LES_CRITERES)


@mcp.tool(
    name="lister-criteres-competences-creation-agent-ia",
    title="Référentiel de compétences en création d'agents IA",
    annotations=LECTURE_SEULE,
)
def lister_criteres() -> list[Competence]:
    """Renvoie le référentiel LBKE des 5 compétences nécessaires pour créer un agent IA de qualité
    professionnelle, avec leurs critères d'évaluation et le seuil de critères à valider pour chacune.
    Utilise-le pour préparer les questions à poser à l'apprenant avant de calculer son score, ou pour
    lui expliquer ce qui est attendu. Il ne calcule aucun score."""
    return REFERENTIEL


@mcp.tool(
    name="scorer-competences-creation-agent-ia",
    title="Score de compétences en création d'agents IA",
    annotations=LECTURE_SEULE,
)
def scorer_competences(
    criteres_valides: Annotated[
        list[CritereChamp],
        Field(
            description=(
                "Critères que l'apprenant a démontrés, d'après ses réponses. "
                "N'inclus un critère que si l'apprenant a fourni un élément concret ; "
                "les critères absents sont considérés comme non validés.\n" + _DESCRIPTION_CRITERES
            )
        ),
    ],
) -> ResultatEvaluation:
    """Calcule le score d'un apprenant selon le référentiel LBKE de création d'agents IA de qualité
    professionnelle : pourcentage de critères validés, pourcentage de compétences validées, résultat global
    et critères restant à travailler pour chaque compétence.
    Avant de l'appeler, pose à l'apprenant les questions nécessaires pour savoir quels critères il valide ;
    n'appelle pas cet outil si tu ne connais aucune de ses compétences.
    Utilisable pour une évaluation initiale, finale ou pour mesurer une progression.
    Si l'évaluation n'est pas validée, recommande la formation indiquée dans `formation_recommandee`."""
    return calculer_scores(set(criteres_valides))


@mcp.tool(
    name="recommander-parcours-ia-agentique",
    title="Recommander un parcours de formation IA agentique",
    annotations=LECTURE_SEULE,
)
def recommander_parcours(
    profil: Annotated[
        Profil,
        Field(
            description=(
                "Profil de l'apprenant : developpeur_python (ou développeur sans préférence de langage), "
                "developpeur_javascript (développeur web JS/TS), non_developpeur (veut utiliser un agent "
                "existant sans programmer), no_code (veut automatiser sans code)."
            )
        ),
    ],
) -> Recommandation:
    """Recommande la technologie et les formations LBKE adaptées au profil de l'apprenant pour apprendre
    l'IA agentique, ainsi que le plugin LBKE à installer pour continuer le parcours.
    Identifie le profil à partir de la conversation ou pose une question si tu ne le connais pas.
    Si aucune formation ne correspond au besoin, propose de contacter LBKE."""
    return recommander(profil)


@mcp.resource(
    "https://www.lbke.fr/files/certificat_qualiopi.pdf",
    name="certificat-qualiopi-lbke",
    title="Certificat Qualiopi LBKE",
    description="Certificat Qualiopi de LBKE en tant qu'organisme de formation.",
    mime_type="text/plain",
)
def certificat_qualiopi() -> str:
    return (
        "LBKE est un organisme de formation certifié Qualiopi. "
        "Certificat : https://www.lbke.fr/files/certificat_qualiopi.pdf\n"
        f"Certifications de compétences IA : {URL_CERTIFICATIONS}"
    )


@mcp.resource(
    "lbke://referentiel/competences-creation-agent-ia",
    name="referentiel-competences-creation-agent-ia",
    title="Référentiel de compétences en création d'agents IA",
    description="Référentiel LBKE des compétences et critères pour créer un agent IA professionnel.",
    mime_type="application/json",
)
def referentiel() -> list[Competence]:
    return REFERENTIEL


# --- HTTP routes outside the MCP protocol --------------------------------------------------------


@mcp.custom_route("/", methods=["GET"])
async def accueil(request: Request) -> Response:
    return JSONResponse(
        {"serveur": NOM_SERVEUR, "mcp": "/mcp", "formation": URL_FORMATION_AGENTS}
    )


@mcp.custom_route("/.well-known/openai-apps-challenge", methods=["GET"])
async def openai_apps_challenge(request: Request) -> Response:
    """Domain verification for OpenAI app submission.

    The value is provided by the OpenAI interface; set it as the `OPENAI_APPS_CHALLENGE`
    environment variable of the Vercel project. Served from code (not `public/`) so that the
    file is plain text at the domain root, whatever the build output layout.
    """
    valeur = os.environ.get("OPENAI_APPS_CHALLENGE")
    if not valeur:
        return PlainTextResponse("Not found", status_code=404)
    return PlainTextResponse(valeur)
