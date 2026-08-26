# Base de datos 1 — Resultados electorales, elección de Consejeros Regionales (CORE)

## Autor y publicación de los datos

Los datos son producidos y publicados oficialmente por el Servicio Electoral de Chile (SERVEL), organismo autónomo constitucional a cargo de administrar el sistema electoral. Se obtienen desde la plataforma de resultados electorales oficiales: https://www.servel.cl/biblioteca-de-documentos/resultados-electorales-historicos/ 

## Contenido

La base contendrá el detalle de todas las candidaturas a Consejero Regional en las circunscripciones provinciales seleccionadas, para la elección más reciente disponible. Cada fila corresponde a un candidato individual.

## Variables (columnas)

- Nombre completo del candidato.
- Región.
- Circunscripción provincial en la que compite.
- Pacto electoral.
- Subpacto, cuando corresponda.
- Partido político o condición de independiente.
- Número asignado al candidato en la papeleta.
- Posición del candidato dentro de su lista (calculada).
- Cantidad de candidatos que componen la lista (calculada).
- Número de listas que compiten en la circunscripción (calculado).
- Votos obtenidos.
- Porcentaje de votos obtenido por el candidato dentro del total de votos de su lista (calculado).
- Electo (Sí/No).
- Género del candidato, en caso de que podamos obtener esta información desde un registro público.

Las variables que aparecen como "calculadas" serán creadas por nosotros a partir de la información recopilada. Por ejemplo, SERVEL entrega el número asignado a cada candidato en la papeleta, pero nosotros tendremos que ver qué posición ocupó dentro de su lista.


## Pertinencia

Esta base es el pilar central del proyecto: sin ella no es posible medir el efecto de orden en la papeleta, que es la variable independiente principal de la investigación. Además, permite calcular las variables de control necesarias (tamaño de lista, número de listas en competencia) que se usarán para ver bajo qué condiciones el efecto se intensifica o desaparece.

## Metodología de obtención

1. Ingresar al sitio web de SERVEL y buscar la información correspondiente a la elección de Consejeros Regionales de 2024.
2. Recopilar la información de las candidaturas a partir del Boletín Final de Consejeros Regionales publicado por SERVEL y descargar los archivos disponibles con los resultados de la elección.
3. Reunir la información de las circunscripciones seleccionadas en una misma base de datos.
4. Calcular algunas variables necesarias para el análisis (mencionadas anteriormente)
5. Revisar que la información recopilada coincida con los datos oficiales publicados por SERVEL y corregir errores antes de realizar el análisis.