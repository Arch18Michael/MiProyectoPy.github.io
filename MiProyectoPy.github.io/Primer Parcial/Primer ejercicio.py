# Primer ejercicio 
personas = ["Pedro", "Carla", "Laura", "José", "Marta"]

calorias_pedro = (2000, 1800, 2100, 2000, 1900, 2500, 2200)
calorias_carla = (1500, 1600, 1700, 1550, 1500, 1800, 1900)
calorias_laura = (2500, 2600, 2400, 2300, 2400, 2500, 2600)
calorias_jose = (1800, 1900, 2000, 2100, 2000, 1900, 1800)
calorias_marta = (1300, 1400, 1350, 1250, 1200, 1500, 1600)


historial_calorias = {
    "Pedro": calorias_pedro,
    "Carla": calorias_carla,
    "Laura": calorias_laura,
    "José": calorias_jose,
    "Marta": calorias_marta
}


for persona, calorias in historial_calorias.items():
    promedio_semanal = sum(calorias) / len(calorias)
    
    if promedio_semanal > 2000:
        print(f"{persona} tiene consumo alto")
    else:
        print(f"{persona} tiene consumo dentro del rango recomendado")