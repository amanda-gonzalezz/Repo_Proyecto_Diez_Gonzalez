import pandas as pd
import json
import os

# 1. Universo completo (2515 candidatos, de Amanda)
# Se busca primero en la carpeta compartida del repositorio del equipo; si no
# está disponible, se usa la copia de respaldo guardada en datos_originales/.
RUTA_COMPARTIDA = '../../../Gonzalez_Amanda_01_datos_electorales_database_01/datos_electorales_database_limpia.csv'
RUTA_RESPALDO = '../../datos_originales/datos_electorales_database_limpia.csv'
RUTA_UNIVERSO = RUTA_COMPARTIDA if os.path.exists(RUTA_COMPARTIDA) else RUTA_RESPALDO
print(f"Usando universo de candidatos desde: {RUTA_UNIVERSO}")

df_universo = pd.read_csv(RUTA_UNIVERSO)
df_universo = df_universo[['id_candidato', 'nombre_candidato', 'sexo', 'region',
                            'circunscripcion', 'pacto', 'subpacto', 'sigla_partido', 'partido']].copy()

# 2. Gasto agregado + aplicar correcciones de los 10 casos huérfanos
df_gasto = pd.read_csv('./gasto_agregado_por_candidato.csv')
with open('./correcciones_id.json') as f:
    correcciones = json.load(f)
df_gasto['id_candidato'] = df_gasto['id_candidato'].apply(lambda x: correcciones.get(x, x))
# ya no necesitamos nombre/region/circunscripcion del archivo de gasto (usamos los de Amanda, ya validados)
df_gasto = df_gasto[['id_candidato', 'gasto_total_declarado', 'num_transacciones_gasto']]

# 3. Auditoria
df_aud = pd.read_csv('./auditoria_core.csv')
df_aud = df_aud.drop_duplicates(subset='id_candidato', keep='first')

# 4. Unir todo, con el universo como base (LEFT JOIN, para no perder a nadie)
df_final = df_universo.merge(df_gasto, on='id_candidato', how='left')
df_final = df_final.merge(df_aud, on='id_candidato', how='left')

# 5. Rellenar candidatos sin gasto declarado
df_final['gasto_total_declarado'] = df_final['gasto_total_declarado'].fillna(0).astype(int)
df_final['num_transacciones_gasto'] = df_final['num_transacciones_gasto'].fillna(0).astype(int)
df_final['declara_gasto'] = df_final['gasto_total_declarado'].apply(lambda x: 'Sí' if x > 0 else 'No')
df_final['estado_cuenta_auditoria'] = df_final['estado_cuenta_auditoria'].fillna('Sin información')

# 6. Chequeos de calidad
print("Filas totales:", len(df_final))
print("Nulos por columna:")
print(df_final.isnull().sum())
print()
print("Duplicados de id_candidato:", df_final['id_candidato'].duplicated().sum())
print()
print("Distribución declara_gasto:")
print(df_final['declara_gasto'].value_counts())
print()
print("Estadísticas de gasto_total_declarado:")
print(df_final['gasto_total_declarado'].describe())

# Rellenar el único vacío legítimo de la base: subpacto no siempre existe
df_final['subpacto'] = df_final['subpacto'].fillna('No aplica')

df_final.to_csv('../../base_gasto_core_2024_limpia.csv', index=False, encoding='utf-8')
print()
print("Guardado en base_gasto_core_2024_limpia.csv")
