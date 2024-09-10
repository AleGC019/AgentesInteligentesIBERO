import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

data = pd.read_csv('dataset_km_miles.csv')

x = data.drop('miles', axis=1)
y = data['miles']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Crear modelo
model = LinearRegression()

#Entrenar modelo
model.fit(x_train, y_train)

#Predecir
y_pred = model.predict(x_test)

#Evaluar modelo
print(f'MAE: {mean_absolute_error(y_test, y_pred)}')
print(f'MSE: {mean_squared_error(y_test, y_pred)}')
print(f'R2: {r2_score(y_test, y_pred)}')


#Graficar
plt.figure(dpi=200)
sns.scatterplot(x=x_test['km'], y=y_test)
sns.lineplot(x=x_test['km'], y=y_pred, color='red')
plt.xlabel('Kilometers')
plt.ylabel('Miles')
plt.title('Kilometers vs Miles')
plt.grid(True)
plt.show()

print(f'Reales: {y_test.values}\n')
print(f'Predicciones: {y_pred}')
