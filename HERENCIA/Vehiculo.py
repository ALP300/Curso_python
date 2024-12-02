from animales import Animal

class Vehiculo(Animal):
    def __init__(self, nombre, marca):
        super().__init__(nombre)
        self.marca= marca
        
    def hacer_sonido(self):
        print(f"El {self.marca}{self.nombre} hace un sonido de motor")
        