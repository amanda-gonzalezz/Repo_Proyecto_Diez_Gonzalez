# Entrega 02 — Preparar y limpiar los datos

**Curso:** Narración Gráfica de No Ficción (COM-208)
**Integrantes:** Fernanda Diez, Amanda González

---

## Hipótesis actual

Existe una relación entre la posición de una candidatura dentro de su lista en la elección de Consejeros Regionales (CORE) y su resultado electoral, considerando también los niveles de gasto de campaña.

## Preguntas de investigación actuales

- ¿Existe una relación entre la posición que ocupa una candidatura dentro de su lista y el porcentaje de votos que obtiene dentro de esa lista?
- ¿Esa relación se mantiene al comparar candidaturas con niveles de gasto de campaña similares?
- ¿La relación entre posición y resultado cambia según el tamaño de la lista?
- ¿Qué relación existe entre el gasto electoral, la posición en la lista y los resultados electorales?
- ¿Qué características comparten las candidaturas electas que no ocupaban la primera posición ni estuvieron entre las de mayor gasto?

## Avance del proyecto en relación con la hipótesis

Se construyó la base nacional de las 2.515 candidaturas a CORE 2024, con posición en la lista, votos, porcentaje de votos dentro de la lista y tamaño de esta. También se construyó la base de gasto declarado ante SERVEL para ese mismo universo, cruzable con la anterior mediante `id_candidato`.

Un hallazgo nuevo al limpiar el gasto: **185 candidaturas (7,4%) no declararon gasto**, y **370 (14,7%) tienen cuenta rechazada** por SERVEL. Quienes tienen cuenta rechazada tienen bastante más probabilidad de no haber declarado gasto (30%, contra 5,3% entre los aprobados). Esto no estaba contemplado en el diseño original y se incorpora como variable de calidad (`estado_cuenta_auditoria`).

Por la corrección de la Entrega 01, las preguntas se reformularon de forma descriptiva a preguntas explícitas de **relación/correlación estadística**, incorporando el tamaño de lista como variable moderadora. Esto redefine las visualizaciones planeadas: los gráficos principales serán de dispersión con línea de tendencia, para posición-resultado y gasto-resultado, en vez de solo comparar promedios entre grupos.

## Síntesis de la historia

Cada candidatura a Consejero Regional aparece en la papeleta con un número que su propio partido le asignó, antes de contarse un solo voto. La creencia instalada es que se gana por mérito o por plata. Este proyecto pone a prueba, con datos reales de CORE 2024, una tercera explicación que casi nadie mira: el lugar donde la candidatura queda impresa en la cédula, y cómo esa posición interactúa con el gasto y el tamaño de la lista.

Con ambas bases cruzables, es posible calcular si la relación entre posición y resultado se sostiene incluso comparando candidaturas con gasto similar. El hallazgo sobre cuentas rechazadas agrega una capa nueva: no solo importa cuánto se gasta, sino qué tan prolijamente se declara, y eso también podría estar conectado con quién gana.
