## Importar las bibliotecas necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Cargar los conjuntos de datos de entrenamiento y prueba
entrenamiento_df = pd.read_csv('train.csv')
prueba_df = pd.read_csv('test.csv')

# Eliminar columnas irrelevantes
entrenamiento_limpio = entrenamiento_df.drop(columns=['Name', 'Ticket', 'Cabin'])
prueba_limpio = prueba_df.drop(columns=['Name', 'Ticket', 'Cabin'])

# Imputar valores faltantes en el conjunto de entrenamiento
entrenamiento_limpio['Age'] = entrenamiento_limpio['Age'].fillna(entrenamiento_limpio['Age'].median())
entrenamiento_limpio['Embarked'] = entrenamiento_limpio['Embarked'].fillna(entrenamiento_limpio['Embarked'].mode()[0])

# Imputar valores faltantes en el conjunto de prueba
prueba_limpio['Age'] = prueba_limpio['Age'].fillna(prueba_limpio['Age'].median())
prueba_limpio['Embarked'] = prueba_limpio['Embarked'].fillna(prueba_limpio['Embarked'].mode()[0])

# Asegurarse de que no haya NaNs en el conjunto de prueba después de la imputación
# Rellenar cualquier NaN restante
prueba_limpio = prueba_limpio.fillna({
    'Age': prueba_limpio['Age'].median(),    # Imputar con la mediana en caso de NaN en Age
    'Fare': prueba_limpio['Fare'].median(),  # Asegurar que 'Fare' no tenga NaN
    'Embarked': prueba_limpio['Embarked'].mode()[0]  # Imputar con la moda en Embarked
})

# Verificar si quedan valores faltantes
print(entrenamiento_limpio.isnull().sum())
print(prueba_limpio.isnull().sum())

# Convertir las variables categóricas a numéricas usando LabelEncoder
codificador = LabelEncoder()

# Combinar los conjuntos de datos de entrenamiento y prueba para codificar las categorías
datos_combinados = pd.concat([entrenamiento_limpio[['Sex', 'Embarked']], prueba_limpio[['Sex', 'Embarked']]])

# Limpiar los tipos mixtos: reemplazar valores numéricos con las correspondientes cadenas de texto
datos_combinados['Sex'] = datos_combinados['Sex'].replace({1: 'male', 0: 'female'})
datos_combinados['Embarked'] = datos_combinados['Embarked'].replace({2: 'S', 0: 'C', 1: 'Q'})

# Ajustar el codificador para que los valores sean consistentes
datos_combinados['Sex'] = codificador.fit_transform(datos_combinados['Sex'])
datos_combinados['Embarked'] = codificador.fit_transform(datos_combinados['Embarked'])

# Separar los datos combinados de vuelta en los conjuntos de entrenamiento y prueba
entrenamiento_limpio['Sex'] = datos_combinados['Sex'].iloc[:len(entrenamiento_limpio)]
entrenamiento_limpio['Embarked'] = datos_combinados['Embarked'].iloc[:len(entrenamiento_limpio)]

prueba_limpio['Sex'] = datos_combinados['Sex'].iloc[len(entrenamiento_limpio):]
prueba_limpio['Embarked'] = datos_combinados['Embarked'].iloc[len(entrenamiento_limpio):]

# Separar las características (X) y la variable objetivo (y) en el conjunto de entrenamiento
X_entrenamiento = entrenamiento_limpio.drop(columns=['Survived', 'PassengerId'])
y_entrenamiento = entrenamiento_limpio['Survived']

# Extraer características del conjunto de prueba
X_prueba = prueba_limpio.drop(columns=['PassengerId'])

# Verificar si quedan valores faltantes en X_prueba
print(X_prueba.isnull().sum())

# Ajustar los IDs de pasajeros para las predicciones de prueba
ids_pasajeros_prueba = prueba_limpio['PassengerId']

# Definir los modelos de clasificación
modelo_regresion_logistica = LogisticRegression(max_iter=200)
modelo_arbol_decision = DecisionTreeClassifier(random_state=42)
modelo_bosque_aleatorio = RandomForestClassifier(random_state=42)

# Entrenar los modelos con el conjunto de entrenamiento
modelo_regresion_logistica.fit(X_entrenamiento, y_entrenamiento)
modelo_arbol_decision.fit(X_entrenamiento, y_entrenamiento)
modelo_bosque_aleatorio.fit(X_entrenamiento, y_entrenamiento)

# Hacer predicciones en el conjunto de prueba
predicciones_regresion_logistica = modelo_regresion_logistica.predict(X_prueba)
predicciones_arbol_decision = modelo_arbol_decision.predict(X_prueba)
predicciones_bosque_aleatorio = modelo_bosque_aleatorio.predict(X_prueba)

# Crear DataFrames con las predicciones para cada modelo
resultado_regresion_logistica = pd.DataFrame({'PassengerId': ids_pasajeros_prueba, 'Survived': predicciones_regresion_logistica})
resultado_arbol_decision = pd.DataFrame({'PassengerId': ids_pasajeros_prueba, 'Survived': predicciones_arbol_decision})
resultado_bosque_aleatorio = pd.DataFrame({'PassengerId': ids_pasajeros_prueba, 'Survived': predicciones_bosque_aleatorio})

# Guardar los resultados en archivos CSV
resultado_regresion_logistica.to_csv('log_reg_output.csv', index=False)
resultado_arbol_decision.to_csv('dec_tree_output.csv', index=False)
resultado_bosque_aleatorio.to_csv('rand_forest_output.csv', index=False)