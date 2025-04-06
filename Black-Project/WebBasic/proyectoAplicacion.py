# Importación de librerías
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Cargar el conjunto de datos Iris
data = sns.load_dataset('iris')
print("Primeras filas del dataset:")
print(data.head())

# Selección de variables predictoras y variable objetivo
X = data[['sepal_length', 'sepal_width', 'petal_width']]  # Features
y = data['petal_length']  # Target

# División de los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Tamaño de entrenamiento: {X_train.shape}")
print(f"Tamaño de prueba: {X_test.shape}")

# Creación y entrenamiento del modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Coeficientes del modelo
print("\nCoeficientes del modelo:")
print(f"Coeficientes: {model.coef_}")
print(f"Intersección (intercepto): {model.intercept_}")

# Predicción
y_pred = model.predict(X_test)

# Evaluación del modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nError Cuadrático Medio (MSE): {mse}")
print(f"Coeficiente de determinación (R²): {r2}")

# Visualización: Valores reales vs. predicciones
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicciones')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
         color='red', linewidth=2, label='Línea ideal')
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Regresión Lineal - Predicción de petal_length")
plt.legend()
plt.grid(True)
plt.show()
