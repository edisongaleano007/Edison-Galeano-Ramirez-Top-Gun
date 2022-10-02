
distancia = int(input("Digite la distancia: "))
tiempo = int(input("digite el tiempo: "))
velocidad = (distancia / tiempo)
print(velocidad)
if velocidad <= 20:
    print(f"la velocidad promedio es: {velocidad} km/h velocidad muy baja!")
else:
    if velocidad >= 21 and velocidad <= 60:
        print(f"la velocidad promedio es: {velocidad} km/h velocidad normal!")
    else:
        if (velocidad >= 61 and velocidad <= 80):
            print(f"la velocidad promedio es: {velocidad} km/h velocidad muy alta!")
        else:
            if (velocidad >= 81 and velocidad <= 120):
                print(f"la velocidad promedio es: {velocidad} km/h MULTA tipo_1!...........se le realizara alcoholemia")
                alcoholemia = int(input("Cuantos grados de alcoholemia tiene el conductor? "))
                if alcoholemia < 20:
                    print("Comparendo normal")
                else:
                    if alcoholemia > 21 and alcoholemia <= 39:
                        print("suspencion de la licencia 6 meses")
                    else:
                        if alcoholemia >=40 and alcoholemia <= 99:
                            print("Suspencion de la licencia entre 1 y 3 años")
                        else:
                            if alcoholemia >= 100 and alcoholemia <= 149:
                                print("Suspencion de licencia entre 3 y 5 años y hara el curso de 40 horas")
            else:
                if (velocidad >= 121):
                    print(
                        f"la velocidad promedio es: {velocidad} km/h MULTA TIPO_2 Inmovilizacion del vehiculo...........se le realizara alcoholemia")
                    alcoholemia = int(input("Cuantos grados de alcoholemia tiene el conductor? "))
                    if alcoholemia < 20:
                        print("Comparendo normal")
                    else:
                        if alcoholemia > 21 and alcoholemia <= 39:
                            print("suspencion de la licencia 6 meses")
                        else:
                            if alcoholemia >= 40 and alcoholemia <= 99:
                                print("Suspencion de la licencia entre 1 y 3 años")
                            else:
                                if alcoholemia >= 100 and alcoholemia <= 149:
                                    print("Suspencion de licencia entre 3 y 5 años y hara el curso de 40 horas")
                                else:
                                    if alcoholemia > 150:
                                        print("Susupencion de la licencia entre 5 y 10 años y hara el curso de 80 horas")




