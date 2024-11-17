'''
Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F
'''

nota= int(input("Ingresar nota: "))
if   nota > 90 and nota <= 100:
    print("A")
elif nota > 80 and nota <= 90:
    print("B")
elif nota > 70 and nota <= 80:
    print("C")
elif nota > 60 and nota <= 70:
    print("D")
elif nota > 0 and nota <= 60:
    print("F")
else:
    print("Nota invalida")