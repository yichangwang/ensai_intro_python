class Term:

    def __init__(self, operand):
        self.operand = operand
    
    # def __str__(self):
    #     return str(self.operand)

    def __add__(self, another):
        return Term(self.calculate_value() + another.calculate_value())

    def calculate_value(self):
        return str(self.operand)


class Expression(Term):
    def __init__(self, operator, operand):
        Term.__init__(self, operand)
        self.operator=operator

    def calculate_value(self):
        return self.operator + self.operand.calculate_value()


class Binairy(Expression):
    def __init__(self, operand, operand2, operator):
        Expression.__init__(self, operator, operand)
        if isinstance(operand2, Expression):
            self.operand2 = Term('(') + operand2+ Term(')')
        else:
            self.operand2 = Term(operand2)

    def calculate_value(self):
        print('{}{}{}'.format(self.operand.calculate_value(), self.operator, self.operand2.calculate_value()))
        
#        expression.__init__(self,operator)
#        a=exp.calculate_value(exp.operator)
#        return str(operand) + a
#        
       
a = Term(5)
# print(a)
ex = Expression("+", a)
# print(ex.calculate_value())
bi = Binairy(Term(3), ex, "-")
bi.calculate_value()
tri = Binairy(bi, ex, 'x')
tri.calculate_value()