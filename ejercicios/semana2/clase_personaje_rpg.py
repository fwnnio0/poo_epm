class PersonajeRPG:
    def __init__(self, nombre, vida, nivel, fuerza, velocidad, inteligencia,
                 tipo_arma, defensa, expericencia, energia):
        
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.inteligencia = inteligencia
        self.tipo_arma = tipo_arma
        self.defensa = defensa
        self.experiencia = expericencia
        self.energia = energia

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Tipo de arma: {self.tipo_arma}")
        print(f"Defensa: {self.defensa}")
        print(f"Expericiencia: {self.experiencia}")
        print(f"Energía: {self.energia}")
    
    def usarHabilidad(self, habilidad):
        print("Su habilidad: ", habilidad)

    def completarMision(self, mision):
        print("Su misión: ", mision)

    def equiparObjeto(self, objeto):
        print("Su objeto: ", objeto)

    def atacarEnemigo(self, enemigo):
        print("Su enemigo: ", enemigo)

    def decirFrase(self, frase):
        print("Su frase: ", frase)

    def morir(self):
        print("Derrotado")

gwen = PersonajeRPG("Gwen", 620, 1, 75, 85, 90, "Tijeras Mágicas",
                    40, 0, 100)

gwen.mostrarDatos()
gwen.usarHabilidad("Corte Celestial")
gwen.completarMision("Defender el Nexo")
gwen.equiparObjeto("Ore espiritual")
gwen.atacarEnemigo("Yasuo")
gwen.decirFrase("El viento lo elige todo")
gwen.morir

"""
Atributos                               Métodos                         Objeto (Gwen)
1. Nombre                               1. Usar Habilidad               Gwen
2. Vida                                 2. Completar Misión             620
3. Nivel                                3. Equipar Objeto               1
4. Fuerza                               4. Atacar Enemigo               75
5. Velocidad                            5. Decir Frase                  85
6. Inteligencia                         6. Morir                        90
7. Tipo de arma                                                         Tijeras Mágicas
8. Defensa                                                              40
9. Expericiencia                                                        0
10. Energía                                                             100
"""