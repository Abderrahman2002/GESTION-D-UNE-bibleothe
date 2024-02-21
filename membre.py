# membre.py
class Membre:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []

    def emprunter_livre(self, livre):
        self.emprunts.append(livre)
        return f"{self.nom} a emprunté le livre '{livre.titre}'."

    def retourner_livre(self, livre):
        if livre in self.emprunts:
            self.emprunts.remove(livre)
            return f"{self.nom} a retourné le livre '{livre.titre}'."
        else:
            return f"{self.nom} n'a pas emprunté le livre '{livre.titre}'."
