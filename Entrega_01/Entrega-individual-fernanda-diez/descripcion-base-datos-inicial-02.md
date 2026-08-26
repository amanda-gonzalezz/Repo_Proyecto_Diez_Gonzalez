# Base de datos 2 — Gasto de campaña declarado, elección de Consejeros Regionales (CORE)

## Autor y publicación de los datos

Los datos son producidos y publicados oficialmente por el **Servicio Electoral de Chile (SERVEL)**, a través de su **Plataforma de Transparencia Electoral**, que recoge las declaraciones de aportes y gastos de campaña que cada candidato está obligado a presentar por la Ley N° 19.884 sobre Transparencia, Límite y Control del Gasto Electoral. Se obtiene desde: https://www.servel.cl

## Contenido

La base contendrá el detalle del gasto de campaña declarado por cada uno de los candidatos incluidos en la Base de datos 1 (resultados electorales), para la misma elección de Consejeros Regionales.

**Variables (columnas):**

| Columna | Descripción |
|---|---|
| `id_candidato` | Identificador único (mismo formato que en la Base de datos 1, para permitir el cruce) |
| `nombre_candidato` | Nombre completo del candidato |
| `region` | Región de la candidatura |
| `circunscripcion_provincial` | Circunscripción provincial |
| `gasto_total_declarado` | Monto total de gasto de campaña declarado (en pesos chilenos) |
| `aporte_propio` | Monto del gasto financiado con recursos propios del candidato |
| `aporte_partido` | Monto del gasto financiado por su partido/lista |
| `aporte_terceros` | Monto del gasto financiado por aportes de terceros |
| `limite_gasto_permitido` | Límite legal de gasto para ese cargo/circunscripción, según fórmula de SERVEL |
| `porcentaje_limite_usado` | % del límite legal que efectivamente gastó (calculada) |

La columna `porcentaje_limite_usado` es calculada; no viene directamente del archivo de SERVEL.

**Período:** misma elección de Consejeros Regionales que la Base de datos 1, para asegurar comparabilidad.

## Pertinencia

Esta base permite responder la segunda mitad de la pregunta de investigación: si el gasto de campaña predice el resultado electoral tanto o más que la posición en la papeleta. Al cruzarla con la Base de datos 1 mediante el identificador del candidato, se puede establecer si ambos factores actúan de forma independiente, se refuerzan mutuamente (candidatos bien posicionados que además reciben más financiamiento de su partido), o si uno compensa al otro.

## Metodología de obtención

1. Ingresar a la Plataforma de Transparencia Electoral de SERVEL y ubicar la sección de declaraciones de gasto para la elección de Consejeros Regionales seleccionada.
2. Descargar las declaraciones disponibles por candidato o por circunscripción, según el formato en que la plataforma las entregue (individual por candidato o consolidado).
3. Consolidar la información en una tabla maestra con una fila por candidato, usando como identificador el mismo nombre/formato que en la Base de datos 1.
4. Verificar que cada candidato de la Base de datos 1 tenga su registro correspondiente en esta base (y documentar los casos sin declaración de gasto encontrada, si los hay, como limitación).
5. Calcular `porcentaje_limite_usado` a partir del gasto declarado y el límite legal correspondiente.
6. Unir ambas bases (Base de datos 1 + Base de datos 2) mediante `id_candidato` para generar la tabla final de análisis.

No se requiere web scraping: las declaraciones son de descarga directa desde la plataforma oficial. Como limitación metodológica, se documentará que el gasto declarado depende del reporte voluntario del candidato ante SERVEL, por lo que podría no reflejar el 100% del gasto real de campaña.