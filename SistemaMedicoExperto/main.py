from queue import PriorityQueue

class Medico:
    def __init__(self, nombre, conocimientos):
        self.nombre = nombre
        self.conocimientos = conocimientos  # Lista de enfermedades que puede diagnosticar


class Paciente:
    def __init__(self, nombre, sintomas):
        self.nombre = nombre
        self.sintomas = sintomas  # Lista de síntomas


class Enfermedad:
    def __init__(self, nombre, sintomas):
        self.nombre = nombre
        self.sintomas = sintomas  # Lista de síntomas asociados a la fermented

    def __lt__(self, other):
        return self.nombre < other.nombre


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
        max_coincidencias = 0

        for enfermedad in self.medico.conocimientos:
            coincidencias = self.calcular_coincidencias(enfermedad)
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_enfermedad = enfermedad

        return mejor_enfermedad

    def calcular_coincidencias(self, enfermedad):
        return sum(1 for sintoma in enfermedad.sintomas if sintoma in self.paciente.sintomas)

def solicitar_sintomas():
    sintomas = []
    for i in range(4):
        sintoma = input(f"Ingrese el síntoma {i+1} (o 'n' para terminar): ")
        if sintoma.lower() == 'n':
            break
        sintomas.append(sintoma)
    return sintomas

