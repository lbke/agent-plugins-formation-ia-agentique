"""LBKE competency framework for building professional-grade AI agents.

Pure data and scoring logic, with no MCP dependency, so it can be tested
in isolation. Criteria and thresholds come from the original Skybridge server
(agent-plugins-formation-ia-agentique-mcp-server, src/server.ts).
"""

from pydantic import BaseModel, Field

URL_FORMATION_AGENTS = "https://www.lbke.fr/formations/ia/agents-ia-en-entreprise"
URL_CERTIFICATIONS = "https://www.lbke.fr/actus/certifications-competences-ia"


class Critere(BaseModel):
    code: str = Field(description="Code du critère, par exemple « 1.2 ».")
    champ: str = Field(description="Nom du champ à renseigner dans l'outil de score.")
    libelle: str


class Competence(BaseModel):
    code: str
    titre: str
    description: str
    seuil: int = Field(description="Nombre minimal de critères validés pour valider la compétence.")
    criteres: list[Critere]


REFERENTIEL: list[Competence] = [
    Competence(
        code="1",
        titre="Identifier les cas d'usage des agents IA",
        description=(
            "Identifier les cas d'usage des agents fondés sur l'intelligence artificielle pour apprécier "
            "leur adéquation avec une problématique métier et un contexte professionnel donné, en s'appuyant "
            "sur une compréhension de leurs grands principes de fonctionnement, avantages, limites et risques."
        ),
        seuil=2,
        criteres=[
            Critere(code="1.1", champ="c1_1_principes_fonctionnement",
                    libelle="Les grands principes de fonctionnement des agents IA sont identifiés."),
            Critere(code="1.2", champ="c1_2_cas_usage_pertinents",
                    libelle="Des cas d'usage pour lesquels les agents IA sont avantageux et constituent la solution la plus efficace sont identifiés."),
            Critere(code="1.3", champ="c1_3_limites_et_risques",
                    libelle="Des limitations et des risques associés à l'utilisation de l'intelligence artificielle au sein de systèmes logiciels sont identifiés."),
        ],
    ),
    Competence(
        code="2",
        titre="Concevoir un agent IA",
        description=(
            "Concevoir en autonomie des agents IA répondant à des problématiques concrètes dans un domaine "
            "professionnel, à l'aide d'une méthodologie formalisée."
        ),
        seuil=2,
        criteres=[
            Critere(code="2.1", champ="c2_1_processus_modelise",
                    libelle="Le processus ou parcours utilisateur optimisé à l'aide d'un agent IA est modélisé explicitement."),
            Critere(code="2.2", champ="c2_2_reponse_a_la_problematique",
                    libelle="L'agent IA répond à la problématique."),
            Critere(code="2.3", champ="c2_3_ameliorations_identifiees",
                    libelle="Les améliorations apportées par l'agent IA sont identifiées."),
        ],
    ),
    Competence(
        code="3",
        titre="Implémenter un agent IA frugal",
        description=(
            "Implémenter des agents IA pour optimiser un processus, à l'aide d'au moins une technologie adaptée "
            "à cet usage, en favorisant l'intelligence artificielle frugale."
        ),
        seuil=3,
        criteres=[
            Critere(code="3.1", champ="c3_1_technologie_adaptee",
                    libelle="La technologie employée est adaptée à la création d'agents IA."),
            Critere(code="3.2", champ="c3_2_fonctionnement_demontre",
                    libelle="Le bon fonctionnement de l'agent IA est démontré."),
            Critere(code="3.3", champ="c3_3_empreinte_evaluee",
                    libelle="L'empreinte environnementale de l'agent IA est évaluée quantitativement ou qualitativement."),
            Critere(code="3.4", champ="c3_4_empreinte_minimisee",
                    libelle="L'empreinte environnementale de l'agent IA est minimisée selon différentes techniques."),
        ],
    ),
    Competence(
        code="4",
        titre="Évaluer la fiabilité d'un agent IA",
        description=(
            "Évaluer les caractéristiques d'un agent IA pour garantir un haut niveau de confiance à l'aide "
            "d'une analyse multicritère."
        ),
        seuil=2,
        criteres=[
            Critere(code="4.1", champ="c4_1_analyse_multicritere",
                    libelle="Une analyse multicritère est mise en œuvre pour évaluer le système agentique produit par le candidat."),
            Critere(code="4.2", champ="c4_2_dimensions_avant_publication",
                    libelle="L'analyse multicritère de l'agent tient compte des différentes dimensions à envisager avant la publication d'un agent IA."),
            Critere(code="4.3", champ="c4_3_resultats_pris_en_compte",
                    libelle="Les résultats de l'analyse multicritère ont été pris en compte dans l'implémentation de l'agent."),
        ],
    ),
    Competence(
        code="5",
        titre="Publier un agent IA",
        description=(
            "Publier un agent IA dans un contexte professionnel afin de le rendre opérationnel et accessible, "
            "en concevant un plan de déploiement approprié."
        ),
        seuil=3,
        criteres=[
            Critere(code="5.1", champ="c5_1_utilisateurs_identifies",
                    libelle="Le profil type des utilisateurs finaux ou systèmes informatiques clients mobilisant l'agent IA est identifié."),
            Critere(code="5.2", champ="c5_2_plan_publication",
                    libelle="Un plan de publication de l'agent IA est opérationnel ou formalisé."),
            Critere(code="5.3", champ="c5_3_metriques_definies",
                    libelle="Des métriques de suivi sont définies."),
            Critere(code="5.4", champ="c5_4_suivi_continu",
                    libelle="Un processus de suivi en continu des métriques est démontré."),
        ],
    ),
]

