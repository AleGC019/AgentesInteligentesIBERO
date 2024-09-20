import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Cargar los datos
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Preprocesamiento de datos
# Rellenar los valores faltantes en la columna 'Age' con la mediana
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median())
test_data['Age'] = test_data['Age'].fillna(test_data['Age'].median())

# Rellenar los valores faltantes en 'Embarked' con el valor más frecuente
train_data['Embarked'] = train_data['Embarked'].fillna(train_data['Embarked'].mode()[0])

# Rellenar el único valor faltante en 'Fare' en el conjunto de test con la mediana
test_data['Fare'] = test_data['Fare'].fillna(test_data['Fare'].median())

# Eliminar la columna 'Cabin' porque tiene demasiados valores faltantes
train_data = train_data.drop('Cabin', axis=1)
test_data = test_data.drop('Cabin', axis=1)

# Convertir las variables categóricas ('Sex', 'Embarked') en variables dummy
train_data = pd.get_dummies(train_data, columns=['Sex', 'Embarked'], drop_first=True)
test_data = pd.get_dummies(test_data, columns=['Sex', 'Embarked'], drop_first=True)

# Eliminar columnas irrelevantes ('PassengerId', 'Name', 'Ticket')
train_data = train_data.drop(['PassengerId', 'Name', 'Ticket'], axis=1)
test_data = test_data.drop(['PassengerId', 'Name', 'Ticket'], axis=1)

# Separar las características (X) y la variable objetivo (y)
X_train = train_data.drop('Survived', axis=1)
y_train = train_data['Survived']

# Inicializar los modelos
log_reg = LogisticRegression(max_iter=1000)
decision_tree = DecisionTreeClassifier(random_state=42)
random_forest = RandomForestClassifier(random_state=42)

# Entrenar los modelos
log_reg.fit(X_train, y_train)
decision_tree.fit(X_train, y_train)
random_forest.fit(X_train, y_train)

# Evaluar los modelos en el conjunto de entrenamiento
y_pred_log_reg = log_reg.predict(X_train)
y_pred_dec_tree = decision_tree.predict(X_train)
y_pred_rand_forest = random_forest.predict(X_train)

# Mostrar resultados
print("Logistic Regression Accuracy:", accuracy_score(y_train, y_pred_log_reg))
print("Logistic Regression Report:\n", classification_report(y_train, y_pred_log_reg))

print("Decision Tree Accuracy:", accuracy_score(y_train, y_pred_dec_tree))
print("Decision Tree Report:\n", classification_report(y_train, y_pred_dec_tree))

print("Random Forest Accuracy:", accuracy_score(y_train, y_pred_rand_forest))
print("Random Forest Report:\n", classification_report(y_train, y_pred_rand_forest))

# Predicciones en el conjunto de prueba
test_pred_log_reg = log_reg.predict(test_data)
test_pred_dec_tree = decision_tree.predict(test_data)
test_pred_rand_forest = random_forest.predict(test_data)

# Crear un dataframe con las predicciones
test_predictions = pd.DataFrame({
    'Logistic Regression': test_pred_log_reg,
    'Decision Tree': test_pred_dec_tree,
    'Random Forest': test_pred_rand_forest
})

# Mostrar las predicciones
print(test_predictions.head())

