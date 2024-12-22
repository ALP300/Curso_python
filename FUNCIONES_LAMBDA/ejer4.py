def operar(x,y,funcion):
    return funcion(x,y)

resultado= operar(2,3, lambda x,y: x+y)
print("El resultado de la suma es: ", resultado)
resultado2= operar(2,3, lambda x,y: x*y)
print("El resultado de la multiplicación es: ", resultado2)