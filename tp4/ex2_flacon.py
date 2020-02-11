class Flacon:
    """Classe Flacon permettant de gérer les volumes de sirop dans un flacon"""

    def __init__(self, etiquette, capacite):
        """Crée un flacon de capacite 'capacite' contenant un sirop intitulé 'etiquette'
        etiquette: str
        capacite: float
        """
        self.__etiquette = etiquette
        self.__capacite = capacite
        self.__volume = 0.0
        self.__concentration = 0.0

    def __str__(self):
        """Renvoie une chaîne de caractères comportant les informations du flacon (étiquette,
        volume/capacité, concentration)"""
        return self.__etiquette + ": V=" + str(self.__volume) + "/" + str(self.__capacite) + " C="
        + str(self.__concentration)

    def verser(self, vSirop, vEau):
        """Ajoute les volumes vSirop et vEau dans le flacon"""
        if vSirop + vEau + self.__volume > self.__capacite:
            return False
        vSiropAvantRemplissage = self.__concentration * self.__volume
        self.__volume = self.__volume + vSirop + vEau
        self.__concentration = (vSiropAvantRemplissage + vSirop) / self.__volume
        return True

    def transvaser(self, flacon, volume):
        "Transvase un volume depuis un 'flacon' spécifié dans notre flacon"
        if volume > flacon.__volume:
            return False
        vSiropAjouté = flacon.__concentration * volume
        if self.verser(vSiropAjouté, volume - vSiropAjouté):
            flacon.__volume -= volume
            return True
        return False


if __name__ == "__main__":
    fla1 = Flacon("Flacon 1", 100)
    fla2 = Flacon("Flacon 2", 60)
    print("\nINFOS:")
    print(fla1)
    print(fla2)
    print("\nVERSER:")
    print(1, not fla1.verser(60, 60))
    print(2, fla1.verser(30, 60))
    print("\nINFOS:")
    print(fla1)
    print(fla2)
    print("\nTRANSVASER:")
    print(3, not fla2.transvaser(fla1, 110))
    print(4, not fla2.transvaser(fla1, 80))
    print(5, fla2.transvaser(fla1, 60))
    print("\nINFOS:")
    print(fla1)
    print(fla2)
    print("\nDOCS:")
    print("Falcon =>", Flacon.__doc__)
    print("Verser =>", fla1.verser.__doc__)