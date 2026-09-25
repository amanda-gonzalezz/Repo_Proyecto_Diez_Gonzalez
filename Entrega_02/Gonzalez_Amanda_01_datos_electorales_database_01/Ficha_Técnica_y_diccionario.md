## Ficha técnica y diccionario de datos

### Fuente de los datos

La base fue construida a partir de la integración de tres fuentes de datos sobre la elección de Consejeros Regionales (CORE) de Chile realizada en 2024.

La primera fuente corresponde a la base de candidaturas de las Elecciones Regionales y Municipales 2024 publicada por el Servicio Electoral de Chile (database_raw_01). De esta fuente se utilizaron los registros correspondientes a la elección de consejeros regionales y variables como nombre, sexo, región, territorio electoral, pacto, subpacto, partido, letra de lista y número de candidatura.

La segunda fuente corresponde al sistema Elecciones Históricas de la Biblioteca del Congreso Nacional de Chile (database_raw_02). Desde este sitio se descargaron los resultados de la elección de CORE 2024 para cada una de las 16 regiones del país. De estos archivos se obtuvo principalmente la cantidad de votos correspondiente a cada candidatura.

Finalmente, para identificar a las candidaturas electas se utilizó el listado publicado por Emol, “Cómo quedó conformado cada uno de los 16 consejos regionales del país”(database_raw_03), que se traspasó a un CSV presenta los consejeros regionales electos e identifica como fuente de la información al SERVEL. Esta fuente se usó para construir la variable de quienes fueron electos.

### Metodología de construcción de la base

La unidad de observación corresponde a una candidatura a consejero o consejera regional en las elecciones de 2024. Cada fila de la base representa una candidatura.

La información de las candidaturas proviene de los registros publicados por el Servicio Electoral de Chile (SERVEL), que contienen las candidaturas inscritas para la elección junto con datos como su territorio electoral, lista y número de papeleta.

Los resultados electorales provienen de los registros de la elección publicados por la Biblioteca del Congreso Nacional de Chile. Estos datos tienen su origen en el proceso de escrutinio de las mesas receptoras de sufragios, donde se contabilizan y registran los votos obtenidos por las candidaturas.

Como la información necesaria para el proyecto se encontraba distribuida en distintas fuentes y archivos, se construyó una base propia que reúne las candidaturas registradas por SERVEL con sus respectivos resultados electorales. La base final contiene 2.515 candidaturas de las 16 regiones del país.

Además de las variables provenientes de las fuentes originales, se construyeron variables necesarias para analizar la relación entre la posición de una candidatura dentro de su lista y su resultado electoral, entre ellas la posición dentro de la lista, el tamaño de la lista, los votos totales de la lista y el porcentaje de votos obtenido por cada candidatura dentro de ella.

Finalmente, se incorporó la condición de electo de cada candidatura a partir del listado de candidatos electos publicado por Emol obtenido de registros del SERVEL.

### Alcance de los datos

La base comprende las candidaturas que participaron en la elección de Consejeros Regionales (CORE) de Chile de 2024 en las 16 regiones del país. Su cobertura territorial considera las 66 circunscripciones provinciales utilizadas para esta elección.

La información reunida permite identificar a las candidaturas y conocer su sexo, región, circunscripción, lista, pacto, subpacto, partido, número de papeleta, cantidad de votos obtenidos y condición de electo. Además, la base incorpora variables construidas para estudiar la posición de cada candidatura dentro de su lista, el tamaño de esta, la cantidad de listas que compiten en cada circunscripción y la proporción de los votos de la lista obtenida por cada candidatura.

El alcance de la base se limita a la elección de Consejeros Regionales de 2024. No incluye las candidaturas ni los resultados correspondientes a las elecciones de gobernadores regionales, alcaldes o concejales realizadas durante el mismo proceso electoral.

### Unidad de observación

La unidad de observación corresponde a cada candidatura a Consejero Regional presentada en las elecciones de 2024.

Cada fila de la base representa una candidatura individual. Las distintas variables contenidas en las columnas describen características o resultados asociados a esa misma candidatura.

La base contiene un total de 2.515 observaciones.

### Características de los datos

La base final corresponde a un conjunto de datos estructurados en formato CSV. La información está organizada en filas y columnas, donde cada fila representa una candidatura a Consejero Regional y cada columna corresponde a una variable asociada a ella.

La base contiene 2.515 registros y 19 variables. Combina información proveniente directamente de las fuentes originales con variables construidas durante el proceso de preparación de los datos. Estas últimas fueron incorporadas para organizar la información de acuerdo con las preguntas de investigación para poder hacer el análisis de las candidaturas.

La base reúne variables de identificación de las candidaturas, información territorial y electoral, además de variables relacionadas con la posición dentro de las listas y los resultados de votación.

