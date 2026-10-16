# Ficha Técnica — gasto_vs_resultado_electoral.csv

## Características de los datos

Esta base combina dos bases ya limpias de la Entrega 02: la de gasto de campaña (fuente: SERVEL, "Reporte de Ingresos y Gastos Definitivas 2024") y la de resultados electorales (fuente: Sistema Integrado de Información Territorial de la Biblioteca del Congreso Nacional y Boletín Final de Consejeros Regionales de SERVEL). Cubre el universo completo de candidaturas a Consejero Regional (CORE) en la elección 2024: 2.515 candidatos, sin nulos ni duplicados. El cruce entre ambas bases, usando `id_candidato`, calzó al 100%.

## Variables incorporadas

| Variable | Descripción |
|---|---|
| `id_candidato` | Identificador único del candidato (nombre normalizado + circunscripción), usado para cruzar bases. |
| `nombre_candidato` | Nombre completo del candidato, tal como aparece en la papeleta. |
| `region` | Región donde compitió el candidato. |
| `circunscripcion` | Circunscripción provincial donde compitió. |
| `pacto` | Pacto electoral al que perteneció la candidatura. |
| `partido` | Partido político del candidato. |
| `gasto_total_declarado` | Monto total de gasto de campaña declarado ante SERVEL, en pesos chilenos. |
| `declara_gasto` | Indica si el candidato declaró algún gasto ("Sí"/"No"); los que no declararon quedan con `gasto_total_declarado = 0`. |
| `outlier_gasto_iqr` | Indica si el gasto del candidato es un valor atípico, según el método del rango intercuartílico (IQR) aplicado en la Entrega 02. |
| `posicion_lista` | Número de orden del candidato dentro de su lista (1 = primer lugar de la lista). |
| `primero_lista` | Indica si el candidato fue el primero de su lista ("Sí"/"No"). |
| `tamano_lista` | Cantidad total de candidatos que integraron esa misma lista. |
| `votos` | Votos obtenidos por el candidato. |
| `porcentaje_votos_lista` | Porcentaje de votos que el candidato obtuvo, calculado sobre el total de votos de su propia lista. |
| `electo` | Indica si el candidato resultó electo Consejero Regional ("Sí"/"No"). |

## Observaciones

- De las 15 columnas, 9 vienen de la base de gasto y 6 de la base de resultados; se dejaron fuera las columnas que no aportaban a esta visualización en particular (por ejemplo, `subpacto`, `sigla_partido`, `num_transacciones_gasto`, `estado_cuenta_auditoria`, `numero_papeleta`, `letra_lista`, `numero_listas_circunscripcion` y `votos_lista`), que sí están documentadas en las fichas técnicas originales de cada base en la Entrega 02.
- `gasto_total_declarado = 0` no es un dato faltante: corresponde a 185 candidatos (7,4% del total) que efectivamente no declararon gasto ante SERVEL. Se mantuvieron en la base en vez de eliminarlos, porque sacarlos habría dejado fuera justamente a los casos más baratos, sesgando cualquier análisis hacia quienes sí gastaron.
- 163 candidatos (6,5%) están marcados como outlier de gasto (gasto sobre $14.734.090). No se eliminaron de la base: siguen apareciendo en el gráfico, porque son casos reales y relevantes para la pregunta de investigación, no errores de digitación.
