lista_1 = ["h","e","l","l","o"," ","t","e","a","m"]
lista_2 = ["h","e","l","l","o"," ","w","o","r","l","d"]

lista_3 = lista_1 + lista_2       #sumamos las listas
lista_nueva = []
for i in lista_3:                  #recorremos la lista
    if i not in lista_nueva:        # aqui busca que si la letra en la pocion i no se repite y luego la agrega
        lista_nueva.append(i)

print(lista_nueva)


######### lo hice de dos formas :)

"""lista1 = ["h","e","l","l","o"," ","t","e","a","m"]
lista_nueva1 = []
for i in lista1:
    if i not in lista_nueva1:
        lista_nueva1.append(i)

print(lista_nueva1)



lista2 = ["h","e","l","l","o"," ","w","o","r","l","d"]
lista_nueva2 = []
for i in lista2:
    if i not in lista_nueva2:
        lista_nueva2.append(i)

print(lista_nueva2)

listaTotal = set(lista_nueva1) - set(lista_nueva2)


print(listaTotal)"""





