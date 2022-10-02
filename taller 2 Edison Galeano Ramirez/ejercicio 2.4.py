class generacion:
    def __int__(self,x):
        self.padre= None
        self.hijo_izquierdo = None
        self.hijo_derecho = None
        self.clave = x

        def __str__(self):
            cadena = "generacion"+str(self.clave)+"--->"
            if self.padre != None:
                cadena += "\tpadre: "+str(self.padre.clave)
            else:
                cadena += "\tpadre: Ninguno"
            if self.hijo_izquierdo != None:

             cadena += "\th_izq: "+str(self.hijo_izquierdo.clave)
            else:
                        cadena += "\th_izq: Ninguno"
                        if self.hijo_derecho != None:
                          cadena += "\th_der: "+str(self.hijo_derecho.clave)
                        else:
                            cadena += "\th_der:  Ninguno"
                            cadena += "\n"
                        return cadena

            class ArbolBin:
                def __int__(self):
                    self.raiz = None

                    def mostrarArbolBin(self, sangria=4):
                        if self.raiz == None:
                            print("El arbol de generacion esta vacio! ")
                            return
                        print("El arbols es: ")

                        def mostrarArbolBinRec(generacion, cadena):
                            print(str(generacion.clave))
                            # para el hijo izq

                            if generacion.hijo_izquierdo != None:
                                if generacion.hijo_derecho != None:
                                    print(cadena + "├" + "─" * sangria, end="")
                                else:
                                    print(cadena + "└" + "─" * sangria, end="")
                                    mostrarArbolBinRec(generacion.hijo_izquierdo, cadena + "|" * sangria)
                                    # para el hijo derecho

                                    if generacion.hijo_derecho != None:
                                        print(cadena + "└" + "─" * sangria, end="")
                                        mostrarArbolBinRec(generacion.hijo_derecho, cadena + "|" * sangria)

                                        mostrarArbolBinRec(self.raiz, "")

                                        arbol = ArbolBin();
                                        generacion_1 = generacion("papá carlos"); arbol.raiz = generacion_1
                                        generacion_2 = generacion("hmano wilder"); generacion_1.hijo_izq = generacion_2;
                                        generacion_2.padre = generacion_1
                                        generacion_3 = generacion("madre berta"); generacion_3.padre = generacion_1;
                                        generacion_1.hojo_der = generacion_3
                                        generacion_4 = generacion("juanka"); generacion_4.padre = generacion_2;
                                        generacion_2.hijo_izq = generacion_4
                                        generacion_5 = generacion("edison yoop"); generacion_5.padre = generacion_2;
                                        generacion_2.hijo_der = generacion_5
                                        generacion_6 = generacion("maxi"); generacion_6.padre = generacion_4;
                                        generacion_4.hijo_izq = generacion_6

                                        print(generacion_1)
                                        print(generacion_2)
                                        print(generacion_3)
                                        print(generacion_4)
                                        print(generacion_5)
                                        print(generacion_6)





