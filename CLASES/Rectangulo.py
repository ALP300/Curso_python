class Rectangulo:
    def __init__(self, base, altura):
        self.base= base
        self.altura= altura
        
    def calcular_area(self):
        return self.base*self.altura

rectangulo1= Rectangulo(5,3)
area= rectangulo1.calcular_area()
print(f"El área del rectángulo es: {area}")