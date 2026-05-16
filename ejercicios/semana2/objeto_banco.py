class Banco:
    def __init__(self, no_clientes, no_elementos_seguridad, no_edificios, sistema_informatico,
                 nombre_banco, no_cajeros, fiable, capital, horario_atencion, color_banco):

        self.no_clientes = no_clientes
        self.no_elementos_seguridad = no_elementos_seguridad
        self.no_edificios = no_edificios
        self.sistema_informatico = sistema_informatico
        self.nombre_banco = nombre_banco
        self.no_cajeros = no_cajeros
        self.fiable = fiable
        self.capital = capital
        self.horario_atencion = horario_atencion
        self.color_banco = color_banco

        print(f"Número de clientes: {self.no_clientes}")
        print(f"Número de elementos de seguridad: {self.no_elementos_seguridad}")
        print(f"Número de edificios: {self.no_edificios}")
        print(f"Sistema informático: {self.sistema_informatico}")
        print(f"Nombre del banco: {self.nombre_banco}")
        print(f"Número de cajeros: {self.no_cajeros}")
        print(f"¿Es fiable?: {self.fiable}")
        print(f"Capital: {self.capital}")
        print(f"Horario de atención: {self.horario_atencion}")
        print(f"Color del banco: {self.color_banco}")

acme = Banco(10000, None, None, "ACME 0.1", "ACME", 10000, True, 1000000, "9:00 am - 19:00 pm",
             "Verde fosforescente")

"""
Atributo                                Objeto

1. No. Clientes                         10000
2. Seguridad                            None
3. Infraestructura                      None
4. Sistema                              ACME 01
5. Nombre                               ACME
6. No. Cajeros                          10000
7. Fiable                               True
8. Capital                              1000000
9. Horario de atención                  9am - 7pm
10. Color                               Verde fosoforescente
"""