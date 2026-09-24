### Documentación del proceso de limpieza

#### Fuentes utilizadas

La primera fue la base de candidaturas de las Elecciones Regionales y Municipales 2024 publicada por el Servicio Electoral de Chile (SERVEL). Esta fuente fue elegida porque contiene la información necesaria para identificar a las candidaturas y su participación electoral, como nombre, sexo, región, territorio electoral, pacto, subpacto, partido, letra de lista y número de papeleta (la mayoría de los datos de la tabla se encontraba en esta base de datos).

La segunda fuente fue el sistema Elecciones Históricas de la Biblioteca del Congreso Nacional de Chile (BCN). Desde este sitio se descargaron los resultados de la elección de CORE 2024 correspondientes a cada una de las 16 regiones de Chile. Esta fuente fue utilizada para obtener la cantidad de votos oficial de cada candidatura.

La tercera fuente fue la publicación de Emol "Cómo quedó conformado cada uno de los 16 consejos regionales del país", que presenta las candidaturas electas en cada región e identifica a SERVEL como fuente de la información. Esta publicación solo se usó para identificar a las candidaturas que resultaron electas y construir la variable "electo".

### Proceso de limpieza y preparación de los datos

#### 1.Selección de las candidaturas

El proceso comenzó con la base de candidaturas de SERVEL. Como este archivo contiene información de las distintas elecciones regionales y municipales realizadas en 2024, se filtró la variable correspondiente al tipo de elección para usar solo las candidaturas a Consejero Regional.

Después de realizar este filtro quedaron 2.515 candidaturas. Este número se utilizó como referencia durante los pasos posteriores para comprobar que no se perdieran o duplicaran candidaturas al cruzar las distintas fuentes.

#### 2.Preparación de los resultados electorales de la BCN

Los resultados de la BCN estaban separados en 16 archivos, uno correspondiente a cada región del país. Estos archivos fueron reunidos para poder trabajar los resultados a nivel nacional.

Al juntar los archivos se obtuvieron inicialmente 2.579 registros. Cada archivo regional incluía cuatro filas que no correspondían a candidaturas: "Válidamente Emitidos", "Votos Nulos", "Votos Blanco" y "Total".

Como la unidad de observación de la base corresponde a una candidatura, esas filas se eliminaron. En total se eliminaron 64 registros, correspondientes a cuatro filas de cada región. Después de esta limpieza quedaron 2.515 registros de candidaturas, la misma cantidad obtenida desde SERVEL.

#### 3.Homologación y cruce de SERVEL y BCN

El siguiente paso fue cruzar la información de candidaturas de SERVEL con los resultados electorales de la BCN.

Antes de realizar este cruce se homologó la escritura de los nombres, debido a que existían diferencias entre la forma en que algunas candidaturas aparecían registradas en ambas fuentes. Se normalizaron los nombres para hacer más fácil la comparación y se comprobó que las 2.515 candidaturas de SERVEL pudieran asociarse con un registro de resultados de la BCN.

Al final de este proceso se incorporó a cada candidatura la cantidad de votos obtenidos.

#### 4.Organización territorial

Se decidió mantener "region" y "circunscripcion" como dos variables diferentes. "region" identifica una de las 16 regiones del país, mientras que "circunscripcion" corresponde al territorio electoral o circunscripción provincial en que compite la candidatura (más específico). En total, la base considera 66 circunscripciones provinciales.

La base final fue ordenada primero por región, siguiendo el orden geográfico de norte a sur y luego por circunscripción.

#### 5.Creación de un identificador

Se creó la variable "id_candidato" para contar con un identificador único para cada candidatura. Este identificador se construyó utilizando el nombre completo registrado por SERVEL junto con la circunscripción correspondiente.

Se decidió utilizar ambas variables porque el número de papeleta no funciona como identificador único a nivel nacional y puede repetirse entre distintas circunscripciones.

Además, este identificador permitirá posteriormente cruzar esta base con la otra base de datos utilizada en el proyecto.

#### 6.Construcción de la posición dentro de la lista

Una de las principales decisiones del proceso fue diferenciar "numero_papeleta" de "posicion_lista".

El número de papeleta corresponde al número electoral asignado a la candidatura, pero no indica directamente su posición relativa dentro de su lista. Para construir "posicion_lista", las candidaturas fueron agrupadas según región, circunscripción y letra de lista. Dentro de cada grupo se ordenaron de acuerdo con su número de papeleta.

La primera candidatura de cada lista recibió la posición 1, la siguiente la posición 2 y así sucesivamente. De esta forma, cuando comienza una nueva lista, la posición vuelve a comenzar desde 1 aunque el número de papeleta continúe aumentando.

