'''
Escribe un programa que solicite al usuario un número entero y calcule
si es divisible por 3 y por 5.
'''
numero_1= int(input("Ingresa un número entero: "))
if numero_1 % 3 == 0 and numero_1 % 5 == 0: 
     print(f"El numero_1 {numero_1} es divisible por 3 y 5")
else:
    print(f"El numero_1 {numero_1} no es divisible por 3 y 5")