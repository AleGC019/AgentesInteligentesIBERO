import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_preprocess_data(file_path):
    # Cargar el dataset
    df = pd.read_csv(file_path, header=None)
    df.columns = ['car_ID', 'symboling', 'CarName', 'fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel',
                  'enginelocation', 'wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight', 'enginetype',
                  'cylindernumber', 'enginesize', 'fuelsystem', 'boreratio', 'stroke', 'compressionratio', 'horsepower',
                  'peakrpm', 'citympg', 'highwaympg', 'price']

    # Asegurarse de que la columna 'price' contiene solo valores numéricos
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Manejar valores faltantes en la columna 'price'
    df = df.dropna(subset=['price'])

    # Limpiar los nombres de las marcas de automóviles
    def clean_car_name(name):
        return name.split(' ')[0].lower()

    df['CarName'] = df['CarName'].apply(clean_car_name)

    # Diccionario de corrección de nombres de marcas
    corrections = {
        'maxda': 'mazda',
        'porcshce': 'porsche',
        'toyouta': 'toyota',
        'vokswagen': 'volkswagen',
        'vw': 'volkswagen'
    }

    df['CarName'] = df['CarName'].replace(corrections)

    # Columnas categóricas
    categorical_columns = ['CarName', 'fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel', 'enginelocation',
                           'enginetype', 'cylindernumber', 'fuelsystem']

    # Aplicar LabelEncoder a las columnas categóricas
    label_encoders = {}
    for col in categorical_columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    return df

# Cargar y preprocesar los datos
df = load_and_preprocess_data('CarPrice_Assignment.csv')

# Separar características (X) y variable objetivo (y)
X = df.drop(['price'], axis=1)
y = df['price']

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Entrenar el modelo de regresión lineal con restricciones no negativas
model = LinearRegression(positive=True)
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Calcular las métricas de evaluación
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Formatear los valores con separadores de miles y decimales
formatted_mse = "{:,.2f}".format(mse)
formatted_mae = "{:,.2f}".format(mae)

print(f'Mean Squared Error: {formatted_mse}')
print(f'Mean Absolute Error: {formatted_mae}')
print(f'R^2 Score: {r2}')
print('\n\n')

# Visualización de resultados
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.show()

# Gráfica de comparación de valores originales y predichos
plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Actual Prices', color='blue')
plt.plot(y_pred, label='Predicted Prices', color='red', linestyle='dashed')
plt.xlabel('Index')
plt.ylabel('Price')
plt.title('Comparison of Actual and Predicted Prices')
plt.legend()
plt.show()

# Crear una tabla de comparación de valores originales y predichos
comparison_df = pd.DataFrame({'Actual Price': y_test.values, 'Predicted Price': y_pred})

# Mostrar todos los valores en la tabla
pd.set_option('display.max_rows', None)
print(comparison_df)