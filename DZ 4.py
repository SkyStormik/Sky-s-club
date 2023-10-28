class Country:
    country = "Germany"
class Brand:
    brand = "Audi"
class Model:
    model = "rs7"
class V:
    V = "3993 см3"
class Power:
    power = "560 h.p."
class Weight:
    weight = "2005 kg"
class Speed:
    speed = "250 km/hour"
class LongWidthHeight:
    long = "5012 mm"
    width = "2139 mm"
    height = "1419 mm"
class Drive:
    drive = "All-wheel drive"
class Classauto:
    classauto = "sportcar"
class Auto(Country, Brand, Model, V, Power, Weight, Speed, LongWidthHeight, Drive, Classauto):
    Auto = "Audi rs7"
print(Auto)