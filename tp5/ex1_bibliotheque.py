import sys

class Document():
    def __init__ (self, num, titre):
        self.num = int(num)
        self.titre = titre
    def __str__ (self):
        return "Nombre: " + str(self.num) + "\n" + "titre: " + self.titre


class Livre(Document):
    def __init__(self, num, titre, author, nb_pages):
        Document.__init__(self, num, titre)
        self.author = author
        self.nb_pages = int(nb_pages)

    def __str__(self):
        return Document.__str__(self) + "\n" + "author: " + self.author + "\n" + \
            "Nombre de pages: " + str(self.nb_pages)


class Roman(Livre):
    prixLitterairesValides = set([ "Goncourt", "Médicis", "Interallié" ])
    def __init__(self, num, titre, author, nb_pages):
        Livre.__init__(self, num, titre, author, nb_pages)
        self.prixLitteraires = []

    def add_prix(self, prix):
        if prix not in Roman.prixLitterairesValides:
            return False
        self.prixLitteraires.append(prix)
        return True

    def __str__ (self):
        return " => ROMAN:\n" + Livre.__str__(self) + "\n" + "Prix littéraires: " + \
        '(' + ','.join(self.prixLitteraires) + ')'


class Manuel(Livre):
    def __init__(self, num, titre, author, nb_pages, niveau):
        Livre.__init__(self, num, titre, author, nb_pages)
        self.niveau = niveau
    def __str__(self):
        return " => MANUEL:\n" + Livre.__str__(self) + "\n" + "Niveau: " + self.niveau


class Revue(Document):
    def __init__(self, num, titre, mois, annee):
        Document.__init__(self, num, titre)
        self.mois = int(mois)
        self.annee = int(annee)
    def __str__(self):
        return " => REVUE:\n" + Document.__str__(self) + "\n" + "Mois/Année: " + \
            str(self.mois) + "/" + str(self.annee)


class Dictionnaire(Document):
    def __init__(self, num, titre, langue):
        Document.__init__(self, num, titre)
        self.langue = langue
    def __str__(self):
        return " => DICTIONNAIRE:\n" + Document.__str__(self) + "\n" + "Langue: " + \
            self.langue


class Bibliotheque():
    def __init__(self, capacite):
        self.capacite = capacite
        self.liste = []

    def afficher_documents(self):
        for doc in self.liste:
            print(doc)
    
    def document(self, i):
        print(self.liste[i-1])
    
    def ajouter(self, doc):
        if (len(self.liste) < self.capacite):
            self.liste.append(doc)
            return True
        else:
            import sys
            print("La capacité de la bibliothèque est dépassée", file=sys.stderr)
            return False
    
    def supprimer(self, doc):
        try:
            self.liste.remove(doc)
            return True
        except:
            return False
    
    def afficher_auteurs(self):
        for doc in self.liste:
            if isinstance(doc, Livre):
                print(doc.author)


class Livrotheque(Bibliotheque):
    def __init__(self, capacite):
        Bibliotheque.__init__(self, capacite)

    def ajouter(self, livre):
        if isinstance(livre, Livre):
            return Bibliotheque.ajouter(self, livre)
        else:
            print("Le document a ajouter à la livrothèque n'est pas un livre",
                file=sys.stderr)
            return False
        def afficherauthors(self):
            for doc in self.liste:
                print(doc.author)


if __name__ == '__main__':
    print(help(Roman))  # Method resolution order
    print(Roman.prixLitterairesValides)
    rom = Roman(1001, "Roman numéro 1", "Hugo", 150)
    man = Manuel (2001, "Manuel numéro 1", "Proust", 200, "1ère")
    rev = Revue (3001, "Revue numéro 1", 10, 2009)
    dic = Dictionnaire (4001, "Dictionnaire numéro 1", "Anglais")
    print(rom)
    print(rom.add_prix("Truc") == False)
    print(rom.add_prix("Médicis") == True)
    print(rom)
    print(man)
    print(rev)
    print(dic)

    bibli = Bibliotheque(3)
    print("\n*** AJOUT DES DOCUMENTS A LA BIBLIOTHEQUE ***")
    bibli.ajouter(rom)
    bibli.ajouter(man)
    bibli.ajouter(rev)
    bibli.ajouter(dic)

    # Dépasse la capacité de la bibliothèque
    bibli.afficher_documents()
    print("\n*** SUPPRESSION DE LA REVUE DE LA BIBLIOTHEQUE ***")
    bibli.supprimer(rev)
    bibli.afficher_documents()
    print("\n*** AFFICHAGE DES AUTEURS DE LA BIBLIOTHEQUE ***")
    bibli.afficher_auteurs()
    livro = Livrotheque(3)
    print("\n*** AJOUT DE 2 LIVRES (ROMAN + MANUEL) A LA LIVROTHEQUE ***")
    livro.ajouter(rom)
    livro.ajouter(man)
    livro.ajouter(rev)
    
    # N'est pas un livre
    livro.afficher_documents()
    print("\n*** SUPPRESSION DU ROMAN DE LA LIVROTHEQUE ***")
    livro.supprimer(rom)
    livro.afficher_documents()
    print("\n*** AFFICHAGE DES AUTEURS DE LA LIVROTHEQUE ***")
    livro.afficher_auteurs()

    import pylint
    # need to run with: $python ex1_bibliotheque.py "biblioteque"
    pylint.run_pyreverse()
