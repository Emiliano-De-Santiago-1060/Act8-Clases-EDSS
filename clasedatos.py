class Informacion:
    
    def  mi_lista(self):
        lista_Nomperras=["Bobo", "Papiroflexico", "xdpapu"]
        for x in lista_Nomperras:
            print(x)

    def mi_conjunto(self):
        tamaños=["grandes", "medianos", "chicos"]
        for z in tamaños:
            print(z)


    def mi_tupla(self):
        razas=("pastor", "pomerania", "gran danes")
        for y in razas:
            print(y)

    def mi_diccionario(self):
        carros2 = {
    "naco: ": "cris",
    "maincra: ": "edgar",
    "dado: ": "wicho"}

        for x, y in carros2.items():
            print(x,y)

datos=Informacion()


print("Listado de nombre de perros")
datos.mi_lista()
print("")
print("Conjunto de tamaños de perros")
datos.mi_conjunto()
print("")
print("Tuplas de razas de perros")
datos.mi_tupla()
print("")
print("Diccionario de dueños de perros")
datos.mi_diccionario()