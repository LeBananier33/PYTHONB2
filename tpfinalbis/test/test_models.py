import pytest
from src.models import Livre, LivreNumerique, Bibliotheque

@pytest.fixture
def livre_simple():
    """Crée un livre papier classique."""
    return Livre("1984", "George Orwell", "9780451524935")


@pytest.fixture
def livre_numerique():
    """Crée un livre numérique."""
    return LivreNumerique("Python Facile", "Luc Martin", "9780454883545", 25)


@pytest.fixture
def biblio_vide():
    """Crée une bibliothèque vide."""
    return Bibliotheque("BiblioTest")


def test_livre_to_dict(livre_simple):
    """Vérifie la conversion d'un livre en dictionnaire."""
    d = livre_simple.to_dict()
    assert d["type"] == "Livre"
    assert d["titre"] == "1984"
    assert d["auteur"] == "George Orwell"


def test_livre_from_dict():
    """Vérifie la création d'un livre à partir d'un dictionnaire."""
    data = {"titre": "1984", "auteur": "George Orwell", "isbn": "9780451524935"}
    livre = Livre("", "", "").from_dict(data)
    assert livre.titre == "1984"
    assert livre.isbn == "9780451524935"

def test_livre_numerique_to_dict(livre_numerique):
    """Vérifie la conversion d'un livre numérique en dictionnaire."""
    d = livre_numerique.to_dict()
    assert d["type"] == "LivreNumerique"
    assert d["taille_fichier"] == 25


def test_livre_numerique_from_dict():
    """Vérifie la création d'un livre numérique à partir d'un dictionnaire."""
    data = {
        "titre": "Python Facile",
        "auteur": "Luc Martin",
        "isbn": "9780454883545",
        "taille_fichier": 25
    }
    livre = LivreNumerique("", "", "", 0).from_dict(data)
    assert livre.titre == "Python Facile"
    assert livre.taille_fichier == 25

def test_ajouter_livre(biblio_vide, livre_simple):
    """Vérifie qu'on peut ajouter un livre à la bibliothèque."""
    biblio_vide.ajouter_livre(livre_simple)
    assert len(biblio_vide.livres) == 1
    assert biblio_vide.livres[0].titre == "1984"


def test_ajouter_livre_existant(biblio_vide, livre_simple, capsys):
    """Vérifie qu'on ne peut pas ajouter deux fois le même livre."""
    biblio_vide.ajouter_livre(livre_simple)
    biblio_vide.ajouter_livre(livre_simple)
    sortie = capsys.readouterr().out
    assert "existe déjà" in sortie
    assert len(biblio_vide.livres) == 1


def test_afficher_livres_vide(biblio_vide, capsys):
    """Vérifie le message quand la bibliothèque est vide."""
    biblio_vide.afficher_livres()
    sortie = capsys.readouterr().out
    assert "La bibliothèque est vide" in sortie


def test_afficher_livres(biblio_vide, livre_simple, capsys):
    """Vérifie l'affichage du catalogue avec un livre."""
    biblio_vide.ajouter_livre(livre_simple)
    biblio_vide.afficher_livres()
    sortie = capsys.readouterr().out
    assert "Catalogue de BiblioTest" in sortie
    assert "1984" in sortie

