from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono= bono
    
    def salario_total(self):
        return self.salario+self.bono
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Bono: {self.bono}, Salario total: {self.salario_total()}")
    