enfermedades = [
    Enfermedad("Gripe", ["fiebre", "tos", "cansancio"]),
    Enfermedad("Covid-19", ["fiebre", "tos", "falta de aire"]),
    Enfermedad("Resfriado", ["congestión nasal", "estornudos", "dolor de garganta"]),
    Enfermedad("Infección urinaria", ["dolor al orinar", "orina turbia", "necesidad frecuente de orinar"]),
    Enfermedad("Gastritis", ["dolor abdominal", "náuseas", "vómitos", "sensación de llenura"]),
    Enfermedad("Diabetes", ["sed excesiva", "orina frecuente", "fatiga", "visión borrosa"]),
    Enfermedad("Hipertensión", ["dolor de cabeza", "fatiga", "visión borrosa", "dificultad para respirar"]),
    Enfermedad("Anemia", ["cansancio", "palidez", "dolor de cabeza", "mareos"]),
    Enfermedad("Asma", ["tos", "sibilancias", "opresión en el pecho", "dificultad para respirar"]),
    Enfermedad("Artritis", ["dolor articular", "rigidez", "hinchazón", "enrojecimiento"]),
    Enfermedad("Colesterol alto", ["dolor en el pecho", "fatiga", "mareos", "palpitaciones"]),
    Enfermedad("Depresión", ["tristeza", "fatiga", "insomnio", "pérdida de interés"]),
    Enfermedad("Migraña", ["dolor de cabeza", "náuseas", "sensibilidad a la luz", "sensibilidad al sonido"]),
    Enfermedad("Neumonía", ["tos", "fiebre", "escalofríos", "dolor de pecho"]),
    Enfermedad("Conjuntivitis", ["enrojecimiento", "picazón", "lagrimeo", "sensibilidad a la luz"]),
    Enfermedad("Celulitis", ["enrojecimiento", "hinchazón", "dolor", "calor"]),
    Enfermedad("Bronquitis", ["tos", "mucosidad", "fatiga", "dificultad para respirar"]),
    Enfermedad("Sinusitis", ["dolor facial", "congestión nasal", "secreción nasal", "dolor de cabeza"]),
    Enfermedad("Otitis", ["dolor de oído", "secreción del oído", "pérdida de audición"]),
    Enfermedad("Hepatitis", ["ictericia", "fatiga", "dolor abdominal", "náuseas"]),
    Enfermedad("Gastroenteritis", ["diarrea", "vómitos", "dolor abdominal", "fiebre"]),
    Enfermedad("Dermatitis", ["erupción cutánea", "picazón", "enrojecimiento", "hinchazón"]),
    Enfermedad("Eczema", ["piel seca", "picazón", "enrojecimiento", "descamación"]),
    Enfermedad("Psoriasis", ["placas rojas", "picazón", "descamación", "dolor"]),
    Enfermedad("Alergia", ["estornudos", "picazón", "congestión nasal", "erupción cutánea"]),
    Enfermedad("Cistitis", ["dolor al orinar", "orina turbia", "necesidad frecuente de orinar", "dolor pélvico"]),
    Enfermedad("Tuberculosis", ["tos persistente", "fiebre", "sudores nocturnos", "pérdida de peso"]),
    Enfermedad("Varicela", ["erupción cutánea", "fiebre", "cansancio", "pérdida de apetito"]),
    Enfermedad("Sarampión", ["erupción cutánea", "fiebre", "tos", "conjuntivitis"]),
    Enfermedad("Rubeola", ["erupción cutánea", "fiebre", "dolor de cabeza", "ganglios inflamados"]),
    Enfermedad("Tos ferina", ["tos persistente", "fiebre", "fatiga", "vómitos"]),
    Enfermedad("Meningitis", ["fiebre", "dolor de cabeza", "rigidez en el cuello", "náuseas"]),
    Enfermedad("Hepatitis B", ["ictericia", "fatiga", "dolor abdominal", "náuseas"]),
    Enfermedad("Hepatitis C", ["ictericia", "fatiga", "dolor abdominal", "náuseas"]),
    Enfermedad("VIH/SIDA", ["fiebre", "fatiga", "pérdida de peso", "infecciones recurrentes"]),
    Enfermedad("Lupus", ["fatiga", "dolor articular", "erupción cutánea", "fiebre"]),
    Enfermedad("Esclerosis múltiple", ["fatiga", "debilidad muscular", "problemas de visión", "mareos"]),
    Enfermedad("Parkinson", ["temblores", "rigidez muscular", "problemas de equilibrio", "lentitud de movimientos"]),
    Enfermedad("Alzheimer", ["pérdida de memoria", "confusión", "cambios de humor", "dificultad para hablar"]),
    Enfermedad("Epilepsia", ["convulsiones", "pérdida de conciencia", "confusión", "movimientos incontrolables"]),
    Enfermedad("Fibromialgia", ["dolor muscular", "fatiga", "problemas de sueño", "dificultad para concentrarse"]),
    Enfermedad("Enfermedad de Crohn", ["dolor abdominal", "diarrea", "fatiga", "pérdida de peso"]),
    Enfermedad("Colitis ulcerosa", ["dolor abdominal", "diarrea", "sangrado rectal", "fatiga"]),
    Enfermedad("Síndrome del intestino irritable", ["dolor abdominal", "diarrea", "estreñimiento", "hinchazón"]),
    Enfermedad("Celiaquía", ["dolor abdominal", "diarrea", "pérdida de peso", "fatiga"]),
    Enfermedad("Enfermedad de Lyme", ["erupción cutánea", "fiebre", "dolor de cabeza", "fatiga"]),
    Enfermedad("Mononucleosis", ["fiebre", "dolor de garganta", "fatiga", "inflamación de ganglios"]),
    Enfermedad("Escarlatina", ["erupción cutánea", "fiebre", "dolor de garganta", "lengua enrojecida"]),
    Enfermedad("Dengue", ["fiebre alta", "dolor de cabeza", "dolor muscular", "erupción cutánea"]),
    Enfermedad("Zika", ["fiebre", "erupción cutánea", "dolor articular", "conjuntivitis"]),
    Enfermedad("Chikungunya", ["fiebre", "dolor articular", "erupción cutánea", "dolor de cabeza"]),
    Enfermedad("Malaria", ["fiebre", "escalofríos", "sudoración", "dolor de cabeza"]),
    Enfermedad("Fiebre tifoidea", ["fiebre alta", "dolor abdominal", "diarrea", "erupción cutánea"]),
    Enfermedad("Brucelosis", ["fiebre", "sudoración", "dolor muscular", "fatiga"]),
    Enfermedad("Leptospirosis", ["fiebre", "dolor muscular", "dolor de cabeza", "ictericia"]),
    Enfermedad("Tétanos", ["rigidez muscular", "espasmos", "dificultad para tragar", "fiebre"]),
    Enfermedad("Rabia", ["fiebre", "dolor de cabeza", "ansiedad", "espasmos musculares"]),
    Enfermedad("Ébola", ["fiebre alta", "hemorragias", "dolor muscular", "vómitos"]),
    Enfermedad("Hantavirus", ["fiebre", "dolor muscular", "dificultad para respirar", "tos"]),
    Enfermedad("Fiebre amarilla", ["fiebre", "ictericia", "dolor muscular", "vómitos"]),
    Enfermedad("Gonorrea", ["dolor al orinar", "secreción", "dolor abdominal", "sangrado"]),
    Enfermedad("Sífilis", ["úlceras", "erupción cutánea", "fiebre", "dolor de cabeza"]),
    Enfermedad("Clamidia", ["dolor al orinar", "secreción", "dolor abdominal", "sangrado"]),
    Enfermedad("Herpes", ["ampollas", "dolor al orinar", "picazón", "fiebre"]),
    Enfermedad("Candidiasis", ["picazón", "secreción", "dolor al orinar", "enrojecimiento"]),
    Enfermedad("Tricomoniasis", ["secreción", "picazón", "dolor al orinar", "olor fuerte"]),
    Enfermedad("Vaginosis bacteriana", ["secreción", "olor fuerte", "picazón", "dolor al orinar"]),
    Enfermedad("Gripe aviar", ["fiebre", "tos", "dolor muscular", "dificultad para respirar"]),
    Enfermedad("Gripe porcina", ["fiebre", "tos", "dolor muscular", "fatiga"]),
    Enfermedad("Fiebre del Nilo Occidental", ["fiebre", "dolor de cabeza", "dolor muscular", "erupción cutánea"]),
    Enfermedad("Encefalitis japonesa", ["fiebre", "dolor de cabeza", "vómitos", "convulsiones"]),
    Enfermedad("Tifoidea", ["fiebre alta", "dolor abdominal", "diarrea", "erupción cutánea"]),
    Enfermedad("Brucelosis", ["fiebre", "sudoración", "dolor muscular", "fatiga"]),
    Enfermedad("Leptospirosis", ["fiebre", "dolor muscular", "dolor de cabeza", "ictericia"]),
    Enfermedad("Tétanos", ["rigidez muscular", "espasmos", "dificultad para tragar", "fiebre"]),
    Enfermedad("Rabia", ["fiebre", "dolor de cabeza", "ansiedad", "espasmos musculares"]),
    Enfermedad("Ébola", ["fiebre alta", "hemorragias", "dolor muscular", "vómitos"]),
    Enfermedad("Hantavirus", ["fiebre", "dolor muscular", "dificultad para respirar", "tos"]),
    Enfermedad("Fiebre amarilla", ["fiebre", "ictericia", "dolor muscular", "vómitos"]),
    Enfermedad("Gonorrea", ["dolor al orinar", "secreción", "dolor abdominal", "sangrado"]),
    Enfermedad("Sífilis", ["úlceras", "erupción cutánea", "fiebre", "dolor de cabeza"]),
    Enfermedad("Clamidia", ["dolor al orinar", "secreción", "dolor abdominal", "sangrado"]),
    Enfermedad("Herpes", ["ampollas", "dolor al orinar", "picazón", "fiebre"]),
    Enfermedad("Candidiasis", ["picazón", "secreción", "dolor al orinar", "enrojecimiento"]),
    Enfermedad("Tricomoniasis", ["secreción", "picazón", "dolor al orinar", "olor fuerte"]),
    Enfermedad("Vaginosis bacteriana", ["secreción", "olor fuerte", "picazón", "dolor al orinar"]),
    Enfermedad("Gripe aviar", ["fiebre", "tos", "dolor muscular", "dificultad para respirar"]),
    Enfermedad("Gripe porcina", ["fiebre", "tos", "dolor muscular", "fatiga"]),
    Enfermedad("Fiebre del Nilo Occidental", ["fiebre", "dolor de cabeza", "dolor muscular", "erupción cutánea"]),
    Enfermedad("Encefalitis japonesa", ["fiebre", "dolor de cabeza", "vómitos", "convulsiones"]),
    Enfermedad("Mononucleosis", ["fiebre", "dolor de garganta", "fatiga", "inflamación de ganglios"]),
    Enfermedad("Escarlatina", ["erupción cutánea", "fiebre", "dolor de garganta", "lengua enrojecida"]),
    Enfermedad("Dengue", ["fiebre alta", "dolor de cabeza", "dolor muscular", "erupción cutánea"]),
    Enfermedad("Zika", ["fiebre", "erupción cutánea", "dolor articular", "conjuntivitis"]),
    Enfermedad("Chikungunya", ["fiebre", "dolor articular", "erupción cutánea", "dolor de cabeza"]),
    Enfermedad("Malaria", ["fiebre", "escalofríos", "sudoración", "dolor de cabeza"]),
]

medico = Medico("Dr. House", enfermedades)

nombre_paciente = input("Ingrese el nombre del paciente: ")
sintomas_paciente = solicitar_sintomas()

paciente = Paciente(nombre_paciente, sintomas_paciente)
print(f"Paciente: {paciente.nombre}, Síntomas: {paciente.sintomas}")

diagnostico = Diagnostico(medico, paciente)

print(diagnostico.diagnosticar())
