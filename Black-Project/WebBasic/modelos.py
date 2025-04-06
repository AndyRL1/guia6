# Paso 2: Importar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Paso 2.1: Cargar el conjunto de datos Iris desde seaborn
data = sns.load_dataset('iris')

# Mostrar las primeras filas del dataset
print("Primeras filas del dataset:")
print(data.head())

# Paso 3: Preparar los datos
# Seleccionar las variables predictoras y la variable objetivo
X = data[['sepal_length', 'sepal_width', 'petal_width']]  # Variables predictoras
y = data['petal_length']  # Variable a predecir

# Dividir el conjunto de datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nTamaño del conjunto de entrenamiento:", X_train.shape)
print("Tamaño del conjunto de prueba:", X_test.shape)

# Paso 4: Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Mostrar los coeficientes e intersección del modelo
print("\nCoeficientes del modelo:", model.coef_)
print("Intersección (intercepto):", model.intercept_)

# Paso 5: Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)
predictions_df = pd.DataFrame({'Valores Reales': y_test, 'Predicción': y_pred})
print("\nComparación de valores reales vs. predicción:")
print(predictions_df.head())

# Paso 6: Evaluar el modelo utilizando el Error Cuadrático Medio (MSE) y R²
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nError cuadrático medio (MSE): {mse}")
print(f"Coeficiente de determinación (R²): {r2}")

# Paso 7: Visualización de resultados
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicciones')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, label="Línea de referencia")
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Comparación: Valores reales vs. Predicciones")
plt.legend()
plt.show()