TOUS_LES_CRITERES: list[Critere] = [c for comp in REFERENTIEL for c in comp.criteres]


class ResultatCompetence(BaseModel):
    code: str
    titre: str
    criteres_valides: int
    criteres_total: int
    seuil: int
    valide: bool
    criteres_a_travailler: list[str] = Field(
        description="Libellés des critères non validés, à utiliser pour proposer une progression."
    )


class ResultatEvaluation(BaseModel):
    pourcentage_criteres_valides: float = Field(ge=0, le=100)
    pourcentage_competences_validees: float = Field(ge=0, le=100)
    evaluation_validee: bool = Field(description="Vrai si toutes les compétences atteignent leur seuil.")
    competences: list[ResultatCompetence]
    formation_recommandee: str | None = Field(
        description="URL de la formation LBKE à recommander si l'évaluation n'est pas validée."
    )


def calculer_scores(criteres_valides: set[str]) -> ResultatEvaluation:
    """Compute scores from the set of validated criterion field names."""
    inconnus = criteres_valides - {c.champ for c in TOUS_LES_CRITERES}
    if inconnus:
        raise ValueError(f"Critères inconnus : {sorted(inconnus)}")

    resultats = []
    for comp in REFERENTIEL:
        valides = [c for c in comp.criteres if c.champ in criteres_valides]
        resultats.append(
            ResultatCompetence(
                code=comp.code,
                titre=comp.titre,
                criteres_valides=len(valides),
                criteres_total=len(comp.criteres),
                seuil=comp.seuil,
                valide=len(valides) >= comp.seuil,
                criteres_a_travailler=[
                    f"{c.code} {c.libelle}" for c in comp.criteres if c.champ not in criteres_valides
                ],
            )
        )

    nb_valides = sum(r.criteres_valides for r in resultats)
    nb_comp_validees = sum(r.valide for r in resultats)
    validee = nb_comp_validees == len(resultats)
    return ResultatEvaluation(
        pourcentage_criteres_valides=round(100 * nb_valides / len(TOUS_LES_CRITERES), 1),
        pourcentage_competences_validees=round(100 * nb_comp_validees / len(resultats), 1),
        evaluation_validee=validee,
        competences=resultats,
        formation_recommandee=None if validee else URL_FORMATION_AGENTS,
    )
