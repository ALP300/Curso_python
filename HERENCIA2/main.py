from empleado import Empleado
from gerente import Gerente
from departamento import Departamento

nombre = input("Ingresa tu nombre: ")
salario = int(input("Ingresa tu salario"))
empleado1= Empleado(nombre,salario)
empleado2= Empleado("Pepe",1200)

gerente= Gerente("Luis",1200,2000)
gerente2= Gerente("Juan",1200,2000)

departamento= Departamento("Ventas")

departamento.Agregar_empleado(empleado1)
departamento.Agregar_empleado(gerente)

departamento.mostrar_empleados()