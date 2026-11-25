import pytest
from fastmcp import Client
from starlette.testclient import TestClient

from app import app
from referentiel import TOUS_LES_CRITERES
from server import mcp

TOUS = [c.champ for c in TOUS_LES_CRITERES]


@pytest.fixture
async def client():
    async with Client(mcp) as c:
        yield c


async def test_outils_exposes_et_lecture_seule(client):
    outils = {t.name: t for t in await client.list_tools()}
    assert set(outils) == {
        "lister-criteres-competences-creation-agent-ia",
        "scorer-competences-creation-agent-ia",
        "recommander-parcours-ia-agentique",
    }
    for outil in outils.values():
        assert outil.annotations.read_only_hint is True
        assert outil.annotations.open_world_hint is False
        assert outil.output_schema is not None


async def test_score_complet(client):
    res = await client.call_tool("scorer-competences-creation-agent-ia", {"criteres_valides": TOUS})
    data = res.structured_content
    assert data["pourcentage_criteres_valides"] == 100
    assert data["evaluation_validee"] is True
    assert data["formation_recommandee"] is None


async def test_score_partiel_recommande_formation(client):
    res = await client.call_tool(
        "scorer-competences-creation-agent-ia",
        {"criteres_valides": ["c1_1_principes_fonctionnement", "c1_2_cas_usage_pertinents"]},
    )
    data = res.structured_content
    assert data["pourcentage_criteres_valides"] == round(100 * 2 / 17, 1)
    assert data["pourcentage_competences_validees"] == 20
    assert data["competences"][0]["valide"] is True
    assert len(data["competences"][0]["criteres_a_travailler"]) == 1
    assert data["formation_recommandee"].startswith("https://www.lbke.fr/")


async def test_critere_inconnu_refuse(client):
    with pytest.raises(Exception):
        await client.call_tool("scorer-competences-creation-agent-ia", {"criteres_valides": ["c9_9"]})


async def test_recommandation(client):
    res = await client.call_tool("recommander-parcours-ia-agentique", {"profil": "developpeur_python"})
    assert res.structured_content["plugin_suivant"] == "formation-langchain"


def test_http_app(monkeypatch):
    monkeypatch.setenv("OPENAI_APPS_CHALLENGE", "abc123")
    with TestClient(app) as http:
        assert http.get("/").status_code == 200
        r = http.get("/.well-known/openai-apps-challenge")
        assert r.text == "abc123"
        assert r.headers["content-type"].startswith("text/plain")
