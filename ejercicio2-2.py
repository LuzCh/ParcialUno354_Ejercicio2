import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
ruta_archivo = 'movies_data.csv'
df = pd.read_csv(ruta_archivo, encoding='ISO-8859-1')

# Crear un gráfico de dispersión
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Budget', y='Earnings', hue='Genre', alpha=0.7)
plt.title('Budget vs Earnings by Genre')
plt.xlabel('Budget (in millions)')
plt.ylabel('Earnings (in billions)')
plt.legend(title='Genre', bbox_to_anchor=(1, 1), loc='upper left')
plt.grid()
plt.show()
