class Country:
    def __init__(self):
        super().__init__()
        self.country = "Germany"
class Brand:
    def __init__(self):
        super().__init__()
        self.brand = "Audi"
class Model:
    def __init__(self):
        super().__init__()
        self.model = "rs7"
class V:
    def __init__(self):
        super().__init__()
        self.V = "3993 cm3"
class Power:
    def __init__(self):
        super().__init__()
        self.power = "560 h.p."
class Weight:
    def __init__(self):
        super().__init__()
        self.weight = "2005 kg"
class Speed:
    def __init__(self):
        super().__init__()
        self.speed = "250 km/hour"
class LongWidthHeight:
    def __init__(self):
        super().__init__()
        self.long = "5012 mm"
        self.width = "2139 mm"
        self.height = "1419 mm"
class Drive:
    def __init__(self):
        super().__init__()
        self.drive = "All-wheel drive"
class Classauto:
    def __init__(self):
        super().__init__()
        self.classauto = "sportcar"
class Auto(Country, Brand, Model, V, Power, Weight, Speed, LongWidthHeight, Drive, Classauto):
    def print_info(self):
        print(self.brand)
        print(self.country)
        print(self.model)
        print(self.V)
        print(self.power)
        print(self.weight)
        print(self.speed)
        print(self.long)
        print(self.width)
        print(self.height)
        print(self.drive)
        print(self.classauto)
Audi = Auto()
Audi.print_info()