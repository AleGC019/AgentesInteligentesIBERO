import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix


# Lectura de datos
data = pd.read_csv('data.csv')

# Eliminación de columnas innecesarias
data = data.drop(['id', 'Unnamed: 32'], axis=1)

# Análisis exploratorio
print(data.head())
#print(data.describe())
#print(data.info())


label_encoder = LabelEncoder()
# Convertir la columna diagnosis a valores numéricos
data['diagnosis'] = label_encoder.fit_transform(data['diagnosis'])
#print(data.head())

# Separación de datos
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de regresión lineal
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

# Matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)

sns.heatmap(conf_matrix, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()


print('\n\n')

#Implementacion de formula de regresion lineal manual
#valores true positives
tp = conf_matrix[0][0]
#valores false positives
fp = conf_matrix[0][1]
#valores false negatives
fn = conf_matrix[1][0]
#valores true negatives
tn = conf_matrix[1][1]

#precision
precision = tp / (tp + fp)
print('Precision:', precision)
#Negative Predictive Value
npv = tn / (tn + fn)
print('Negative Predictive Value:', npv)
#Sensitivity
sensitivity = tp / (tp + fn)
print('Sensitivity:', sensitivity)
#Specificity
specificity = tn / (tn + fp)
print('Specificity:', specificity)
#F1 Score
f1 = 2 * (precision * sensitivity) / (precision + sensitivity)
print('F1 Score:', f1)
#Accuracy
accuracy = (tp + tn) / (tp + tn + fp + fn)
print('Accuracy:', accuracy)


print('\n\n')
print('Tabla')
# Valores de la matriz de confusión
tp = conf_matrix[0][0]
fp = conf_matrix[0][1]
fn = conf_matrix[1][0]
tn = conf_matrix[1][1]

# Cálculo de métricas
precision = tp / (tp + fp)
npv = tn / (tn + fn)
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)
f1 = 2 * (precision * sensitivity) / (precision + sensitivity)
accuracy = (tp + tn) / (tp + tn + fp + fn)

# Creación de DataFrame
metrics = {
    'Metric': ['Precision', 'Negative Predictive Value', 'Sensitivity', 'Specificity', 'F1 Score', 'Accuracy'],
    'Value': [precision, npv, sensitivity, specificity, f1, accuracy]
}
df_metrics = pd.DataFrame(metrics)

# Mostrar la tabla
print(df_metrics)

print('\n\n')
#Classification Report









