""" formula de la distancia  d = v*t +- (1/2) * 9.8 * t**2  formula del tiempo
d = distancia  v = velocidad  t = tiempo h = altura
velocidad final(vf) = velocidad inicial(vo) + 9.8 + t --> el resultado es en metros cuadrados """
import math      # se importa un math para poder hacer operaciones con raiz cuadrada

altura = int(input("digite la altura en metros: "))             #altura
g = 9.8                                                         #gravedad....segun la matematica convencional
t = float(math.sqrt((2*altura)/9.8))                              #aplicamos la formula para hallar primero el tiempo
d = 1/2 * 9.8 * float(t)                                        # ya con el tiempo podemos saber cual es la distacia
n = round(t)

print(f"el tiempo recorrido es: {t} segundos")
print(f"la distancia recorrida es {d} metros")

for i in range(n):
        if
    print(n, end=" ")