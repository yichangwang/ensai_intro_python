class NormalCase:
    def one_method(self):
        print("normal")


class SpecialCase:
    def one_method(self):
        print("special")


# Fonction fabrique renvoyant une classe
def convenient_case(is_normal=True):
    return NormalCase() if is_normal else SpecialCase()


if __name__ == "__main__":
    an_instance = convenient_case(is_normal=False)
    an_instance.one_method()
