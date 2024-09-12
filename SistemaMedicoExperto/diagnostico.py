class Diagnostico:
    def __init__(self, medico, paciente):
        self.medico = medico
        self.paciente = paciente

    def diagnosticar(self):
        posible_diagnostico = self.encontrar_enfermedad()
        if posible_diagnostico:
            return f"El paciente {self.paciente.nombre} probablemente tiene {posible_diagnostico.nombre}."
        else:
            return "No se pudo determinar la enfermedad con los síntomas proporcionados."

    def encontrar_enfermedad(self):
        mejor_enfermedad = None
        max_puntaje = 0

        for enfermedad in self.medico.conocimientos:
            puntaje = self.calcular_puntaje(enfermedad)
            if puntaje > max_puntaje:
                max_puntaje = puntaje
                mejor_enfermedad = enfermedad

        return mejor_enfermedad

    def calcular_puntaje(self, enfermedad):
        coincidencias = sum(1 for sintoma in enfermedad.sintomas if sintoma in self.paciente.sintomas)
        sintomas_faltantes = len(enfermedad.sintomas) - coincidencias
        puntaje = coincidencias - sintomas_faltantes * 0.5  # Penaliza síntomas faltantes
        return puntaje