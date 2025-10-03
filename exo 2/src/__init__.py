class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0):
        self.titulaire = titulaire
        if solde_initial < 0:
            raise ValueError("Le solde initial ne peut pas être négatif.")
        self.solde = solde_initial

    def deposer(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant du dépôt doit être positif.")
        self.solde += montant
        print(f"{montant:.2f} € déposés. Nouveau solde : {self.solde:.2f} €")

    def retirer(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif.")
        if montant > self.solde:
            raise ValueError("Fonds insuffisants pour effectuer ce retrait.")
        self.solde -= montant
        print(f"{montant:.2f} € retirés. Nouveau solde : {self.solde:.2f} €")

    def afficher_solde(self):
        print(f"Solde du compte de {self.titulaire} : {self.solde:.2f} €")

compte1 = CompteBancaire("Alice", 100)

compte1.afficher_solde()  
compte1.deposer(50)        
compte1.retirer(30) 