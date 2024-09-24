import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error, r2_score, roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# Cargar los datos
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Preprocesamiento de datos
# Rellenar los valores faltantes en la columna 'Age' con la mediana
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median())
test_data['Age'] = test_data['Age'].fillna(test_data['Age'].median())

# Rellenar los valores faltantes en 'Embarked' con el valor más frecuente
train_data['Embarked'] = train_data['Embarked'].fillna(train_data['Embarked'].mode()[0])
test_data['Embarked'] = test_data['Embarked'].fillna(test_data['Embarked'].mode()[0])

# Rellenar el único valor faltante en 'Fare' en el conjunto de test con la mediana
train_data['Fare'] = train_data['Fare'].fillna(train_data['Fare'].median())
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
print('\n\n')
print("Logistic Regression Accuracy:", accuracy_score(y_train, y_pred_log_reg))
print("Logistic Regression Report:\n\n", classification_report(y_train, y_pred_log_reg))
print("Logistic Regression Confusion Matrix:\n", confusion_matrix(y_train, y_pred_log_reg))
print("Logistic Regression MSE:", mean_squared_error(y_train, y_pred_log_reg))
print("Logistic Regression R2:", r2_score(y_train, y_pred_log_reg))
print("Logistic Regression ROC AUC:", roc_auc_score(y_train, log_reg.predict_proba(X_train)[:, 1]))
print('\n\n')

print("Decision Tree Accuracy:", accuracy_score(y_train, y_pred_dec_tree))
print("Decision Tree Report:\n\n", classification_report(y_train, y_pred_dec_tree))
print("Decision Tree Confusion Matrix:\n", confusion_matrix(y_train, y_pred_dec_tree))
print("Decision Tree MSE:", mean_squared_error(y_train, y_pred_dec_tree))
print("Decision Tree R2:", r2_score(y_train, y_pred_dec_tree))
print("Decision Tree ROC AUC:", roc_auc_score(y_train, decision_tree.predict_proba(X_train)[:, 1]))
print('\n\n')

print("Random Forest Accuracy:", accuracy_score(y_train, y_pred_rand_forest))
print("Random Forest Report:\n\n", classification_report(y_train, y_pred_rand_forest))
print("Random Forest Confusion Matrix:\n", confusion_matrix(y_train, y_pred_rand_forest))
print("Random Forest MSE:", mean_squared_error(y_train, y_pred_rand_forest))
print("Random Forest R2:", r2_score(y_train, y_pred_rand_forest))
print("Random Forest ROC AUC:", roc_auc_score(y_train, random_forest.predict_proba(X_train)[:, 1]))
print('\n')

# Graficar ROC y AUC
models = {
    "Logistic Regression": log_reg,
    "Decision Tree": decision_tree,
    "Random Forest": random_forest
}

plt.figure(figsize=(10, 8))
for model_name, model in models.items():
    y_pred_proba = model.predict_proba(X_train)[:, 1]
    fpr, tpr, _ = roc_curve(y_train, y_pred_proba)
    plt.plot(fpr, tpr, label=f'{model_name} (AUC = {roc_auc_score(y_train, y_pred_proba):.2f})')

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.show()

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

# Conteo de sobrevivientes y no sobrevivientes por cada modelo
log_reg_counts = test_predictions['Logistic Regression'].value_counts()
dec_tree_counts = test_predictions['Decision Tree'].value_counts()
rand_forest_counts = test_predictions['Random Forest'].value_counts()

print("Logistic Regression Counts:\n")
print("- No sobrevivientes:", log_reg_counts.get(0, 0))
print("- Sobrevivientes:", log_reg_counts.get(1, 0))
print('\n')

print("Decision Tree Counts:\n")
print("- No sobrevivientes:", dec_tree_counts.get(0, 0))
print("- Sobrevivientes:", dec_tree_counts.get(1, 0))
print('\n')

print("Random Forest Counts:\n")
print("- No sobrevivientes:", rand_forest_counts.get(0, 0))
print("- Sobrevivientes:", rand_forest_counts.get(1, 0))
print('\n')

# Teclada de espera para finalizar el programa
input("Presione Enter para finalizar...")