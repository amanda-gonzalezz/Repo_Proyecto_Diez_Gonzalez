## Ficha técnica de la base de datos

### Características generales

- **Tipo de datos:** resultados de candidaturas a consejeros regionales (CORE), elecciones de Chile de 2024.
- **Unidad de análisis de la base original:** candidatura a consejero regional.
- **Unidad de análisis de la visualización:** grupo de candidaturas electas por región y posición en la lista.
- **Cobertura territorial:** las 16 regiones de Chile.
- **Categorías consideradas:** primera posición y otras posiciones dentro de la lista.
- **Formato de la base utilizada:** CSV.
- **Total de candidaturas en la base:** 2.515.
- **Total de candidaturas electas:** 302.
- **Electas en primera posición:** 204.
- **Electas en otras posiciones:** 98.

### Variables incorporadas

| Variable | Descripción |
|---|---|
| region | Región correspondiente a la candidatura. |
| posicion_lista | Posición de la candidatura dentro de su lista. |
| primero_lista | Identifica si la candidatura ocupaba la primera posición. |
| electo | Indica si la candidatura resultó electa. |
| categoria | Agrupación utilizada en el gráfico: primera posición u otras posiciones. |
| cantidad | Número de candidaturas electas por región y categoría. |
| total | Total de candidaturas electas de la región. |
| porcentaje | Porcentaje que representa cada categoría sobre el total de candidaturas electas de la región. |

### Observaciones sobre la base de datos

- La base original contiene candidaturas electas y no electas. El gráfico considera únicamente las electas.
- Las barras están normalizadas al 100 % para comparar proporciones entre regiones, independientemente del número de consejeros regionales electos en cada una.
- Cada candidatura electa se contabiliza una sola vez, en la región correspondiente y en una de las dos categorías de posición.
- La versión HTML permite consultar la cantidad y el porcentaje mediante información interactiva; el JPG presenta una versión estática.
- Los resultados describen la posición de quienes fueron electos. No representan la probabilidad de resultar electo según la posición en la lista ni permiten establecer causalidad.

De las 302 candidaturas electas, 204 estaban en primera posición (67,5 %) y 98 en posiciones posteriores (32,5 %). Estas cifras corresponden al conjunto nacional. La visualización presenta el desglose porcentual de cada región.
