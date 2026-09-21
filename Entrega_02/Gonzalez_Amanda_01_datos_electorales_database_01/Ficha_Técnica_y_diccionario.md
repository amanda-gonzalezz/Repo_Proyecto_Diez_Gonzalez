## Ficha técnica y diccionario de datos

### Fuente de los datos

La base fue construida a partir de la integración de tres fuentes de datos sobre la elección de Consejeros Regionales (CORE) de Chile realizada en 2024.

La primera fuente corresponde a la base de candidaturas de las Elecciones Regionales y Municipales 2024 publicada por el Servicio Electoral de Chile (database_raw_01). De esta fuente se utilizaron los registros correspondientes a la elección de consejeros regionales y variables como nombre, sexo, región, territorio electoral, pacto, subpacto, partido, letra de lista y número de candidatura.

La segunda fuente corresponde al sistema Elecciones Históricas de la Biblioteca del Congreso Nacional de Chile (database_raw_02). Desde este sitio se descargaron los resultados de la elección de CORE 2024 para cada una de las 16 regiones del país. De estos archivos se obtuvo principalmente la cantidad de votos correspondiente a cada candidatura.

Finalmente, para identificar a las candidaturas electas se utilizó el listado publicado por Emol, “Cómo quedó conformado cada uno de los 16 consejos regionales del país”(database_raw_03), que presenta los consejeros regionales electos e identifica como fuente de la información al SERVEL. Esta fuente se usó para construir la variable de quienes fueron electos.

### Metodología de construcción de la base

La unidad de observación de la base corresponde a una candidatura a consejero o consejera regional. Cada fila representa, por lo tanto, a una candidatura.

El proceso comenzó con la base de candidaturas de SERVEL. Se seleccionaron únicamente los registros correspondientes a la elección de Consejeros Regionales, obteniendo 2.515 candidaturas.

Luego se reunieron los 16 archivos regionales de resultados descargados desde la Biblioteca del Congreso Nacional de Chile . Estos archivos tenían registros de candidatos y filas de resumen electoral. Se eliminaron las categorías “válidamente emitidos”, “votos nulos”, “votos blanco” y “total”, porque no corresponden a candidaturas y no coinciden con la unidad de observación definida para la base.

Después se homologaron los nombres utilizados por SERVEL y los datos de la Biblioteca del Congreso Nacional para poder cruzar ambas fuentes. El proceso permitió asociar las 2.515 candidaturas registradas en SERVEL con sus respectivos resultados electorales de la Biblioteca del Congreso Nacional.

Se mantuvieron como variables territoriales separadas "región" y "circunscripcion" (que corresponde al territorio electoral o circunscripción provincial en que compite cada candidatura)

También se construyó "id_candidato", formado a partir del nombre completo que aparecía en el documento del SERVEL junto a su circunscripción. Esta variable fue creada para facilitar la identificación de cada candidato y poder cruzarla más fácil con la otra base de nuestro proyecto.

A partir de la estructura de las listas y del número de papeleta se construyeron nuevas variables. Una llamada "posicion_lista" que indica el lugar relativo de la candidatura dentro de su propia lista. Otra llamada "primero_lista" que identifica a quienes ocupan la primera posición. Otra llamada "tamano_lista" que corresponde a la cantidad de candidatos de cada lista y por último una llamada "numero_listas_circunscripcion" que registra la cantidad de listas o candidaturas independientes que compiten en cada circunscripción.

También se calculó "votos_lista" mediante la suma de los votos obtenidos por las candidaturas pertenecientes a una misma lista y circunscripción. A partir de este resultado se construyó "porcentaje_votos_lista", calculado de la siguiente manera:

porcentaje_votos_lista = (votos / votos_lista) x 100

Finalmente, el listado publicado por Emol fue utilizado para identificar las candidaturas electas y construir la variable "electo".

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

La base contiene 2.515 registros y 19 variables. Incluye datos cualitativos o categóricos, utilizados para describir características de las candidaturas y su participación electoral, y datos cuantitativos, que permiten realizar cálculos y análisis sobre aspectos como la posición dentro de la lista y los resultados de votación.

La base combina información proveniente directamente de las fuentes originales con variables construidas durante el proceso de preparación de los datos. Estas últimas fueron incorporadas para organizar la información de acuerdo con las preguntas de investigación y permitir el posterior cruce y análisis de las candidaturas.

### Otras observaciones y limitaciones

Para facilitar el cruce entre las distintas fuentes se realizó un proceso de homologación de los registros. Se normalizó la escritura utilizada para identificar a las candidaturas, debido a diferencias en la forma en que algunos nombres aparecían registrados entre las fuentes.

Los nombres completos de las candidaturas fueron conservados en la base final para disminuir errores y facilitar el cruce con la otra base de datos del proyecto.

La variable "subpacto" contiene registros vacíos en los casos en que esta categoría no corresponde o no aparece registrada en la fuente original.

También existen tres candidaturas independientes que no poseen una "letra_lista" registrada. Estos casos no se les asignó una letra. Para las variables relacionadas con posición y tamaño de lista fueron consideradas como candidaturas individuales.

Hay que distinguir la variable "numero_papeleta" de "posicion_lista". La primera corresponde al número electoral de la candidatura, mientras que "posicion_lista" representa el lugar que ocupa dentro de su propia lista. Entonces una candidatura con un número de papeleta mayor puede ocupar igualmente la primera posición de una lista distinta.

También hay que considerar el significado de "porcentaje_votos_lista". Esta variable representa la proporción de los votos obtenidos por su propia lista que corresponden a esa candidatura y que se calculó como se mencionó previamente.

La base permite explorar si existe una relación entre la posición de una candidatura dentro de su lista y el porcentaje de votos que concentra dentro de ella. Una asociación entre ambas variables no permite establecer por sí sola que la posición sea la causa de una mayor o menor votación. Existen otros factores que podrían relacionarse con los resultados y que no están incluidos en esta base.

