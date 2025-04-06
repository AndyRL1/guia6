from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset
iris = load_iris()

# Convertir a DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["target"] = iris.target

# Mostrar las primeras filas
print(df.head())

# Estadísticas descriptivas
print("📌 Estadísticas:")
print(df.describe())

# Conteo por clase
print("📌 Cantidad por clase:")
print(df["target"].value_counts())

# Histograma de características
sns.histplot(data=df, x="sepal length (cm)", hue="target", multiple="stack")
plt.title("Histograma - Largo del sépalo")
plt.show()

# Matriz de correlación
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Matriz de correlación")
plt.show()

# Gráfico de pares
sns.pairplot(df, hue="target")
plt.show()

# Guardar estadísticas en Excel
df.describe().to_excel("estadisticas_iris.xlsx")

df.to_excel("iris_data.xlsx", index=False)
print("📁 Archivo 'iris_data.xlsx' guardado correctamente.")