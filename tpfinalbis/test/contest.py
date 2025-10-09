import pytest
from src.models import Livre, LivreNumerique
from tpfinalbis.src.file_manager import BibliothequeAvecFichier

@pytest.fixture
def biblio_vide():
    return BibliothequeAvecFichier("TestBiblio")

@pytest.fixture
def livre_exemple():
    return Livre("1984", "George Orwell", "9780451524935")

@pytest.fixture
def livre_num_exemple():
    return LivreNumerique("Python Facile", "A. Dupont", "9780451524935", 3.2)
