class Coche:
    def __init__(self, marca, color, modelo, numero_puertas, tipo_transmision,
                 cilindros, traccion, aire_acondicionado, radio, cajuela):
        
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.numero_puertas = numero_puertas
        self.tipo_transmision = tipo_transmision
        self.cilindros = cilindros
        self.traccion = traccion
        self.aire_acondicionado = aire_acondicionado
        self.radio = radio
        self.cajuela = cajuela

    def mostrarDatos(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Módelo: {self.modelo}")
        print(f"Número de puertas: {self.numero_puertas}")
        print(f"Tipo de transmisión: {self.tipo_transmision}")
        print(f"Número de cilindros: {self.cilindros}")
        print(f"Tipo de tracción: {self.traccion}")
        print(f"Aire Acondicionado: {self.aire_acondicionado}")
        print(f"Radio: {self.radio}")
        print(f"Cajuela: {self.cajuela}")

    def encender(self):
        print("El transporte está encedido")

    def apagar(self):
        print("El trasnporte está apagado")

    def acelerar(self, velocidad):
        print("Acelerando a: ", velocidad)

    def frenar(self):
        print("Frenando")

    def abrirCajuela(self):
        print("Cajuela abierta")

miCoche = Coche("Honda", "Azul", "Civic", 4, "Automática", 4,
                "Delantera", True, True, True)

miCoche.mostrarDatos()
miCoche.encender()
miCoche.acelerar("150km/h")
miCoche.frenar()
miCoche.abrirCajuela()
miCoche.apagar()
