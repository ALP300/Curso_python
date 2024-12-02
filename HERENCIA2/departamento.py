from empleado import Empleado
from gerente import Gerente

class Departamento:
    def __init__(self, nombre):
        self.nombre= nombre
        self.empleados= []
    
    def Agregar_empleado(self,empleado):
        self.empleados.append(empleado)
    
    def mostrar_empleados(self):
        print(f"Empleados del departamiento: {self.nombre}")
        for empleado in self.empleados:
            empleado.mostrar_info()
            