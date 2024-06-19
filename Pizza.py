class PizzaComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Base(PizzaComponent):
    cost = 5.00


class Decorator(PizzaComponent):
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)


class Cheese(Decorator):
    cost = 1.00

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Ham(Decorator):
    cost = 0.75

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Catupiry(Decorator):
    cost = 1.25

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Pepperoni(Decorator):
    cost = 1.50

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Olives(Decorator):
    cost = 0.75

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Mushrooms(Decorator):
    cost = 1.00

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Onions(Decorator):
    cost = 0.50

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


pizza1 = Cheese(Pepperoni(Base()))
print(pizza1.getDescription() + ": $" + str(pizza1.getTotalCost()))

pizza2 = Cheese(Pepperoni(Olives(Mushrooms(Base()))))
print(pizza2.getDescription() + ": $" + str(pizza2.getTotalCost()))
