#############################################
#   UNIVERSIDAD IBEROAMERICANA DE PUEBLA    #
#   Tema 5 - Sistemas expertos              #
#   Eguizabal Medrano, Fernando Andres      #
#############################################

# Se debe descargar la librería networkx para poder ejecutar el programa
import networkx as nx

# Creación del grafo
grafo_diagnostico = nx.Graph()

# Agregar nodos de enfermedades
enfermedades = [
    "gripe", "resfriado_comun", "alergia_estacional", "gastroenteritis",
    "migraña", "sinusitis", "bronquitis_aguda", "conjuntivitis", "indigestion", "fatiga_cronica"
]

# Agregamos las enfermedades al grafo
for enfermedad in enfermedades:
    grafo_diagnostico.add_node(enfermedad)

# Agregar nodos de síntomas y conectar con enfermedades, asignando pesos que reflejan la probabilidad de ocurrencia de dicho síntoma en la enfermedad
grafo_diagnostico.add_edge("fiebre", "gripe", weight=0.9)
grafo_diagnostico.add_edge("tos", "gripe", weight=0.7)
grafo_diagnostico.add_edge("dolor_de_cabeza", "gripe", weight=0.7)
grafo_diagnostico.add_edge("dolor_muscular", "gripe", weight=0.8)
grafo_diagnostico.add_edge("fatiga", "gripe", weight=0.6)

grafo_diagnostico.add_edge("tos", "resfriado_comun", weight=0.7)
grafo_diagnostico.add_edge("congestion_nasal", "resfriado_comun", weight=0.8)
grafo_diagnostico.add_edge("dolor_de_garganta", "resfriado_comun", weight=0.7)
grafo_diagnostico.add_edge("estornudos", "resfriado_comun", weight=0.6)
grafo_diagnostico.add_edge("fatiga_leve", "resfriado_comun", weight=0.5)

grafo_diagnostico.add_edge("estornudos", "alergia_estacional", weight=0.8)
grafo_diagnostico.add_edge("picazon_en_los_ojos", "alergia_estacional", weight=0.9)
grafo_diagnostico.add_edge("congestion_nasal", "alergia_estacional", weight=0.7)
grafo_diagnostico.add_edge("tos", "alergia_estacional", weight=0.6)
grafo_diagnostico.add_edge("ojos_llorosos", "alergia_estacional", weight=0.7)

grafo_diagnostico.add_edge("nauseas", "gastroenteritis", weight=0.8)
grafo_diagnostico.add_edge("diarrea", "gastroenteritis", weight=0.9)
grafo_diagnostico.add_edge("dolor_abdominal", "gastroenteritis", weight=0.9)
grafo_diagnostico.add_edge("vomitos", "gastroenteritis", weight=0.8)
grafo_diagnostico.add_edge("fatiga", "gastroenteritis", weight=0.6)

grafo_diagnostico.add_edge("dolor_de_cabeza_intenso", "migraña", weight=0.9)
grafo_diagnostico.add_edge("sensibilidad_a_la_luz", "migraña", weight=0.8)
grafo_diagnostico.add_edge("nauseas", "migraña", weight=0.7)
grafo_diagnostico.add_edge("mareo", "migraña", weight=0.6)
grafo_diagnostico.add_edge("vision_borrosa", "migraña", weight=0.5)

grafo_diagnostico.add_edge("dolor_facial", "sinusitis", weight=0.8)
grafo_diagnostico.add_edge("congestion_nasal", "sinusitis", weight=0.8)
grafo_diagnostico.add_edge("dolor_de_cabeza", "sinusitis", weight=0.7)
grafo_diagnostico.add_edge("fiebre_baja", "sinusitis", weight=0.6)
grafo_diagnostico.add_edge("tos", "sinusitis", weight=0.5)

grafo_diagnostico.add_edge("tos_persistente", "bronquitis_aguda", weight=0.9)
grafo_diagnostico.add_edge("flema", "bronquitis_aguda", weight=0.8)
grafo_diagnostico.add_edge("fatiga", "bronquitis_aguda", weight=0.7)
grafo_diagnostico.add_edge("fiebre_baja", "bronquitis_aguda", weight=0.6)
grafo_diagnostico.add_edge("dolor_en_el_pecho", "bronquitis_aguda", weight=0.7)

grafo_diagnostico.add_edge("ojos_rojos", "conjuntivitis", weight=0.9)
grafo_diagnostico.add_edge("picazon_en_los_ojos", "conjuntivitis", weight=0.8)
grafo_diagnostico.add_edge("secrecion_ocular", "conjuntivitis", weight=0.7)
grafo_diagnostico.add_edge("lagrimeo", "conjuntivitis", weight=0.6)
grafo_diagnostico.add_edge("sensibilidad_a_la_luz", "conjuntivitis", weight=0.5)

grafo_diagnostico.add_edge("dolor_abdominal", "indigestion", weight=0.8)
grafo_diagnostico.add_edge("hinchazon", "indigestion", weight=0.7)
grafo_diagnostico.add_edge("acidez_estomacal", "indigestion", weight=0.6)
grafo_diagnostico.add_edge("nauseas", "indigestion", weight=0.5)
grafo_diagnostico.add_edge("sensacion_de_saciedad", "indigestion", weight=0.4)

grafo_diagnostico.add_edge("cansancio_extremo", "fatiga_cronica", weight=0.9)
grafo_diagnostico.add_edge("dolor_muscular", "fatiga_cronica", weight=0.8)
grafo_diagnostico.add_edge("insomnio", "fatiga_cronica", weight=0.7)
grafo_diagnostico.add_edge("dificultad_para_concentrarse", "fatiga_cronica", weight=0.7)
grafo_diagnostico.add_edge("irritabilidad", "fatiga_cronica", weight=0.6)

