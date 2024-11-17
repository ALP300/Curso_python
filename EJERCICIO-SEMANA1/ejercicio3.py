'''
Escribe un programa que lea un número entero y determine si es
positivo, negativo o cero.
'''
numero = int(input("Ingrese el primer número: "))
if numero > 0:
    print("El numero",numero,"es positivo")
elif numero < 0:
    print("El numero",numero,"es negativo")
elif numero == 0:
    print("El número es cero")
else:
    "Ingreso un número inválido"