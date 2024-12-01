'''
Ejercicio 6: Método con un valor de retorno y parámetros opcionales
Escribe un método que reciba una lista de números y, si no se pasa ninguna lista, 
utilice una lista por defecto. 
El método debe devolver la suma de los números.

'''

def sumar_lista(lista=None):
    if lista is None:
        lista=[1,2,3,4,5,6,7]
    
    return sum(lista)
#Esto con una lista predeterminada
resultado= sumar_lista()
print(f"Resultado con lista predeterminada es: {resultado}")

#Esto con una lista
lista_personalizada= [87,34,3,74]
resultado_lista= sumar_lista(lista_personalizada)
print(f"Resultado con la lista personalizada: {resultado_lista}")