# bibliotheque.py
class bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_tous_les_livres(self):
        for livre in self.livres:
            print(f"ISBN: {livre.isbn}, Titre: {livre.titre}, Auteur: {livre.auteur}, Disponible: {livre.disponibilite}")

    def rechercher_livre_par_titre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                return livre
        return None

    def emprunter_livre(self, titre):
        livre = self.rechercher_livre_par_titre(titre)
        if livre:
            return livre.emprunter()
        else:
            return f"Aucun livre avec le titre '{titre}' n'a été trouvé."

    def retourner_livre(self, titre):
        livre = self.rechercher_livre_par_titre(titre)
        if livre:
            return livre.retourner()
        else:
            return f"Aucun livre avec le titre '{titre}' n'a été trouvé."
