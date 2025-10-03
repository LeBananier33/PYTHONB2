import json
import csv
from tpfinalbis.models import Bibliotheque
from tpfinalbis.models import LivreNumerique

class BibliothequeAvecFichier(Bibliotheque):
    def sauvegarder_json(self, fichier):
            data = [livre.to_dict() for livre in self.livres]
            with open(fichier, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Catalogue sauvegardé dans '{fichier}'.")

    def exporter_csv(self, fichier):
            with open(fichier, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Titre", "Auteur", "ISBN", "Type", "Taille_fichier"])
                for livre in self.livres:
                    if isinstance(livre, LivreNumerique):
                        writer.writerow([livre.titre, livre.auteur, livre.isbn, "LivreNumerique", livre.taille_fichier])
                    else:
                        writer.writerow([livre.titre, livre.auteur, livre.isbn, "Livre", ""])
            print(f"Catalogue exporté en CSV dans '{fichier}'.")