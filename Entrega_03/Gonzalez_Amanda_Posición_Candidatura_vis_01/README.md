# Posición en la lista de las candidaturas electas a CORE en 2024

## Descripción del proyecto

Esta visualización muestra qué posición ocupaban en sus respectivas listas las candidaturas que resultaron electas como consejeros regionales (CORE) en Chile en 2024. Mediante un gráfico de barras horizontales apiladas al 100 %, elaborado con Altair, se compara por región el porcentaje de candidaturas electas que estaban en la primera posición y el porcentaje que ocupaba posiciones posteriores.

El gráfico acompaña una crónica periodística sobre la relación entre el orden de las candidaturas y los resultados electorales. Permite observar diferencias regionales, pero no demuestra que la posición en la lista determine la elección.

## Proceso de visualización

La visualización fue desarrollada en Google Colab con Python, pandas y Altair, utilizando la base de datos limpia trabajada en la entrega anterior.

## Pasos realizados

1. Se cargó el archivo `datos_electorales_database_limpia.csv` con pandas.
2. Se revisaron las columnas y se seleccionaron las variables relacionadas con región, posición en la lista y condición de electo.
3. Se trabajó con las candidaturas que resultaron electas.
4. Se distinguió entre candidaturas en **primera posición** y candidaturas en **otras posiciones**.
5. Se agruparon los datos por región y categoría, y se contó la cantidad de personas electas en cada grupo.
6. Se calculó qué porcentaje representaba cada categoría respecto del total de candidaturas electas de su región.
7. Se creó un gráfico de barras horizontales apiladas al 100 % con Altair y se ordenaron las regiones de norte a sur.
8. Se incorporaron etiquetas de los ejes, colores para las dos categorías y una ventana interactiva (*tooltip*) con cantidades y porcentajes.
9. Se exportó el gráfico en HTML y como imagen para su presentación junto a la crónica.

## Decisiones tomadas

Se eligió un gráfico de barras horizontales apiladas al 100 % porque:

- Permite comparar la proporción de candidaturas electas en primera posición y en otras posiciones dentro de cada región.
- Facilita la lectura de los nombres de las regiones.
- Presenta las 16 regiones en orden geográfico, de norte a sur.
- La versión HTML permite consultar las cifras específicas al pasar el cursor por las barras.

Se utilizaron dos colores para distinguir ambas categorías. Como las barras representan porcentajes, cada región suma 100 %, aunque el número de personas electas sea distinto entre regiones.

## Base de datos utilizada

Se utilizó el archivo `datos_electorales_database_limpia.csv`, preparado en la Entrega 02, con información de las candidaturas a consejeros regionales en las elecciones de Chile de 2024.

La base de trabajo contiene 2.515 candidaturas, de las cuales 302 figuran como electas. Para esta visualización se consideraron las 302 candidaturas electas.

## Procesamiento de la base de datos

Para preparar los datos del gráfico:

- Se identificaron las candidaturas electas.
- Se clasificó su ubicación en la lista en dos grupos: primera posición y otras posiciones.
- Se contaron las candidaturas electas de cada grupo por región.
- Se calcularon los porcentajes sobre el total de personas electas de cada región.

En el conjunto analizado, 204 candidaturas electas estaban en primera posición y 98 ocupaban posiciones posteriores. El 67,5 % de las candidaturas electas encabezaba su lista.

## Correcciones y verificación de la base de datos

Se utilizó la base limpia de la entrega anterior y se revisó la consistencia de los totales empleados en la visualización. Se comprobó que las dos categorías sumaran el total de candidaturas electas y que los porcentajes por región completaran el 100 %.

No se realizaron nuevas correcciones a registros individuales para esta visualización.

## Preguntas que puede responder la visualización

- ¿Qué proporción de las candidaturas electas encabezaba su lista en cada región?
- ¿En qué regiones hubo una mayor presencia de personas electas desde posiciones posteriores?
- ¿Cómo cambia la composición de las candidaturas electas entre las regiones del país?

El gráfico no permite concluir que aparecer primero cause una mayor probabilidad de resultar electo. Para estudiar esa relación también sería necesario comparar todas las candidaturas, electas y no electas, y considerar otros factores de la competencia electoral.