A partir de esta variable se creó "primero_lista", que toma el valor "Sí" cuando la candidatura se encuentra en la posición 1 y "No" en los demás casos.

#### 7.Construcción de variables relacionadas con las listas

También se creó "tamano_lista", que indica la cantidad de candidaturas que forman parte de una misma lista dentro de una circunscripción.

Además, se construyó "numero_listas_circunscripcion", que indica cuántas listas o candidaturas independientes compiten en cada circunscripción.

Estas variables permiten analizar posteriormente si la posible relación entre la posición y los resultados cambia según el tamaño de las listas o la cantidad de listas que compiten en un mismo territorio.

#### 8.Cálculo de los votos de la lista y porcentaje de cada candidatura

A partir de la variable de votos se construyó "votos_lista". Para calcularla se sumaron los votos obtenidos por todas las candidaturas pertenecientes a una misma lista y circunscripción.

Luego se calculó "porcentaje_votos_lista" mediante la siguiente fórmula: (votos / votos_lista) x 100

Se decidió incorporar esta variable porque permite conocer qué proporción de los votos de su propia lista obtuvo cada candidatura.

#### 9.Identificación de las candidaturas electas

Para construir la variable "electo" se utilizó el listado de consejeros regionales electos publicado por Emol.

Los nombres de esta fuente también tuvieron que ser homologados antes de compararlos con la base, debido a diferencias en la forma de escribir algunos nombres. Una vez realizado el cruce, se identificaron 302 candidaturas electas. Las demás candidaturas fueron registradas con el valor "No" en esta variable.

#### 10.Casos particulares

La variable "subpacto" presenta registros vacíos cuando esta categoría no corresponde o no aparece registrada en la fuente original. Estos valores fueron mantenidos vacíos y no se agregó información que no estuviera presente en la fuente.

También se encontraron tres candidaturas independientes que no tenían una "letra_lista" registrada. Se decidió mantener estos registros sin letra y no asignarles una categoría que no apareciera en los datos originales. Para calcular las variables relacionadas con posición y tamaño de lista, estas candidaturas fueron consideradas de manera individual.

Los nombres completos también fueron conservados en la base final. Esta decisión se tomó para disminuir posibles errores de identificación y facilitar el posterior cruce con la otra base del proyecto.

#### 11.Revisión final de la base

Se verificó que existieran 2.515 registros y que los 2.515 valores de "id_candidato" fueran únicos. También se comprobó la presencia de las 16 regiones y las 66 circunscripciones provinciales.

Para las variables construidas a partir de las listas se comprobó que cada lista comenzara en la posición 1, que existiera una candidatura identificada como primera de cada lista y que la posición máxima coincidiera con el tamaño de la lista.

Finalmente, se comprobó que la variable "electo" identificara 302 candidaturas electas.

#### Herramientas utilizadas

Durante el proceso se trabajó con archivos CSV, Python y la biblioteca Pandas.

Python y Pandas se utilizaron durante el proceso para trabajar con los archivos CSV, filtrar y ordenar registros, revisar datos vacíos o duplicados, agrupar información y realizar los cálculos que necesitábamos para construir la base final.

Para construir las nuevas variables se realizaron agrupaciones según región, circunscripción y lista. A partir de estas agrupaciones se determinó la posición de cada candidatura dentro de su lista, se identificó a quienes aparecían en primera posición, se calculó el tamaño de cada lista, se contó la cantidad de listas por circunscripción y se sumaron los votos obtenidos por cada lista. También se calculó el porcentaje de votos que cada candidatura obtuvo dentro de su propia lista.

Finalmente, se revisó la consistencia de la base comprobando la cantidad de registros, posibles duplicados, valores vacíos y que las variables construidas fueran consistentes con los datos originales.

## Preguntas que se pueden responder con la base limpia

A partir de las variables disponibles en la base de datos limpia, se pueden plantear distintas preguntas relacionadas con la posición de las candidaturas dentro de sus listas y sus resultados electorales:

1. ¿Existe una relación entre la posición que ocupa una candidatura dentro de su lista y el porcentaje de votos que obtiene dentro de esa lista?

2. ¿Las candidaturas que ocupan la primera posición de su lista obtienen un mayor porcentaje de los votos de la lista que las candidaturas ubicadas en otras posiciones?

3. ¿La relación entre la posición dentro de la lista y el porcentaje de votos cambia según la cantidad de listas que compiten en cada circunscripción?

4. ¿Qué posiciones dentro de las listas concentran, en promedio, un mayor porcentaje de los votos de cada lista?