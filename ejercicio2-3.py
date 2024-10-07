import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
ruta_archivo = 'movies_data.csv'
df = pd.read_csv(ruta_archivo, encoding='ISO-8859-1')

# Calcular media, mediana y moda para Earnings, Budget y Box Office
media_earnings = df['Earnings'].mean()
mediana_earnings = df['Earnings'].median()
moda_earnings = df['Earnings'].mode()[0]

media_budget = df['Budget'].mean()
mediana_budget = df['Budget'].median()
moda_budget = df['Budget'].mode()[0]

media_box_office = df['Box Office'].mean()
mediana_box_office = df['Box Office'].median()
moda_box_office = df['Box Office'].mode()[0]

# Imprimir los resultados
print(f"Earnings - Media: {media_earnings}, Mediana: {mediana_earnings}, Moda: {moda_earnings}")
print(f"Budget - Media: {media_budget}, Mediana: {mediana_budget}, Moda: {moda_budget}")
print(f"Box Office - Media: {media_box_office}, Mediana: {mediana_box_office}, Moda: {moda_box_office}")

# Graficar el diagrama de cajas para Earnings
plt.figure(figsize=(12, 4))
sns.boxplot(data=df['Earnings'])
plt.title('Diagrama de Cajas para Earnings')
plt.ylabel('Earnings (in billions)')
plt.grid()
plt.show()

# Graficar el diagrama de cajas para Budget
plt.figure(figsize=(12, 4))
sns.boxplot(data=df['Budget'])
plt.title('Diagrama de Cajas para Budget')
plt.ylabel('Budget (in millions)')
plt.grid()
plt.show()

# Graficar el diagrama de cajas para Box Office
plt.figure(figsize=(12, 4))
sns.boxplot(data=df['Box Office'])
plt.title('Diagrama de Cajas para Box Office')
plt.ylabel('Box Office (in billions)')
plt.grid()
plt.show()