# Umbral de tolerancia bajo el cual un síntoma se considera "representativo" de una enfermedad
umbral_tolerancia = 0.6

# Función para determinar diagnósticos
def diagnosticar_con_grafo(grafo, sintomas):
    enfermedades_posibles = {}
    coincidencias_completas = []

    # Por cada sintoma...
    for sintoma in sintomas:

        # Si el sintoma existe en el grafo...
        if sintoma in grafo:

            # Por cada enfermedad relacionada con el sintoma...
            for enfermedad in grafo.neighbors(sintoma):

                # Obtener el peso de la relación
                peso = grafo[sintoma][enfermedad]['weight']

                # Si el peso es mayor o igual al umbral de tolerancia...
                if peso >= umbral_tolerancia:

                    # Si la enfermedad ya existe en el diccionario de enfermedades posibles, sumar el peso al existente
                    if enfermedad in enfermedades_posibles:
                        enfermedades_posibles[enfermedad] += peso

                    else:
                        # Si no existe, agregar la enfermedad al diccionario con el peso
                        enfermedades_posibles[enfermedad] = peso

    # Una vez terminado el ciclo, se evalúan las coincidencias completas

    # Por cada enfermedad posible...
    for enfermedad in enfermedades_posibles.keys():

        # Se obtienen los síntomas conocidos de la enfermedad
        sintomas_conocidos = list(grafo.neighbors(enfermedad))

        # Si los síntomas conocidos son un subconjunto de los síntomas ingresados, se agrega la enfermedad a la lista de coincidencias completas
        if set(sintomas_conocidos).issubset(set(sintomas)):

            # Se agrega la enfermedad a la lista de coincidencias completas
            coincidencias_completas.append(enfermedad)

    # Se retornan las enfermedades posibles y las coincidencias completas
    return enfermedades_posibles, coincidencias_completas

# Función para calcular el porcentaje de coincidencia
def calcular_probabilidad(sintomas_ingresados, sintomas_conocidos):

    # Contar cuántos síntomas ingresados coinciden con los síntomas conocidos
    sintomas_coincidentes = len(set(sintomas_ingresados) & set(sintomas_conocidos))
    total_sintomas_conocidos = len(set(sintomas_conocidos))

    # Evitar la división por cero
    if total_sintomas_conocidos > 0:
        return (sintomas_coincidentes / total_sintomas_conocidos) * 100
    else:
        return 0.0

# INICIO DEL PROGRAMA
print("\n----- DIAGNÓSTICO MÉDICO -----")
print("Bienvenido al sistema de diagnóstico médico ALEFERMED.")
print("NOTA: Los síntomas deben ser ingresados en minúsculas y con espacios si son más de una palabra, "
      "ej.: cansancio extremo, insomnio...")

# Obtener y imprimir la lista de síntomas posibles (nodos que no son enfermedades)
sintomas_posibles = [nodo for nodo in grafo_diagnostico if nodo not in enfermedades]

print("\nLista de síntomas posibles a ingresar:")
for sintoma in sintomas_posibles:
    # Reemplazar guiones bajos por espacios
    sintoma_sin_guiones = sintoma.replace("_", " ")
    print(f"- {sintoma_sin_guiones}")

# Entrada de síntomas desde la consola
sintomas_ingresados = input("\nIngrese los síntomas que el paciente padece separados por comas: ").strip().split(", ")
sintomas_ingresados = [sintoma.strip().replace(" ", "_") for sintoma in sintomas_ingresados]

print("\nProcesando diagnóstico...")

# Mostrar diagnósticos
enfermedades_posibles, coincidencias_completas = diagnosticar_con_grafo(grafo_diagnostico, sintomas_ingresados)

if enfermedades_posibles:
    print("\nDiagnóstico(s) posible(s):")

    # Crear una lista de tuplas (enfermedad, probabilidad) para ordenar
    resultados = []

    for enfermedad, puntuacion in enfermedades_posibles.items():
        sintomas_conocidos = list(grafo_diagnostico.neighbors(enfermedad))  # Convertir a lista
        probabilidad = calcular_probabilidad(sintomas_ingresados, sintomas_conocidos)
        resultados.append((enfermedad.capitalize(), probabilidad))

    # Ordenar la lista de resultados por probabilidad en orden descendente
    resultados.sort(key=lambda x: x[1], reverse=True)

    for enfermedad, probabilidad in resultados:
        if enfermedad == resultados[0][0]:
            print(f"La enfermedad con mejor probabilidad de encajar en los sintomas es "
                  f"{enfermedad}: Probabilidad: {probabilidad:.2f}%")
        else:
            print(f"\n{enfermedad}:\nProbabilidad: {probabilidad:.2f}%")

    # Mostrar coincidencias completas
    if coincidencias_completas:
        print("\nPor la descripcion brindada, se encontraron algunas coincidencias completas de sus síntomas.")
        print("Puede que el diagnóstico no esté completo, pero estas enfermedades son las que más se ajustan a sus síntomas:")
        for enfermedad in coincidencias_completas:
            print(f"- {enfermedad.capitalize()}")
        print("Cabe recalcar que, de existir síntomas adicionales, estas posibles enfermedades podrían no ser las correctas.")

else:
    print("No se encontraron diagnósticos posibles con los síntomas proporcionados.")
