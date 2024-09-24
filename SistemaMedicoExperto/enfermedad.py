class Enfermedad:
    def __init__(self, nombre, sintomas):
        self.nombre = nombre
        self.sintomas = sintomas  # Lista de síntomas asociados a la enfermedad

    def __lt__(self, other):
        return self.nombre < other.nombre