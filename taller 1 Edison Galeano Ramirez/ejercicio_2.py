

"""ingresamos los datos de los estudiantes"""

nombre = input("ingrese el nombre: ")
apellidos = input("Ingrese su apellido: ")
ocupacion = input("A que te dedicas? ")
edad = int(input("Edad: "))
ciudad = input("Ciudad: ")
telefono = int(input("Numero telefonico: "))
correo = input("Correo: ")

""" toda la informacion la ingresamos a una tupla"""
Informacion_personal_tuple = (nombre,apellidos,ocupacion,edad,ciudad,telefono,correo)

"""aqui imprime la tupla"""
print(Informacion_personal_tuple)

nueva_tupla = ()     # Tupla vacía.
nueva_tupla = nueva_tupla + Informacion_personal_tuple     # a la nueva tupla le ingresamos toda la informacion

nueva_lista = []      #lista vacia
nueva_lista = nueva_lista + list(Informacion_personal_tuple)    #hacemos el cambio de tuple a list
print(nueva_lista)





