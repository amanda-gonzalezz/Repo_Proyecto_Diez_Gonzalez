import pandas as pd
import unicodedata, re, os

def normalizar(texto):
    if texto is None:
        return ""
    texto = str(texto).strip().upper()
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    texto = re.sub(r'\s+', '_', texto)
    texto = re.sub(r'[^A-Z0-9_]', '', texto)
    return texto

# La Base de datos 1 (resultados electorales) es de Amanda González, en su propia
# carpeta individual del repositorio del equipo. Se intenta leer desde ahí primero;
# si esa carpeta todavía no está disponible (por ejemplo, al evaluar esta entrega
# de forma individual antes de que ella suba la suya), se usa una copia de respaldo
# guardada en datos_originales/ de esta misma carpeta.
RUTA_COMPARTIDA = '../../../Gonzalez_Amanda_01_datos_electorales_database_01/datos_electorales_database_limpia.csv'
RUTA_RESPALDO = '../../datos_originales/datos_electorales_database_limpia.csv'
RUTA_UNIVERSO = RUTA_COMPARTIDA if os.path.exists(RUTA_COMPARTIDA) else RUTA_RESPALDO
print(f"Usando universo de candidatos desde: {RUTA_UNIVERSO}")

df_universo = pd.read_csv(RUTA_UNIVERSO)
df_gasto = pd.read_csv('./gasto_agregado_por_candidato.csv')

ids_universo = set(df_universo['id_candidato'])
huerfanos = df_gasto[~df_gasto['id_candidato'].isin(ids_universo)]

# Estrategia: comparar sin ningun underscore/espacio (nombre "aplastado") + circunscripcion
def aplastar(idc):
    nombre_parte, circ_parte = idc.rsplit('__', 1)
    return nombre_parte.replace('_',''), circ_parte

universo_aplastado = {}
for idc in ids_universo:
    n, c = aplastar(idc)
    universo_aplastado[(n, c)] = idc

correcciones = {}
for _, row in huerfanos.iterrows():
    n, c = aplastar(row['id_candidato'])
    match = universo_aplastado.get((n, c))
    if match:
        correcciones[row['id_candidato']] = match
    else:
        correcciones[row['id_candidato']] = None  # sigue sin resolverse

for k, v in correcciones.items():
    print(f"{k}  ->  {v}")

import json
with open('./correcciones_id.json', 'w') as f:
    json.dump(correcciones, f, ensure_ascii=False, indent=2)
