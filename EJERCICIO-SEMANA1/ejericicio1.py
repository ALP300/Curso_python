'''

Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).

'''
num1= float(input("Ingresa el primer número: "))
num2= float(input("Ingresa el segundo número: "))
suma= num1+num2
resta= num1-num2
mult= num1*num2
division= num1/num2 if num2 !=0 else "No se puede dividir entre cero"
divisionEntera= num1//num2 if num2 !=0 else "No se puede dividir entre cero"
modulo= num1%num2 if num2 !=0 else "No se puede calcular el residuo"
print(f"Suma: {suma}")
print(f"Resta {resta}")
print(f"Multiplicación: {mult}")
print(f"División: {division}")
print(f"División Entera: {divisionEntera}")
print(f"Módulo: {modulo}")