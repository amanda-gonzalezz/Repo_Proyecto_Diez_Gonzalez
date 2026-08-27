# Base de datos 1 — Resultados electorales, elección de Consejeros Regionales (CORE)

## Autor y publicación de los datos

Los datos son producidos y publicados oficialmente por el Servicio Electoral de Chile (SERVEL), organismo autónomo constitucional a cargo de administrar el sistema electoral. Se obtienen desde la plataforma de resultados electorales oficiales: https://www.servel.cl/biblioteca-de-documentos/resultados-electorales-historicos/ 

Como fuente complementaria usamos el **Sistema Integrado de Información Territorial (SIIT) de la Biblioteca del Congreso Nacional (BCN)**, que permite generar los resultados de la elección CORE por año (2013, 2017, 2021, 2024) y por unidad territorial (región, comuna, circunscripción), con base en los resultados definitivos sancionados por el TRICEL: https://www.bcn.cl/siit/elecciones_historicas/eleciones.html?tipo=Cores

## Contenido

La base contendrá el detalle de todas las candidaturas a Consejero Regional en las circunscripciones provinciales seleccionadas, para la elección más reciente disponible. Cada fila corresponde a un candidato individual.

## Variables (columnas)

- Crearemos un identificador para el cruce con la Base de datos 2, que se construirá con el nombre + circunscripción provincial. No es un dato que entregue SERVEL, lo generamos nosotras de la misma forma en ambas bases.
- Nombre completo del candidato.
- Región.
- Circunscripción provincial.
- Pacto electoral.
- Subpacto, cuando corresponda.
- Partido político o condición de independiente.
- Número asignado al candidato en la papeleta.
- Posición del candidato dentro de su lista (calculada).
- Cantidad de candidatos que componen la lista (calculada).
- Número de listas que compiten en la circunscripción (calculada).
- Votos obtenidos.
- Porcentaje de votos obtenido por el candidato dentro del total de votos de su lista (calculada).
- Electo (Sí/No).
- Género del candidato, en caso de que podamos obtener esta información desde un registro público.

Las variables que aparecen como "calculadas" serán creadas por nosotros a partir de la información recopilada. Por ejemplo, SERVEL entrega el número asignado a cada candidato en la papeleta, pero nosotros tendremos que ver qué posición ocupó dentro de su lista.

**Nota de estado:** el número asignado al candidato en la papeleta es el dato que aún no tenemos confirmado para el total de la base. Ya enviamos una Solicitud de Transparencia a SERVEL pidiéndolo explícitamente y lo incluimos aquí como columna planificada porque es la variable central de nuestra hipótesis. Si la respuesta no llega a tiempo, usaremos como alternativa la variable binaria "encabeza su lista sí/no".

## Pertinencia

Esta base es el pilar central del proyecto: sin ella no es posible medir el efecto de orden en la papeleta, que es la variable independiente principal de la investigación. Además, permite calcular las variables de control necesarias (tamaño de lista, número de listas en competencia) que se usarán para ver bajo qué condiciones el efecto se intensifica o desaparece.

## Metodología de obtención

1. Ingresar al sitio web de SERVEL y buscar la información correspondiente a la elección de Consejeros Regionales de 2024.
2. Recopilar la información de las candidaturas a partir del Boletín Final de Consejeros Regionales publicado por SERVEL y descargar los archivos disponibles con los resultados de la elección.
3. Complementar y verificar con el SIIT de la BCN, generando los resultados por región/circunscripción para las candidaturas seleccionadas.
4. Reunir la información de las circunscripciones seleccionadas en una misma base de datos.
5. Construir el identificador de cada candidato (nombre + circunscripción provincial), usando el mismo método que la Base de datos 2, para que ambas bases se puedan cruzar.
6. Calcular las variables derivadas mencionadas arriba (posición dentro de la lista, tamaño de la lista, número de listas, porcentaje de votos dentro de la lista).
7. Revisar que la información recopilada coincida con los datos oficiales publicados por SERVEL y corregir errores antes de realizar el análisis.

No se requiere web scraping: la información se obtiene por descarga y consulta directa en ambos sitios oficiales.