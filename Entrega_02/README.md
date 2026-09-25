# Entrega 02

## Hipótesis actual

Existe una correlación entre la posición de una candidatura dentro de su lista en la elección de Consejeros Regionales (CORE) y su resultado electoral, incluso al comparar candidaturas con niveles de gasto de campaña similares.

## Preguntas de investigación actuales

- ¿Existe una correlación entre la posición de una candidatura dentro de su lista y el porcentaje de votos que obtiene dentro de ella?
- ¿Existe una correlación entre el gasto de campaña declarado y el porcentaje de votos obtenido?
- ¿Existe una correlación entre el gasto de campaña y la posición en la lista (¿gastar más implica quedar mejor ubicado)?
- ¿La correlación entre posición y resultado se mantiene al comparar candidaturas con niveles de gasto similares?
- ¿La correlación entre posición y resultado cambia según el tamaño de la lista?
- ¿Qué características comparten las candidaturas electas que no ocupaban la primera posición ni estuvieron entre las de mayor gasto?

## Avance del proyecto en relación con la hipótesis

Se construyó la base nacional de las 2.515 candidaturas a CORE 2024, con posición en la lista, votos, porcentaje de votos en la lista y tamaño de esta. También se construyó la base de gasto declarado ante SERVEL para ese mismo universo, cruzable con la anterior mediante `id_candidato`.

Un hallazgo nuevo al limpiar el gasto: **185 candidaturas (7,4%) no declararon gasto**, y **370 (14,7%) tienen cuenta rechazada** por SERVEL. Quienes tienen cuenta rechazada tienen más probabilidad de no haber declarado gasto (30%, contra 5,3% entre los aprobados). Esto no estaba contemplado en el diseño original y se incorpora como variable de calidad (`estado_cuenta_auditoria`).

Por la corrección de la Entrega 01, las preguntas se reformularon como correlaciones estadísticas explícitas (posición-resultado, gasto-resultado, gasto-posición). De forma preliminar, los gráficos principales serán de dispersión con línea de tendencia, no solo comparaciones de promedios.

## Síntesis de la historia

Cada candidatura a Consejero Regional aparece en la papeleta con un número que su propio partido le asignó, antes de contarse un solo voto. La creencia instalada es que se gana por mérito o por plata. Este proyecto pone a prueba, con datos reales de CORE 2024, una tercera explicación que casi nadie mira: el lugar donde la candidatura queda impresa en la cédula, y cómo esa posición interactúa con el gasto y el tamaño de la lista.
