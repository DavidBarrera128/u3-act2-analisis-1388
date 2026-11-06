# importar librerias
import pandas as pd
import numpy as np
print("analisis de datos Clasificación Médica David Barrera NC = 1388")
pacientes = {
    "Nombre": ["Ana", "Luis", "Marta", "Roberto", "Carla", "Javier"],
    "Presion_Arterial": [120, 140, 135, 110, 150, 125],
    "Fumador": [False, True, False, False, True, True],
    "Nivel_Riesgo": ["Bajo", "Alto", "Medio", "Bajo", "Alto", "Medio"]
}
df = pd.DataFrame(pacientes)
print(df)
print("-+-+-+-+- Agrupar en una sola columna Nombre -+-+-+-+-")
grouped = df.groupby('Nombre')
print(grouped)
print("-+-+-+-+- por agregacion -+-+-+-+-")
# Nombre promedio por departamento
print(grouped['Presion_Arterial'].mean())

# Edad máxima en cada departamento
print(grouped['Fumador'].max())
print("-+-+-+-+- por  -+-+-+-+-")