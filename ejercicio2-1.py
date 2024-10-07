import csv 
import matplotlib.pyplot as plt 
 
 
def cargar_datos_csv(ruta_archivo, columna_index): 
    datos = [] 
    with open(ruta_archivo, newline='', encoding='ISO-8859-1') as archivo_csv: 
        lector_csv = csv.reader(archivo_csv) 
        next(lector_csv) 
        for fila in lector_csv: 
            datos.append(float(fila[columna_index])) 
    return datos 

 
 
def calcular_percentil(datos, percentil): 
    datos_ordenados = sorted(datos) 
    n = len(datos_ordenados) 
    k = (n - 1) * (percentil / 100) 
    f = int(k) 
    c = k - f 
 
    if f + 1 < n: 
        return datos_ordenados[f] + (c * (datos_ordenados[f + 1] - datos_ordenados[f])) 
    else: 
        return datos_ordenados[f] 
  
 
def calcular_cuartiles(datos): 
    q1 = calcular_percentil(datos, 25) 
    q2 = calcular_percentil(datos, 50) 
    q3 = calcular_percentil(datos, 75) 
    return q1, q2, q3 
 
# Función para graficar el histograma de una columna de datos 
 
 
def graficar_histograma(datos, nombre_columna): 
    plt.hist(datos, bins=10, edgecolor='black', alpha=0.7) 
    plt.title(f'Histograma de {nombre_columna}') 
    plt.xlabel('Valores') 
    plt.ylabel('Frecuencia') 
    plt.grid(True) 
    plt.show() 
 
 
# Cargar datos desde el archivo CSV 
ruta_archivo = 'movies_data.csv' 
cont=0
columnas = [2,7,8,9,10,11,12,13,14,15]
columnas_n = ["Running time","Budget","Box Office","Actors Box Office %","Director Box Office %","Earnings","Oscar and Golden Globes nominations","Oscar and Golden Globes awards","Release year","IMDb score"]
for i in columnas: 
    columna_index = i  
    datos = cargar_datos_csv(ruta_archivo, columna_index) 
 
    q1, q2, q3 = calcular_cuartiles(datos) 
    print(f"Cuartil 1 (Q1): {q1}") 
    print(f"Cuartil 2 (Q2) o mediana: {q2}") 
    print(f"Cuartil 3 (Q3): {q3}") 
 
 
    p90 = calcular_percentil(datos, 90) 
    print(f"Percentil 90: {p90}") 
 
    graficar_histograma(datos, columnas_n[cont])
    cont+=1