import json
import csv
from tpfinalbis.file_manager import BibliothequeAvecFichier

class ErreurBibliotheque(BibliothequeAvecFichier):
    def __init__(self, message: str, code_erreur=0):
        super().__init__(message)
        self.code_erreur = code_erreur
raise ErreurBibliotheque("ISBN déjà existant", code_erreur=1001)
