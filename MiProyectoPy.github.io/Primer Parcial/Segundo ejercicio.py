# Segundo ejercicio
nombres_empleados = ["Juan", "Ana", "Luis", "Nadia", "Nico"]

horas_juan = (8, 8, 8, 8, 8, 0, 0)
horas_ana = (9, 9, 9, 9, 9, 4, 0)
horas_luis = (10, 10, 10, 10, 10, 8, 0)
horas_nadia = (7, 7, 7, 7, 7, 5, 0)
horas_nico = (5, 5, 5, 5, 5, 0, 0)

precio_hora = 375

print(" Paso 1: Recorrer la lista de empleados ")
for empleado in nombres_empleados:
    print(empleado)

print("\n Paso 2: Mostrar el diccionario creado ")
diccionario = {
    "Juan": horas_juan,
    "Ana": horas_ana,
    "Luis": horas_luis,
    "Nadia": horas_nadia,
    "Nico": horas_nico
}

for a, b in diccionario.items():
    print(f"{a}: {b}")

print("\nPasos 3 y 4: Calcular salarios y evaluar condiciones")
for empleado, horas in diccionario.items():
    salario_semanal = sum(horas) * precio_hora
    print(f"Empleado: {empleado} | Salario Semanal: ${salario_semanal}")
    
    if salario_semanal > 18000:
        print(f"{empleado} tiene un salario alto")
    else:
        print(f"{empleado} tiene un salario bajo")
    print("-" * 40) 