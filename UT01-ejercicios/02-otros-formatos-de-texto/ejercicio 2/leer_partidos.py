import json

# Cargar datos del fichero JSON
with open('partidos.json', 'r', encoding='utf-8') as f:
    partidos = json.load(f)

# Mostrar los resultados
for partido in partidos:
    print(f"Nombre del Partido: {partido['Nombre del Partido']}")
    print(f"Equipo Local: {partido['Equipo Local']}")
    print(f"Equipo Visitante: {partido['Equipo Visitante']}")
    print(f"Fecha: {partido['Fecha']}")
    print(f"Resultado: {partido['Resultado']}")
    print("---------------------------")