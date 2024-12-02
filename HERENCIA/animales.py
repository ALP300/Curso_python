class Animal:
    def __init__(self, nombre):
        self.nombre= nombre
    
    def hacer_sonido(self):
        print(f"El animal {self.nombre} hace un sonido genérico")
        