print("Clases version 2 el constructor")

class Perro:
    # Funcion del constructor
    def __init__(self,color, edad):
        self.color = color
        self.edad = edad
    # Funciones creadas por el usuario
    def morder(self):
        print("Chin me mordio")
    def chatperro(self, mensaje):
        print(f"Chat perro: {mensaje}")
    def chatperra(self, mensajep):
        print(f"Chat perra: {mensajep}")
    def datos(self):
        print(f"Color {self.color} edad {self.edad}")

# Crear objeto
chihuas=Perro("Negro", 2)
#Llamas a funciones
chihuas.datos()
chihuas.morder()
chihuas.chatperro("Hola, canina")
chihuas.chatperra("Hola, totonaco")
chihuas.chatperro("Quieres ser mi novia?")
chihuas.chatperra("na")