# Entrega 03

## Hipótesis actual

Existe una correlación entre la posición de una candidatura dentro de su lista en la elección de Consejeros Regionales (CORE) y su resultado electoral, incluso al comparar candidaturas con niveles de gasto de campaña similares.

## Preguntas de investigación actuales

- ¿Existe una correlación entre la posición de una candidatura dentro de su lista y el porcentaje de votos que obtiene dentro de ella?
- ¿Existe una correlación entre el gasto de campaña declarado y el porcentaje de votos obtenido?
- ¿Existe una correlación entre el gasto de campaña y la posición en la lista (¿gastar más implica quedar mejor ubicado)?
- ¿La correlación entre posición y resultado se mantiene al comparar candidaturas con niveles de gasto similares?
- ¿Qué características comparten las candidaturas electas que no ocupaban la primera posición ni estuvieron entre las de mayor gasto?

## Avance del proyecto en relación con la hipótesis y preguntas de investigación

En esta entrega cada una construyó una visualización distinta, cuidando que no se repitieran entre sí: Amanda mostró qué posición ocupaban en su lista las 302 candidaturas electas, región por región (204 iban primeras y 98 en otros lugares); Fernanda trabajó la relación entre el gasto de campaña declarado y el resultado electoral. Ambas visualizaciones usan las bases ya limpias de la Entrega 02, cruzadas por `id_candidato`.

El cruce de gasto y resultado confirma algo que ya se sospechaba, pero ahora con los 2.515 candidatos a CORE 2024: hay una correlación positiva entre gasto y porcentaje de votos (r de Pearson = 0,24; estadísticamente significativa), más clara todavía al comparar electos con no electos, ya que quienes resultaron electos gastaron en promedio más del doble que quienes no (mediana de $7,5 millones contra $2,3 millones). Sin embargo, la relación es débil-moderada, no determinante: hubo 8 candidatos electos que no declararon ningún gasto. Del lado de la posición, el 67,5% de los electos iba primero en su lista, y mirando a todas las candidaturas, el 29,1% de quienes iban primeros salió electo contra solo el 5,4% del resto. Ambos factores se relacionan con el resultado; falta cruzarlos para ver si la posición pesa más que el gasto, que es lo que viene en la próxima etapa.

## Síntesis de la historia

Cada candidatura a Consejero Regional llega a la papeleta con un número que su propio partido le asignó antes de que se contara un solo voto, y compite además con lo que logró gastar en campaña. La creencia instalada es que se gana por plata o por buena posición en la lista. Este proyecto separa esos dos factores con datos reales de CORE 2024: el gasto sí se relaciona con mejores resultados, pero de forma más débil de lo que se podría pensar, lo que deja abierta la pregunta de si el verdadero factor decisivo es, en realidad, el lugar donde la candidatura queda impresa en la cédula.
