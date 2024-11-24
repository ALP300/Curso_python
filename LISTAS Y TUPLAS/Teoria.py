'''
LISTAS
'''
lista=[10,98,33,41,53]
lista2=[1]
print(lista[0])
#lista.remove(4)
print(lista)
lista[1]=25
print(lista)
tamaño= len(lista)
print(tamaño)
lista.sort()
print(lista)
lista_combinada= lista+lista2
print(lista_combinada)
#---------------------------------------------------------------------------------------

'''
TUPLA
'''
print("-------------------TUPLAS-------------------------")
tupla=(1,2,3,4,5)
print(tupla[0])
print(tupla[-1])
print(10 in tupla)

print("TRANSFORMACIÓN")

lista3= [1,2,5,6,3,7]
tupla= tuple(lista3)
print(tupla)
segmento=tupla[2:5]
print(segmento)