# livre.py
class Livre:
    def __init__(self, isbn, titre, auteur):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.disponibilite = True

    def emprunter(self):
        if self.disponibilite:
            self.disponibilite = False
            return f"Livre '{self.titre}' emprunté avec succès."
        else:
            return f"Livre '{self.titre}' non disponible."

    def retourner(self):
        if not self.disponibilite:
            self.disponibilite = True
            return f"Livre '{self.titre}' retourné avec succès."
        else:
            return f"Cet exemplaire de '{self.titre}' est déjà disponible."
