# file_manager.py
import json
import csv
from src.models import Bibliotheque, Livre, LivreNumerique
from src.exeptions import ErreurBibliotheque

class BibliothequeAvecFichier(Bibliotheque):
    def sauvegarder_json(self, fichier):
        try:
            data = [livre.to_dict() for livre in self.livres]
            with open(fichier, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Catalogue sauvegardé dans '{fichier}'.")
        except Exception as e:
            raise ErreurBibliotheque(f"Erreur lors de la sauvegarde JSON : {e}")

    def charger_json(self, fichier):
        try:
            with open(fichier, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.livres = []
            for d in data:
                if d["type"] == "Livre":
                    livre = Livre("", "", "").from_dict(d)
                elif d["type"] == "LivreNumerique":
                    livre = LivreNumerique("", "", "", 0).from_dict(d)
                else:
                    raise ErreurBibliotheque(f"Type de livre inconnu : {d['type']}")
                self.livres.append(livre)

            print(f"Catalogue chargé depuis '{fichier}'.")
        except FileNotFoundError:
            raise ErreurBibliotheque(f"Fichier '{fichier}' introuvable.")
        except json.JSONDecodeError:
            raise ErreurBibliotheque(f"Erreur : format JSON invalide dans '{fichier}'.")
        except Exception as e:
            raise ErreurBibliotheque(f"Erreur lors du chargement JSON : {e}")

    def exporter_csv(self, fichier):
        try:
            with open(fichier, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Titre", "Auteur", "ISBN", "Type", "Taille_fichier"])
                for livre in self.livres:
                    if isinstance(livre, LivreNumerique):
                        writer.writerow([livre.titre, livre.auteur, livre.isbn, "LivreNumerique", livre.taille_fichier])
                    else:
                        writer.writerow([livre.titre, livre.auteur, livre.isbn, "Livre", ""])
            print(f"Catalogue exporté en CSV dans '{fichier}'.")
        except Exception as e:
            raise ErreurBibliotheque(f"Erreur lors de l'export CSV : {e}")
