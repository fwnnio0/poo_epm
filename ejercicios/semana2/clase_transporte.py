class Transporte:
    def __init__(self, marca, color, modelo, velocidad_maxima, combustible,
                 numero_ruedas, capacidad_pasajeros, anio, precio, encendido):
        
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.combustible = combustible
        self.numero_ruedas = numero_ruedas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.anio = anio
        self.precio = precio
        self.encendido = encendido

    def mostrarDatos(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Módelo: {self.modelo}")
        print(f"Velocidad máxima: {self.velocidad_maxima}")
        print(f"Combustible: {self.combustible}")
        print(f"Número de ruedas: {self.numero_ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
        print(f"Año de expedición: {self.anio}")
        print(f"Precio: {self.precio}")
        print(f"¿Está encendido?: {self.encendido}")

    def encender(self):
        print("El transporte está encedido")

    def apagar(self):
        print("El trasnporte está apagado")

    def acelerar(self, velocidad):
        print("Acelerando a: ", velocidad)

    def frenar(self):
        print("Frenando")

    def repostar(self, combustible):
        print("Cargando gasolina: ", combustible)

toyota = Transporte("Toyota", "Rojo", "Corolla", 180,
                    "Gasolina", 4, 5, 2020, 300000, False)

toyota.mostrarDatos()
toyota.encender()
toyota.acelerar("120km/h")
toyota.frenar()
toyota.repostar("Gasolina Magna")
toyota.apagar()

"""
Atributos                           Métodos                     Objeto (Toyota)

1. Marca                            1. Encender                 Toyota
2. Color                            2. Apagar                   Rojo
3. Módelo                           3. Acelerar                 Corolla
4. Velocidad máxima                 4. Frenar                   180
5. Combustible                      5. Repostar                 Gasolina
6. Número de ruedas                                             4
7. Capacidad de pasajeros                                       5
8. Año                                                          2020
9. Precio                                                       300000
10. Encendido                                                   False
"""