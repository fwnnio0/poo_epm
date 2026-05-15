class NombreClase:
    def __init__(self):
        print("Constructor")
    
    def metodoUno(self):
        print("Método Uno")

    def metodoDos(self, parametro_uno):
        print(f"Método Dos: {parametro_uno}")

nombre_objeto = NombreClase()
nombre_objeto.metodoUno()
nombre_objeto.metodoDos("Hola")