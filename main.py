import tkinter as tk
from tkinter import ttk, messagebox

class Livre:
    def __init__(self, isbn, titre, auteur):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.disponibilite = True
        self.associations = []

    def emprunter(self, personne):
        if self.disponibilite:
            self.disponibilite = False
            self.associations.append(personne)
            return f"Livre '{self.titre}' emprunté avec succès par {personne.nom}."
        else:
            return f"Livre '{self.titre}' non disponible."

    def retourner(self):
        if not self.disponibilite:
            personne = self.associations.pop()
            self.disponibilite = True
            return f"Livre '{self.titre}' retourné avec succès par {personne.nom}."
        else:
            return f"Cet exemplaire de '{self.titre}' est déjà disponible."

class Bibliotheque:
    def __init__(self):
        self.livres = [
            Livre("123456789", "Python for Beginners", "John Doe"),
            Livre("987654321", "Java Programming", "Jane Smith"),
            Livre("111223344", "Web Development 101", "Bob Johnson"),
        ]

    def afficher_tous_les_livres(self):
        return [f"ISBN: {livre.isbn}, Titre: {livre.titre}, Auteur: {livre.auteur}, Disponible: {livre.disponibilite}, "
                f"Associé à: {[personne.nom for personne in livre.associations]}" for livre in self.livres]

    def rechercher_livre_par_titre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                return livre
        return None

    def emprunter_livre(self, titre, personne):
        livre = self.rechercher_livre_par_titre(titre)
        if livre:
            return livre.emprunter(personne)
        else:
            return f"Aucun livre avec le titre '{titre}' n'a été trouvé."

    def retourner_livre(self, titre):
        livre = self.rechercher_livre_par_titre(titre)
        if livre:
            return livre.retourner()
        else:
            return f"Aucun livre avec le titre '{titre}' n'a été trouvé."

class Membre:
    def __init__(self, nom):
        self.nom = nom

class BibliothequeApp:
    def __init__(self, master):
        self.master = master
        master.title("Gestion de Bibliothèque")

        self.biblio = Bibliotheque()

        self.label = tk.Label(master, text="Bienvenue dans la Bibliothèque", font=("Helvetica", 16), pady=10)
        self.label.pack()

        self.frame = ttk.Frame(master)
        self.frame.pack()

        self.style = ttk.Style()
        self.style.configure("TButton", padding=10, font=("Helvetica", 12))
        self.style.configure("TLabel", padding=10, font=("Helvetica", 12))
        self.style.configure("TEntry", padding=10, font=("Helvetica", 12))

        self.listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, font=("Helvetica", 12))
        self.listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.refresh_button = ttk.Button(self.frame, text="Actualiser", command=self.afficher_livres)
        self.refresh_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.rechercher_entry = ttk.Entry(self.frame, font=("Helvetica", 12))
        self.rechercher_entry.pack(side=tk.LEFT, padx=10, pady=10)
        self.rechercher_button = ttk.Button(self.frame, text="Rechercher Livre", command=self.rechercher_livre)
        self.rechercher_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.emprunter_button = ttk.Button(self.frame, text="Emprunter Livre", command=self.emprunter_livre)
        self.emprunter_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.retourner_button = ttk.Button(self.frame, text="Retourner Livre", command=self.retourner_livre)
        self.retourner_button.pack(side=tk.LEFT, padx=10, pady=10)

    def afficher_livres(self):
        livres = self.biblio.afficher_tous_les_livres()
        self.listbox.delete(0, tk.END)
        for livre in livres:
            self.listbox.insert(tk.END, livre)

    def rechercher_livre(self):
        titre = self.rechercher_entry.get()
        if titre:
            livre = self.biblio.rechercher_livre_par_titre(titre)
            if livre:
                self.listbox.delete(0, tk.END)
                self.listbox.insert(tk.END, f"ISBN: {livre.isbn}, Titre: {livre.titre}, Auteur: {livre.auteur}, "
                                            f"Disponible: {livre.disponibilite}, Associé à: "
                                            f"{[personne.nom for personne in livre.associations]}")
            else:
                messagebox.showinfo("Résultat", f"Aucun livre avec le titre '{titre}' n'a été trouvé.")
        else:
            messagebox.showinfo("Résultat", "Veuillez entrer un titre de livre.")

    def emprunter_livre(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_title = self.listbox.get(selected_index)
            titre = selected_title.split(" par ")[1].split(" -")[0]
            personne = Membre("John Doe")  # Remplacez cela par la logique de sélection du membre
            resultat = self.biblio.emprunter_livre(titre, personne)
            messagebox.showinfo("Résultat", resultat)
            self.afficher_livres()

    def retourner_livre(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_title = self.listbox.get(selected_index)
            titre = selected_title.split(" par ")[1].split(" -")[0]
            resultat = self.biblio.retourner_livre(titre)
            messagebox.showinfo("Résultat", resultat)
            self.afficher_livres()

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliothequeApp(root)
    root.mainloop()
