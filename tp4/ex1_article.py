class Article:
    """An article from supermarket"""
    def __init__(self, ref, article_name, pHT, qtte):
        self.__reference = ref
        self.__name = article_name
        self.__prixHT = pHT
        self.__quantity_in_stock = qtte
        Article.__tauxTVA = 1.196

    def __eq__(self, other):
        """Compare if the two Article instances have the same reference"""
        return isinstance(other, Article) and self.reference() == other.reference()

    def __lt__(self, other):
        """if other is not an Article, rise exception TypeError"""
        if not isinstance(other, Article):
            raise TypeError("unorderable types: " + 
                            type(self).__name__ + 
                            " < " +
                            type(other).__name__)
        return self.quantity_in_stock() < other.quantity_in_stock()

    def __str__(self):
        return '(' + str(self.__reference) + ', ' + str(self.__name) + ', ' + str(self.__prixHT) + ', '
        + str(self.__quantity_in_stock) + ')'


    def name(self):
        return self.__name

    def reference(self):
        return self.__reference

    def prixHT(self):
        """Hors Taxes price"""
        return self.__prixHT

    def prixTTC(self):
        """return the Toutes Taxes price"""
        return self.prixHT() * Article.__tauxTVA

    def quantity_in_stock(self):
        return self.__quantity_in_stock

    def supply(self, qte):
        self.__quantity_in_stock += qte

    def sell(self, qte):
        """if qte > quantity in stock : return False"""
        if (qte > self.__quantity_in_stock):
            return False
        self.__quantity_in_stock -= qte
        return True


# test functions
def test_sell_fail():
    a = Article(1234, "obj", 13.5, 2)
    print(4, not a.sell(1000))
    print(5, a.quantity_in_stock() == 2)


def test_sell_ok():
    a = Article(1234, "obj", 13.5, 2)
    print(6, a.sell(2))
    print(7, a.quantity_in_stock() == 0)


def test_comparison_raise_exception():
    a = Article(1234, "obj", 13.5, 2)
    a < 'string object'  # in a.__lt__
    try:
        a < 'string object'
    except TypeError:
        res = True
        # raise Exception("a is not Article type")
    else:
        res = False
    print(8, res)


if __name__ == '__main__':
    a, b, c = Article(1234, "obj", 13.5, 2), \
              Article(1234, "obj2", 16.5, 3), \
              Article(1434, "obj3", 26.5, 13)
    print(dir())
    l = [a, b, c]
    for a in l:
        print(a)
        print(a.__dict__)
        a.supply(100)
        print(a)
        print(a.sell(300))
        print(a.sell(50))
        print(a.prixHT())
        print(a.prixTTC())
        print(dir(a))
        print(a.prixTTC.__doc__)
        print("##########################")

    # Test
    print(1, l[0] == l[1])  # call x.__eq__(y) => compare the references
    print(2, not l[0] > l[1])  # call x.__lt__(y) => compare the quantities in stock
    print(3, l[0] < l[1])  # callx.__lt__(y) => compare the quantities in stock
    test_sell_fail()
    test_sell_ok()
    test_comparison_raise_exception()
