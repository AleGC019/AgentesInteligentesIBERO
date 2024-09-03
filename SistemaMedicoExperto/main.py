from medico import Medico
from paciente import Paciente
from enfermedad import Enfermedad
from diagnostico import Diagnostico


enfermedades = [
    Enfermedad("Gripe", ["fiebre", "tos", "cansancio"]),
    Enfermedad("Covid-19", ["fiebre", "tos", "falta de aire"]),
    Enfermedad("Resfriado", ["congestion nasal", "estornudos", "dolor de garganta"]),
    Enfermedad("Infección urinaria", ["dolor al orinar", "orina turbia", "necesidad frecuente de orinar"]),
    Enfermedad("Gastritis", ["dolor abdominal", "nauseas", "vomitos", "sensacion de llenura"]),
    Enfermedad("Diabetes", ["sed excesiva", "orina frecuente", "fatiga", "vision borrosa"]),
    Enfermedad("Hipertensión", ["dolor de cabeza", "fatiga", "vision borrosa", "dificultad para respirar"]),
    Enfermedad("Anemia", ["cansancio", "palidez", "dolor de cabeza", "mareos"]),
    Enfermedad("Asma", ["tos", "sibilancias", "opresion en el pecho", "dificultad para respirar"]),
    Enfermedad("Artritis", ["dolor articular", "rigidez", "hinchazon", "enrojecimiento"]),
    Enfermedad("Colesterol alto", ["dolor en el pecho", "fatiga", "mareos", "palpitaciones"]),
    Enfermedad("Depresión", ["tristeza", "fatiga", "insomnio", "perdida de interes"]),
    Enfermedad("Migraña", ["dolor de cabeza", "nauseas", "sensibilidad a la luz", "sensibilidad al sonido"]),
    Enfermedad("Neumonía", ["tos", "fiebre", "escalofrios", "dolor de pecho"]),
    Enfermedad("Conjuntivitis", ["enrojecimiento", "picazon", "lagrimeo", "sensibilidad a la luz"]),
    Enfermedad("Celulitis", ["enrojecimiento", "hinchazon", "dolor", "calor"]),
    Enfermedad("Bronquitis", ["tos", "mucosidad", "fatiga", "dificultad para respirar"]),
    Enfermedad("Sinusitis", ["dolor facial", "congestion nasal", "secrecion nasal", "dolor de cabeza"]),
    Enfermedad("Otitis", ["dolor de oido", "secrecion del oido", "perdida de audicion"]),
    Enfermedad("Hepatitis", ["ictericia", "fatiga", "dolor abdominal", "nauseas"]),
    Enfermedad("Gastroenteritis", ["diarrea", "vomitos", "dolor abdominal", "fiebre"]),
    Enfermedad("Dermatitis", ["erupcion cutanea", "picazon", "enrojecimiento", "hinchazon"]),
    Enfermedad("Eczema", ["piel seca", "picazon", "enrojecimiento", "descamacion"]),
    Enfermedad("Psoriasis", ["placas rojas", "picazon", "descamacion", "dolor"]),
    Enfermedad("Alergia", ["estornudos", "picazon", "congestion nasal", "erupcion cutanea"]),
    Enfermedad("Cistitis", ["dolor al orinar", "orina turbia", "necesidad frecuente de orinar", "dolor pelvico"]),
    Enfermedad("Tuberculosis", ["tos persistente", "fiebre", "sudores nocturnos", "perdida de peso"]),
    Enfermedad("Varicela", ["erupcion cutanea", "fiebre", "cansancio", "perdida de apetito"]),
    Enfermedad("Sarampión", ["erupción cutanea", "fiebre", "tos", "conjuntivitis"]),
    Enfermedad("Rubeola", ["erupcion cutanea", "fiebre", "dolor de cabeza", "ganglios inflamados"]),
    Enfermedad("Tos ferina", ["tos persistente", "fiebre", "fatiga", "vomitos"]),
    Enfermedad("Meningitis", ["fiebre", "dolor de cabeza", "rigidez en el cuello", "nauseas"]),
    Enfermedad("Hepatitis B", ["ictericia", "fatiga", "dolor abdominal", "nauseas"]),
    Enfermedad("Hepatitis C", ["ictericia", "fatiga", "dolor abdominal", "nauseas"]),
    Enfermedad("VIH/SIDA", ["fiebre", "fatiga", "perdida de peso", "infecciones recurrentes"]),
    Enfermedad("Lupus", ["fatiga", "dolor articular", "erupcion cutanea", "fiebre"]),
    Enfermedad("Esclerosis múltiple", ["fatiga", "debilidad muscular", "problemas de vision", "mareos"]),
    Enfermedad("Parkinson", ["temblores", "rigidez muscular", "problemas de equilibrio", "lentitud de movimientos"]),
    Enfermedad("Alzheimer", ["perdida de memoria", "confusion", "cambios de humor", "dificultad para hablar"]),
    Enfermedad("Epilepsia", ["convulsiones", "perdida de conciencia", "confusion", "movimientos incontrolables"]),
    Enfermedad("Fibromialgia", ["dolor muscular", "fatiga", "problemas de sueño", "dificultad para concentrarse"]),
    Enfermedad("Enfermedad de Crohn", ["dolor abdominal", "diarrea", "fatiga", "perdida de peso"]),
    Enfermedad("Colitis ulcerosa", ["dolor abdominal", "diarrea", "sangrado rectal", "fatiga"]),
    Enfermedad("Síndrome del intestino irritable", ["dolor abdominal", "diarrea", "estreñimiento", "hinchazon"]),
    Enfermedad("Celiaquía", ["dolor abdominal", "diarrea", "perdida de peso", "fatiga"]),
    Enfermedad("Enfermedad de Lyme", ["erupcion cutanea", "fiebre", "dolor de cabeza", "fatiga"]),
    Enfermedad("Mononucleosis", ["fiebre", "dolor de garganta", "fatiga", "inflamacion de ganglios"]),
    Enfermedad("Escarlatina", ["erupcion cutanea", "fiebre", "dolor de garganta", "lengua enrojecida"]),
    Enfermedad("Dengue", ["fiebre alta", "dolor de cabeza", "dolor muscular", "erupcion cutanea"]),
    Enfermedad("Zika", ["fiebre", "erupcion cutanea", "dolor articular", "conjuntivitis"]),
    Enfermedad("Chikungunya", ["fiebre", "dolor articular", "erupcion cutanea", "dolor de cabeza"]),
    Enfermedad("Malaria", ["fiebre", "escalofrios", "sudoracion", "dolor de cabeza"]),
]

def mostrar_encabezado():
    print("=" * 50)
    print(" " * 15 + "Sistema de Diagnóstico")
    print("=" * 50)


def solicitar_sintomas():
    sintomas = []
    for i in range(4):
        sintoma = input(f"Ingrese el síntoma {i + 1} (o 'n' para terminar): ")
        if sintoma.lower() == 'n':
            break
        sintomas.append(sintoma)
    return sintomas


def main():
    medico = Medico("Dr. House", enfermedades)
    mostrar_encabezado()
    nombre_paciente = input("Ingrese el nombre del paciente: ")
    sintomas_paciente = solicitar_sintomas()

    paciente = Paciente(nombre_paciente, sintomas_paciente)
    print("\n" + "=" * 50)
    print(f"Paciente: {paciente.nombre}")
    print(f"Sintomas: {', '.join(paciente.sintomas)}")
    print("=" * 50 + "\n")

    diagnostico = Diagnostico(medico, paciente)
    print(diagnostico.diagnosticar())


if __name__ == "__main__":
    main()