import json
import csv

class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return f"{self.titre} - {self.auteur} (ISBN: {self.isbn})"

    def to_dict(self):
        return {
            "type": "Livre",
            "titre": self.titre,
            "auteur": self.auteur,
            "isbn": self.isbn
        }

    def from_dict(self, data):
        return Livre(data["titre"], data["auteur"], data["isbn"])

class LivreNumerique(Livre):
    def __init__(self, titre, auteur, isbn, taille_fichier):
        super().__init__(titre, auteur, isbn)
        self.taille_fichier = taille_fichier

    def __str__(self):
        return f"{super().__str__()} [Taille: {self.taille_fichier} Mo]"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "LivreNumerique"
        d["taille_fichier"] = self.taille_fichier
        return d

    def from_dict(self, data):
        return LivreNumerique(data["titre"], data["auteur"], data["isbn"], data["taille_fichier"])

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre):
        if any(l.isbn == livre.isbn for l in self.livres):
            print(f"Le livre avec ISBN {livre.isbn} existe déjà.")
        else:
            self.livres.append(livre)

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print(f"Catalogue de {self.nom}:")
            for livre in self.livres:
                print(" -", livre)