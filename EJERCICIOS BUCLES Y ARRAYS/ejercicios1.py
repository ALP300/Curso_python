'''
1. Crear una tabla de multiplicar usando un bucle
Escribe un programa que pida un número al usuario y genere su tabla de multiplicar del 1 al 10.

'''
numero= int(input("Introduce un número: ")) #5
print(f"La tabla de multiplicar del 1 al 10 del {numero} es: ")
for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")
    