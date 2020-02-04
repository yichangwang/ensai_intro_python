def creer_plus(ajout):
    def plus(increment):
        """Fonction 'fermeture' : utilise des noms locaux a la fonction enveloppante.
        """
        return increment + ajout
    return plus


if __name__ == "__main__":
    print(" creation de deux fabriques distinctes ". center(50, '-'))
    p = creer_plus(23)
    q = creer_plus(42)
    print(p(100), q(100))
