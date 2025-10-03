# Classe Livre
class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return f"{self.titre} - {self.auteur} (ISBN: {self.isbn})"


class LivreNumerique(Livre):
    def __init__(self, titre, auteur, isbn, taille_fichier):
        super().__init__(titre, auteur, isbn)
        self.taille_fichier = taille_fichier

    def __str__(self):
        return f"{super().__str__()} [Taille: {self.taille_fichier} Mo]"

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, isbn):
        self.livres = [livre for livre in self.livres if livre.isbn != isbn]

    def rechercher_par_titre(self, titre):
        return [livre for livre in self.livres if titre.lower() in livre.titre.lower()]

    def rechercher_par_auteur(self, auteur):
        return [livre for livre in self.livres if auteur.lower() in livre.auteur.lower()]

    def afficher_livres(self):
        for livre in self.livres:
            print(livre)

biblio = Bibliotheque("Médiathèque")

l1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "12345")

biblio.ajouter_livre(l1)

print("Contenu de la bibliothèque :")
biblio.afficher_livres()

print("\n Recherche par titre :")
for livre in biblio.rechercher_par_titre(""):
    print(livre)

print("\n Suppression du Petit Prince...")
biblio.supprimer_livre("12345")
biblio.afficher_livres()
