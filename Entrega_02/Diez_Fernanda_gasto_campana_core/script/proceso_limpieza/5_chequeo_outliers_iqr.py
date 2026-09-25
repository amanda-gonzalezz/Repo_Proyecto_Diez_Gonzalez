import pandas as pd

df = pd.read_csv('../../base_gasto_core_2024_limpia.csv')

# Método IQR visto en clase (datos_y_pandas.md) para detectar outliers
q1 = df['gasto_total_declarado'].quantile(0.25)
q3 = df['gasto_total_declarado'].quantile(0.75)
iqr = q3 - q1
limite_superior = q3 + 1.5 * iqr

df['outlier_gasto_iqr'] = df['gasto_total_declarado'].apply(
    lambda x: 'Sí' if (x > limite_superior) else 'No'
)

print(f"Límite superior (Q3 + 1.5*IQR): {limite_superior:,.0f}")
print(df['outlier_gasto_iqr'].value_counts())

# Decisión: NO eliminamos estos casos. A diferencia de un dato erróneo,
# corresponden a candidatos reales con alto gasto de campaña, información
# relevante para responder la pregunta de investigación "¿quién gastó más?".
# Se dejan marcados para decidir su inclusión en la etapa de análisis.

df.to_csv('../../base_gasto_core_2024_limpia.csv', index=False, encoding='utf-8')
