"""Learning-path recommendations, mirroring the plugin's skills content.

Source of truth: plugins/formation-ia-agentique/skills/enseigner-ia-agentique/references/technologies.md
and plugins/formation-ia-agentique/skills/rechercher-formation-ia-agentique/SKILL.md. Keep both in sync when one changes.
"""

from typing import Literal

from pydantic import BaseModel, Field

Profil = Literal["developpeur_python", "developpeur_javascript", "non_developpeur", "no_code"]

RESSOURCES_LBKE = [
    "https://www.lbke.fr/formations/",
    "https://www.lbke.fr/formations/ressources",
    "https://www.lbke.fr/llms.txt",
]
CONTACT_LBKE = "https://www.lbke.fr/contact"


class Recommandation(BaseModel):
    profil: Profil
    technologie: str
    pourquoi: str
    liens: list[str] = Field(description="Programmes de formation et documentation à proposer.")
    plugin_suivant: str | None = Field(
        description="Plugin LBKE à installer pour poursuivre le parcours, s'il existe."
    )
    ressources_generales: list[str] = RESSOURCES_LBKE
    contact: str = CONTACT_LBKE


_RECOMMANDATIONS: dict[str, dict] = {
    "developpeur_python": dict(
        technologie="LangChain et LangGraph (Python)",
        pourquoi="Choix le plus courant pour programmer des agents IA, et parcours technique proposé par LBKE.",
        liens=["https://www.lbke.fr/formations/", "https://docs.langchain.com/"],
        plugin_suivant="formation-langchain",
    ),
    "developpeur_javascript": dict(
        technologie="Mastra (TypeScript)",
        pourquoi="Technologie recommandée par LBKE pour les développeurs web JavaScript.",
        liens=["https://www.lbke.fr/formations/ia/mastra-ia-agentique-javascript"],
        plugin_suivant=None,
    ),
    "non_developpeur": dict(
        technologie="Claude",
        pourquoi=(
            "Sans programmation, il est plus efficace d'approfondir l'usage d'un agent IA existant ; "
            "Claude propose un parcours e-learning et une certification."
        ),
        liens=["https://www.lbke.fr/formations/technologies/claude", "https://academy.claude.com/"],
        plugin_suivant=None,
    ),
    "no_code": dict(
        technologie="n8n",
        pourquoi="Plateforme d'automatisation no-code adaptée aux workflows agentiques sans code.",
        liens=["https://www.lbke.fr/formations/ia/n8n-automatisation"],
        plugin_suivant=None,
    ),
}


def recommander(profil: Profil) -> Recommandation:
    return Recommandation(profil=profil, **_RECOMMANDATIONS[profil])
