
import json
import pytest
from src.file_manager import BibliothequeAvecFichier
from src.models import Livre, LivreNumerique


@pytest.fixture
def biblio_remplie(tmp_path):
    fichier = tmp_path / "catalogue_test.json"
    biblio = BibliothequeAvecFichier("BiblioTest")
    biblio.ajouter_livre(Livre("1984", "George Orwell", "9780451524935"))
    biblio.ajouter_livre(LivreNumerique("Python Facile", "Luc Martin", "9780454883545", 20))
    return biblio, fichier


def test_sauvegarde_json(biblio_remplie):
    biblio, fichier = biblio_remplie
    biblio.sauvegarder_json(fichier)
    assert fichier.exists()

    with open(fichier, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["titre"] == "1984"
    assert data[1]["type"] == "LivreNumerique"


def test_charger_json(biblio_remplie):
    biblio, fichier = biblio_remplie
    biblio.sauvegarder_json(fichier)

    nouvelle_biblio = BibliothequeAvecFichier("NouvelleBiblio")
    nouvelle_biblio.charger_json(fichier)

    assert len(nouvelle_biblio.livres) == 2
    assert nouvelle_biblio.livres[0].titre == "1984"
    assert isinstance(nouvelle_biblio.livres[1], LivreNumerique)

def test_exporter_csv(biblio_remplie, tmp_path):
    biblio, _ = biblio_remplie
    fichier_csv = tmp_path / "catalogue_test.csv"

    biblio.exporter_csv(fichier_csv)

    assert fichier_csv.exists()

    contenu = fichier_csv.read_text(encoding="utf-8")
    assert "1984" in contenu
    assert "Python Facile" in contenu