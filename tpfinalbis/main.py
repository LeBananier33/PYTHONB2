from models import Livre, LivreNumerique
from file_manager import BibliothequeAvecFichier
from exeptions import ErreurBibliotheque

if __name__ == "__main__":
    biblio = BibliothequeAvecFichier("Médiathèque Centrale")

    try:
        biblio.ajouter_livre(Livre("1984", "George Orwell", "9780451524935"))
        biblio.ajouter_livre(LivreNumerique("Python 101", "Michael Driscoll", "9781492339249", 5))
        biblio.afficher_livres()

        biblio.sauvegarder_json("catalogue.json")

        nouvelle_biblio = BibliothequeAvecFichier("Médiathèque Importée")
        nouvelle_biblio.charger_json("catalogue.json")
        nouvelle_biblio.afficher_livres()

        biblio.exporter_csv("catalogue.csv")

    except ErreurBibliotheque as e:
        print(f"Erreur de bibliothèque : {e}")
