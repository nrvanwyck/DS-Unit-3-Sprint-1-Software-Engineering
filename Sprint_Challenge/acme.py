from random import randint

class Product:
    def __init__(self,
                 name: str,
                 price: int = 10,
                 weight: int = 20,
                 flammability: float = 0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
    
    def stealability(self):
        price_over_weight = self.price / self.weight
        if price_over_weight < 0.5:
            return "Not so stealable..."
        elif 0.5 <= price_over_weight < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        flammability_times_weight = self.flammability * self.weight
        if flammability_times_weight < 10:
            return "...fizzle."
        elif 10 <= flammability_times_weight < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):
    def __init__(self,
                 name: str,
                 price: int = 10,
                 weight: int = 10,
                 flammability: float = 0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"