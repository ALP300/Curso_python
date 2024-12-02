class Empleado():
    def __init__(self, nombre, salario):
        self.nombre= nombre
        self.salario= salario
    
    def mostrar_info(self):
        print(f"El empleado {self.nombre} y su salario es: {self.salario}")
        