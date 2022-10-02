
lista1 = [2,4,3,6]
lista2 = [8,3,4,5]
lista3 = [7,1,3,10]
lista4 = [9,2,1,4]

matriz = ([lista1] + [lista2] + [lista3] + [lista4])
print(matriz)
"""en la lista1 nos acesoramos que el 6 si exixta, lo borramos e ingresaomos el 9"""
indice = lista1.index(6)
print(indice)
item = lista1.pop(3)
print(lista1)
print(item)
lista1.append(9)
print(lista1)

"""en la lista2 nos acesoramos que el 5 si exixta, lo borramos e ingresaomos el 15"""

indice = lista2.index(5)
print(indice)
item = lista2.pop(3)
print(lista2)
print(item)
lista2.append(15)
print(lista2)

"""en la lista3 nos acesoramos que el 10 si exixta, lo borramos e ingresaomos el 11"""
indice = lista3.index(10)
print(indice)
item = lista3.pop(3)
print(lista3)
print(item)
lista3.append(11)
print(lista3)
"""en la lista4 nos acesoramos que el 12 si exixta, lo borramos e ingresaomos el 12"""
indice = lista4.index(4)
print(indice)
item = lista4.pop(3)
print(lista4)
print(item)
lista4.append(12)
print(lista4)

matriz = ([lista1] + [lista2] + [lista3] + [lista4])
print(matriz)

