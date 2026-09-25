import openpyxl
import pandas as pd
import unicodedata, re

def normalizar(texto):
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
wb = openpyxl.load_workbook(RUTA, read_only=True, data_only=True)
ws = wb['Resultado Auditoria Cuentas']

registros = {}
for row in ws.iter_rows(min_row=2, values_only=True):
    eleccion, tipo_cta, region, territorio, nombre, estado = row
    if eleccion != 'CONSEJERO REGIONAL':
        continue
    idc = construir_id(nombre, territorio)
    registros[idc] = estado

df_aud = pd.DataFrame([{'id_candidato': k, 'estado_cuenta_auditoria': v} for k, v in registros.items()])
df_aud.to_csv('./auditoria_core.csv', index=False)
print(f"Registros de auditoría CORE: {len(df_aud)}")
print(df_aud['estado_cuenta_auditoria'].value_counts())
