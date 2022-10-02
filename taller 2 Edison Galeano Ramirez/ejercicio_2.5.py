filas = int(input("Introduce el numero de filas: "))
columnas = int(input("Introduce el numero de columnnas: "))

matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input("fila {}, columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)

        print()
        for fila in matriz:
            print("[", end="")
            for elemento in fila:
                print("{:8.2f}".format(elemento), end=" ")
                print("]")
                print()