import numpy as np

#creacion de arrays
print("--- EJERCICIO 1 ---")
# 1a. Array 1D de longitud 8 (enteros de 10 a 50)
arr_1a = np.random.randint(10, 51, size=8)
print("1a:", arr_1a)

# 1b. Matriz 4x4 de valores True
arr_1b = np.full((4, 4), True)
print("1b:\n", arr_1b)

# 1c. Matriz 3D (3x2x5) de decimales (0 a 1)
arr_1c = np.random.rand(3, 2, 5)
print("1c:\n", arr_1c)

print("\n--- EJERCICIO 2 ---")
# 2a. Enteros del 1 al 20
arr_2a = np.arange(1, 21)
print("2a:", arr_2a)

# 2b. Matriz identidad 5x5
arr_2b = np.eye(5)
print("2b:\n", arr_2b)

# 2c. Matriz 4x6 de ceros
arr_2c = np.zeros((4, 6))
print("2c:\n", arr_2c)


#acceso y modificacion de elementos
print("\n--- EJERCICIO 3 ---")
# 3a. Cuarto elemento de 1a
cuarto_elemento = arr_1a[3]
print("3a (Cuarto elemento de 1a):", cuarto_elemento)

# 3b. Cambiar fila 3, columna 2 por False
arr_1b[2, 1] = False
print("3b (1b modificado):\n", arr_1b)

# 3c. Promedio de la segunda capa de 1c
promedio_segunda_capa = arr_1c[1].mean()
print("3c (Promedio segunda capa de 1c):", promedio_segunda_capa)

print("\n--- EJERCICIO 4 ---")
# 4a. Última fila de 2b
ultima_fila_id = arr_2b[-1]
print("4a (Última fila de 2b):", ultima_fila_id)

# 4b. Elemento central de 2b
elemento_central = arr_2b[2, 2]
print("4b (Elemento central de 2b):", elemento_central)

# 4c. Contar cuántos True quedan en 1b
cantidad_trues = np.sum(arr_1b)
print("4c (Cantidad de True en 1b):", cantidad_trues)


#operaciones matematicas

print("\n--- EJERCICIO 5 ---")
# 5a. Operaciones elemento a elemento (vectores de longitud 10)
arr_a = np.random.randint(1, 10, size=10)
arr_b = np.random.randint(1, 10, size=10)
print("Suma elemento a elemento:", arr_a + arr_b)
print("Resta elemento a elemento:", arr_a - arr_b)
print("Multiplicación elemento a elemento:", arr_a * arr_b)

# 5b. Suma y resta de matrices 3x3
matriz_A = np.random.randint(1, 10, size=(3, 3))
matriz_B = np.random.randint(1, 10, size=(3, 3))
print("Suma matricial:\n", matriz_A + matriz_B)
print("Resta matricial:\n", matriz_A - matriz_B)

# 5c. Multiplicación matricial
producto_matricial = np.matmul(matriz_A, matriz_B)
print("Multiplicación matricial:\n", producto_matricial)

print("\n--- EJERCICIO 6 ---")
# 6a. Producto punto de dos vectores de longitud 5
vec_1 = np.random.randint(1, 10, size=5)
vec_2 = np.random.randint(1, 10, size=5)
producto_punto = np.dot(vec_1, vec_2)
print("6a (Producto punto de vectores):", producto_punto)

# 6b. Transpuesta de matriz 4x3
matriz_4x3 = np.random.randint(1, 10, size=(4, 3))
transpuesta = matriz_4x3.T
print("6b (Matriz original 4x3):\n", matriz_4x3)
print("6b (Transpuesta 3x4):\n", transpuesta)

# 6c. Determinante de matriz 3x3
matriz_det = np.random.randint(1, 5, size=(3, 3))
determinante = np.linalg.det(matriz_det)
print("6c (Matriz 3x3):\n", matriz_det)
print("6c (Determinante):", determinante)


#funciones y metodos numpy
print("\n--- EJERCICIO 7 ---")
# 7a. Estadísticas de 20 enteros
arr_est = np.random.randint(1, 100, size=20)
print("7a (Array):", arr_est)
print("Valor máximo:", arr_est.max())
print("Valor mínimo:", arr_est.min())
print("Promedio:", arr_est.mean())
print("Mediana:", np.median(arr_est))

# 7b. Suma por filas y columnas (matriz 5x5)
matriz_5x5 = np.random.randint(1, 10, size=(5, 5))
print("7b (Matriz 5x5):\n", matriz_5x5)
print("Suma de cada fila:", matriz_5x5.sum(axis=1))
print("Suma de cada columna:", matriz_5x5.sum(axis=0))

# 7c. Desviación estándar de la matriz
print("7c (Desviación estándar):", matriz_5x5.std())

print("\n--- EJERCICIO 8 ---")
# 8a. 15 valores entre 5 y 50 con linspace
secuencia_lin = np.linspace(5, 50, 15)
print("8a (Linspace):", secuencia_lin)

# 8b. Múltiplos de 3 entre 0 y 60 con arange
secuencia_ar = np.arange(0, 61, 3)
print("8b (Arange múltiplos de 3):", secuencia_ar)

#numpy aplicado

print("\n--- EJERCICIO 9 (Calificaciones) ---")
# 9a. Matriz 5 alumnos x 4 materias (notas de 60 a 100)
calificaciones = np.random.randint(60, 101, size=(5, 4))
print("Matriz de calificaciones (Estudiantes x Asignaturas):\n", calificaciones)

# 9b. Promedio por estudiante
promedio_estudiantes = calificaciones.mean(axis=1)
print("Promedio de cada estudiante:", promedio_estudiantes)

# 9c. Estudiante con mayor promedio
mejor_estudiante = np.argmax(promedio_estudiantes) + 1
print(f"El estudiante con mayor promedio es el Estudiante {mejor_estudiante}")

# 9d. Asignatura con mejor promedio
mejor_asignatura = np.argmax(calificaciones.mean(axis=0)) + 1
print(f"La asignatura con mejor promedio es la Asignatura {mejor_asignatura}")

print("\n--- EJERCICIO 10 (Ventas) ---")
# 10a. Matriz 4 sucursales x 12 meses (ventas de 1000 a 10000)
ventas = np.random.randint(1000, 10001, size=(4, 12))
print("Matriz de ventas (Sucursales x Meses):\n", ventas)

# 10b. Ventas totales por sucursal
ventas_sucursales = ventas.sum(axis=1)
print("Ventas totales por sucursal:", ventas_sucursales)

# 10c. Sucursal con mayores ventas
mejor_sucursal = np.argmax(ventas_sucursales) + 1
print(f"La sucursal con mayores ventas anuales es la Sucursal {mejor_sucursal}")

# 10d. Promedio mensual de toda la empresa
promedio_mensual_empresa = ventas.mean()
print("Promedio mensual de ventas de toda la empresa:", promedio_mensual_empresa)

# 10e. Top 3 meses con mayores ventas globales
ventas_mensuales_globales = ventas.sum(axis=0)
top_3_meses = np.argsort(ventas_mensuales_globales)[::-1][:3] + 1
print("Los tres meses con mayores ventas globales son los meses:", top_3_meses)