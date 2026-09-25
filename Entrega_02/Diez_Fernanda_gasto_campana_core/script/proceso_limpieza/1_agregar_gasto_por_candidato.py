import openpyxl
import pandas as pd
import unicodedata
import re

def normalizar(texto):
    """Mayúsculas, sin tildes, espacios -> guión bajo, sin caracteres raros."""
    if texto is None:
        return ""
    texto = str(texto).strip().upper()
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    texto = re.sub(r'\s+', '_', texto)
    texto = re.sub(r'[^A-Z0-9_]', '', texto)
    return texto

def construir_id(nombre, circunscripcion):
    return f"{normalizar(nombre)}__{normalizar(circunscripcion)}"

RUTA = '../../datos_originales/Reporte_Ingresos_Gastos_Definitivas2024_SERVEL_original.xlsx'

print("Cargando hoja INGRESOS Y GASTOS (esto puede tardar unos segundos)...")
wb = openpyxl.load_workbook(RUTA, read_only=True, data_only=True)
ws = wb['INGRESOS Y GASTOS']

# Columnas (0-indexed) según encabezado real:
# 0 TIPO CUENTA(candidato/partido) | 1 TIPO(INGRESOS/GASTO) | 2 ELECCIÓN | 3 REGIÓN
# 4 TERRITORIO ELECTORAL | 5 NOMBRE DE CANDIDATURA/PARTIDO | 6 NOMBRE PARTIDO
# 7 PACTO | 8 SUBPACTO | ... 13 MONTO

registros = {}  # id_candidato -> dict acumulador
n_filas_gasto_core = 0

for row in ws.iter_rows(min_row=12, values_only=True):
    tipo_cuenta, tipo, eleccion, region, territorio, nombre_cand = row[0], row[1], row[2], row[3], row[4], row[5]
    monto = row[13]
    if eleccion != 'CONSEJERO REGIONAL':
        continue
    if tipo_cuenta != 'Candidato':
        continue  # descartamos gasto reportado a nivel de partido, no de candidato individual
    if tipo != 'GASTO':
        continue
    if not nombre_cand or not territorio:
        continue

    n_filas_gasto_core += 1
    idc = construir_id(nombre_cand, territorio)
    if idc not in registros:
        registros[idc] = {
            'id_candidato': idc,
            'nombre_candidato_gasto': str(nombre_cand).strip(),
            'region_gasto': region,
            'circunscripcion_gasto': territorio,
            'gasto_total_declarado': 0,
            'num_transacciones_gasto': 0,
        }
    registros[idc]['gasto_total_declarado'] += (monto or 0)
    registros[idc]['num_transacciones_gasto'] += 1

print(f"Filas de GASTO a nivel de candidato en CORE procesadas: {n_filas_gasto_core}")
print(f"Candidatos distintos con gasto declarado: {len(registros)}")

df_gasto = pd.DataFrame(registros.values())
df_gasto.to_csv('./gasto_agregado_por_candidato.csv', index=False)
print(df_gasto.head())