### Otras observaciones y limitaciones

Para facilitar el cruce entre las distintas fuentes se realizó un proceso de homologación de los registros. Se normalizó la escritura utilizada para identificar a las candidaturas debido a diferencias en la forma en que algunos nombres aparecían registrados entre SERVEL, la Biblioteca del Congreso Nacional y Emol.

Los nombres completos de las candidaturas fueron conservados en la base final para disminuir posibles errores de identificación y facilitar el cruce con la otra base de datos del proyecto.

Los nombres de las candidaturas se conservaron con la escritura utilizada en la base original de SERVEL. Por esta razón, no se agregaron manualmente tildes u otros signos ortográficos si no estaban presentes en la fuente original.

En la variable "subpacto", los casos en que no aparece registrada fueron identificados como "No tiene".

Existen tres candidaturas independientes que no poseen una letra de lista. Estos casos fueron identificados como "No aplica" y, para calcular las variables relacionadas con posición y tamaño de lista, fueron considerados como candidaturas individuales.

La variable "numero_papeleta" corresponde al número electoral de la candidatura, mientras que "posicion_lista" representa el lugar que ocupa dentro de su propia lista. Por esta razón, una candidatura con un número de papeleta mayor puede ocupar la primera posición de una lista diferente.

También hay que considerar que "porcentaje_votos_lista" representa la proporción de los votos obtenidos por la propia lista que corresponde a cada candidatura.

### Diccionario
| Variable | Descripción | Tipo de dato | Valores posibles | Observaciones editoriales |
|---|---|---|---|---|
| id_candidato | Identificador único construido para cada candidatura a partir de su nombre completo y circunscripción. | Texto | es único por candidatura | Variable construida para facilitar la identificación y el cruce con la otra base del proyecto. |
| nombre_candidato | Nombre completo de la candidatura. | Texto | Todos los nombres de las candidaturas | Se usaron los nombres completos registrados en SERVEL. |
| sexo | Sexo registrado en la candidatura. | Texto | H (hombre) / M (mujer)
| región | Región de su candidatura. | Texto | 16 regiones de Chile
| circunscripción | Territorio electoral o circunscripción provincial en que compite la candidatura. | Texto | 66 circunscripciones provinciales
| letra_lista | Letra que identifica la lista electoral de la candidatura. | Texto |  B, C, F, I, L, M, N, P, Q, R, S, V, W, X, Y / No aplica | Hay tres candidaturas independientes sin letra registrada |
| pacto | Pacto electoral o candidatura independiente. | Texto | Pactos o candidaturas independientes registrados por SERVEL
| subpacto | Subpacto electoral de la candidatura, cuando corresponde. | Texto | Subpactos registrados / No tiene | "No tiene" corresponde a los casos en que la candidatura no registra subpacto. |
| sigla_partido | Sigla del partido político asociado a la candidatura. | Texto | Siglas de partidos registradas
| partido | Nombre del partido político asociado a la candidatura. | Texto | Nombres de partidos registrados
| número_papeleta | Número electoral asignado a la candidatura en la papeleta. | Numérico (entero) | de 100 a 224| Los números pueden repetirse entre distintas circunscripciones.
| posición_lista | Posición relativa de la candidatura dentro de su propia lista. | Numérico (entero) | 1, 2, 3, etc. | Variable construida ordenando las candidaturas de cada lista según numero_papeleta. |
| primero_lista | Indica si la candidatura ocupa la primera posición de su lista. | Booleano (Sí/No) | Sí / No
| tamaño_lista | Cantidad de candidaturas que integran la lista dentro de la circunscripción. | Numérico (entero) | Números enteros positivos | Variable construida a partir del número de candidaturas de cada lista. |
| numero_listas_circunscripción | Cantidad de listas o candidaturas independientes que compiten en una circunscripción. | Numérico (entero) | Números enteros positivos | Variable construida a partir de las listas presentes en cada circunscripción. |
| votos | Cantidad de votos obtenidos por la candidatura. | Numérico (entero) | Números enteros iguales o mayores a 0
| votos_lista | Suma de los votos obtenidos por las candidaturas pertenecientes a una misma lista y circunscripción. | Numérico (entero) | Números enteros iguales o mayores a 0 | Variable construida mediante la suma de votos dentro de cada lista. |
| porcentaje_votos_lista | Porcentaje de los votos de su lista obtenido por la candidatura. | Numérico (decimal) | Valores entre 0 y 100 | Se calcula como (votos / votos_lista) x 100
| electo | Indica si la candidatura resultó electa como Consejero Regional. | Booleano (Sí/No) | Sí / No | Variable construida a partir del listado de consejeros electos publicado por Emol. |