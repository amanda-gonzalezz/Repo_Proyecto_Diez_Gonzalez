# Base de datos 2 — Gasto de campaña declarado, elección de Consejeros Regionales (CORE)

**Responsable:** Fernanda Diez

## Autor y publicación de los datos

Los datos son producidos y publicados oficialmente por el **Servicio Electoral de Chile (SERVEL)**, que recoge las declaraciones de aportes y gastos de campaña que cada candidato está obligado a presentar por la Ley N° 19.884 sobre Transparencia, Límite y Control del Gasto Electoral. Se obtienen desde la sección "Ingresos y gastos electorales de los candidatos y candidatas": http://www-doc.servel.cl/?tipo=ingresosygastos

## Contenido

Ya descargamos el archivo de SERVEL con los ingresos y gastos electorales, pero viene **consolidado con todas las candidaturas de las Elecciones Municipales y Regionales 2024** (alcaldes, concejales, gobernadores regionales y consejeros regionales juntos en un mismo archivo). 

La base final contendrá el gasto de campaña total declarado por cada uno de los candidatos a CORE incluidos en la Base de datos 1 (resultados electorales), para la elección de 2024.

**Variables (columnas)**

| Columna | Descripción |
|---|---|
| `id_candidato` | Identificador para el cruce con la Base de datos 1. Lo construiremos "sumando" el nombre normalizado (mayúsculas, sin tildes, sin espacios extra) con la circunscripción provincial. No es un ID que entregue SERVEL, lo generamos nosotras igual en ambas bases para que el cruce no dependa de que los nombres estén escritos idéntico en las dos fuentes |
| `nombre_candidato` | Nombre completo del candidato, tal como aparece en el archivo original |
| `region` | Región de la candidatura |
| `circunscripcion_provincial` | Circunscripción provincial (unidad territorial más chica que la región, la que realmente define la papeleta, el número de competidores y los cupos de CORE) |
| `gasto_total_declarado` | Monto total de gasto de campaña declarado (en pesos chilenos) |
| `porcentaje_limite_gasto_permitido_usado` | % del límite legal de gasto que efectivamente usó el candidato (calculada) |

## Pertinencia

Esta base es la que nos permite controlar la hipótesis. El estudio de Morales y Becerra (2018) ya mostró que el efecto de la posición en la papeleta se mantiene incluso controlando por gasto de campaña, en el caso de concejales. Al cruzar esta base con la Base de datos 1 mediante el identificador del candidato, podemos comprobar si eso mismo ocurre en la elección CORE: si los candidatos bien posicionados igual tienen ventaja aunque comparemos a candidatos con gasto parecido, o si en realidad la posición y el gasto van tan de la mano que no se puede separar el efecto de uno del otro.

## Metodología de obtención

1. Descargar el archivo de ingresos y gastos electorales de las Elecciones Municipales y Regionales 2024 desde la sección "Ingresos y gastos electorales de los candidatos y candidatas" de servel.cl.
2. Filtrar el archivo para quedarnos solo con las filas correspondientes a candidatos a Consejero Regional, usando la columna de tipo de cargo del archivo original.
3. Normalizar los nombres (mayúsculas, sin tildes) y construir `id_candidato` concatenando nombre normalizado + circunscripción provincial.
4. Verificar que cada candidato de la Base de datos 1 tenga su registro correspondiente en esta base (cruzando por `id_candidato`), revisando manualmente una muestra de cruces para confirmar que calzaron bien, y anotar los casos sin declaración de gasto.
5. Calcular `porcentaje_limite_gasto_permitido_usado` a partir del gasto declarado y el límite legal correspondiente.
6. Unir ambas bases (Base de datos 1 + Base de datos 2) mediante `id_candidato` para generar la tabla final de análisis.

**Sobre el gasto total por candidato:** actualmente tenemos el gasto desglosado en muchos registros pequeños por candidato (cada pago o ítem declarado por separado), no un total ya sumado. Pedimos vía Solicitud de Transparencia que SERVEL nos entregue directamente el gasto total final por candidato, para no tener que sumarlo nosotras. Si esa solicitud no llega a tiempo, la alternativa es sumar manualmente todos los montos declarados por cada candidato en los Formularios Auxiliares 107 (Detalle de Reembolso Solicitado) y 108 (Detalle de Gastos Menores) para calcular nosotras el total por candidato a partir de esos registros individuales.

Como limitación metodológica se documentará que el gasto declarado depende del reporte de cada candidato ante SERVEL, por lo que podría no reflejar el 100% del gasto real de campaña. El estudio de Morales y Becerra reporta que, en su base de concejales, cerca de un cuarto de los candidatos no declaró gasto; es esperable encontrar algo similar acá.
