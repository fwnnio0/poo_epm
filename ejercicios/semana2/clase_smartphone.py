class Smartphone:
    def __init__(self, marca, color, numero_telefono, modelo, sistema_operativo, 
                capacidad_almacenamiento, memoria_ram, esta_encendido,
                esta_bloqueado, porcentaje_bateria):
        
        self.marca = marca
        self.color = color
        self.numero_telefono = numero_telefono
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.capacidad_almacenamiento = capacidad_almacenamiento
        self.memoria_ram = memoria_ram
        self.esta_encendido = esta_encendido
        self.esta_bloqueado = esta_bloqueado
        self.porcentaje_bateria = porcentaje_bateria

        print(f"Marca del teléfono: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Número de teléfono: {self.numero_telefono}")
        print(f"Módelo: {self.modelo}")
        print(f"Sistema Operativo: {self.sistema_operativo}")
        print(f"Capacidad de alamacenamiento: {self.capacidad_almacenamiento}")
        print(f"Memoria Ram: {self.memoria_ram}")
        print(f"¿Está encendido?: {self.esta_encendido}")
        print(f"¿Está bloqueado?: {self.esta_bloqueado}")
        print(f"Porcentaje de la batería: {self.porcentaje_bateria}")

s26ultra = Smartphone("Samsung", "Verde limón", +527751897762, "Samsung Galaxy S26 Ultra",
                      "Android 16", 256, 16, True, False, 80)

"""
Atributos                               Objeto (Samsung Galaxy S26 Ultra)

1. Marca                                Samsung Galaxy
2. Color                                Verde Limón
3. Número de teléfono                   +527751897762
4. Módelo                               Samsung Galaxy S26 Ultra
5. Sistema Operativo                    Android 16
6. Capacidad de almacenamiento          256 GB
7. Memoria RAM                          16 GB
8. Está encendido                       True
9. Está bloqueado                       False
10. Porcentaje de batería               80
"""