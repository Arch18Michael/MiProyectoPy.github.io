import pandas as pd

#Ejercicio 1
datos = {
    'Nombre': ['Ana', 'Luis', 'Marta', 'Pedro'],
    'Edad': [23, 30, 25, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
    'Puntaje': [85, 90, 78, 92]
}
df = pd.DataFrame(datos)
print(df)
#Ejercicio 2
df_filtrado = df[df['Edad'] > 25]
print(df_filtrado)
#Ejercicio 3
edad_media = df['Edad'].mean()
print(f'La edad media es: {edad_media}')
edad_maxima = df['Edad'].max()
print(f'La edad máxima es: {edad_maxima}')
edad_minima = df['Edad'].min()
print(f'La edad mínima es: {edad_minima}')
puntaje_medio = df['Puntaje'].mean()
print(f'El puntaje medio es: {puntaje_medio}')
#Ejercicio 4
df['Aprobado'] = df['Puntaje'].apply(lambda x: 'Sí' if x >= 80 else 'No')
print(df)