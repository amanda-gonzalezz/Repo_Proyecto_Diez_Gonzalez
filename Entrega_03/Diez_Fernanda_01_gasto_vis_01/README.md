# Diez_Fernanda_01_gasto_vis_01 — Documentación

## Qué muestra esta visualización

Un gráfico de dispersión que cruza el gasto de campaña declarado por cada candidato a Consejero Regional (CORE) 2024 con el porcentaje de votos que obtuvo dentro de su propia lista. Busca responder si gastar más en campaña se relaciona con un mejor resultado electoral. Se eligió este cruce (gasto vs. resultado) y no posición vs. resultado, porque Amanda ya trabajó la posición en la lista (qué posición ocupaban los candidatos electos, por región) en su propia visualización, y así las dos cubren ángulos distintos de la misma hipótesis en vez de repetirse.

## Cómo se hizo

1. **Punto de partida:** se usaron las dos bases ya limpias de la Entrega 02: `base_gasto_core_2024_limpia.csv` (gasto declarado, construida por Fernanda) y `datos_electorales_database_limpia.csv` (resultados electorales, construida por Amanda). Ambas tienen 2.515 candidaturas y comparten la columna `id_candidato`, que ya se armó en la entrega anterior para poder cruzarlas sin ambigüedad.
2. **Cruce de las bases:** se unieron ambas tablas con un *left join* sobre `id_candidato`, dejando como base la de gasto. El cruce calzó al 100% (las 2.515 filas encontraron su par), porque el `id_candidato` ya había sido normalizado y corregido en la Entrega 02.
3. **Selección de columnas:** de las dos bases originales (14 y 19 columnas) se dejaron solo las 15 columnas que esta visualización específica necesita: identificación del candidato, gasto, si declaró gasto, si es un outlier de gasto, posición en la lista, tamaño de la lista, votos, porcentaje de votos en la lista y si resultó electo. Esta base reducida es `gasto_vs_resultado_electoral.csv`, la que se usa en el gráfico.
4. **Nueva variable:** se creó `gasto_millones`, que es el gasto declarado dividido por un millón, solo para que el eje del gráfico sea más fácil de leer (en vez de números como 7.548.559, se ve 7,5).
5. **Construcción del gráfico:** con la librería Altair, en Python, se armó un gráfico de dispersión (cada punto es un candidato), coloreado según si la persona resultó electa o no, con una línea de tendencia (regresión lineal) encima para ver si existe una correlación. El detalle completo del código está en `scripts/codigo_para_visualizar_1.ipynb`.
6. **Exportación:** el gráfico se exportó en los dos formatos pedidos: `vis_01.html` (interactivo) y `vis_01.jpg` (imagen fija), ambos en la carpeta `visualizacion/`.

## Por qué esta base y no otra

Se eligió `gasto_vs_resultado_electoral.csv` porque es la única combinación de datos que permite responder directamente la pregunta de investigación sobre gasto y resultado, y porque reutiliza bases que ya fueron limpiadas y verificadas a fondo en la Entrega 02 (sin nulos, sin duplicados, sin montos negativos), por lo que no fue necesario volver a limpiar nada desde cero.

## Preguntas que esta visualización puede responder

1. ¿Los candidatos que declararon más gasto de campaña obtuvieron, en promedio, un mayor porcentaje de votos dentro de su lista?
2. ¿Qué tan fuerte es la relación entre gasto y resultado electoral: es determinante, o solo un factor entre varios?
3. ¿Cuánto gastaron en promedio los candidatos que sí resultaron electos, comparado con los que no?
4. ¿Hay candidatos que ganaron sin haber declarado gasto, o que gastaron mucho y aun así no resultaron electos?
