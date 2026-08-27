# Entrega 01 — Propuesta de proyecto y datos a trabajar

**Curso:** Narración Gráfica de No Ficción (COM-208)
**Facultad de Comunicaciones — Pontificia Universidad Católica de Chile**
**Integrantes:** Fernanda Diez, Amanda González
---

## Título provisorio

**¿Importa el orden? El efecto de la posición en la papeleta en la elección de Consejeros Regionales**

---

## 1. Síntesis del proyecto

En las elecciones chilenas que usan listas, como concejales, diputados y consejeros regionales (CORE), cada candidato tiene un número de orden dentro de su lista, tal como aparece impreso en la papeleta. Ese número no debería cambiar el resultado, ya que en teoría, el elector vota por la persona, no por el lugar donde aparece su nombre. Pero en elecciones donde el votante no conoce a la mayoría de los candidatos, ese orden puede convertirse en un atajo al momento de marcar el voto.

La elección de Consejeros Regionales es un caso propicio para este fenómeno: es un cargo poco conocido por la ciudadanía, con escasa cobertura mediática de cada candidato, y con listas que en algunas circunscripciones llegan a tener más de cien nombres. En una papeleta tan larga, es razonable pensar que el orden pesa más que en una elección donde el elector sabe bien a quién quiere votar.

Al mismo tiempo, existe otro factor que se asume casi sin cuestionarlo como el gran explicador del éxito electoral: el dinero. En este proyecto el gasto de campaña no es un tema aparte, sino la manera de poner a prueba si el efecto del orden es real o no. La idea es simple: si comparamos solo a candidatos que gastaron montos parecidos, y aun así los que van primeros en la lista siguen sacando más votos, eso es una señal de que el orden importa por sí solo, más allá de cuánta plata tenía cada uno detrás.

La pregunta de fondo no es solo estadística. Si el orden en la papeleta realmente cambia el resultado, eso significa que parte de quién queda electo depende de una decisión interna del partido (dónde poner a cada candidato en la lista) y no solo del mérito, del trabajo territorial o de los recursos de cada persona. Es una forma de mostrar que el diseño de una papeleta, algo que parece un detalle puramente administrativo, puede tener consecuencias políticas reales.

## 2. Pregunta de investigación (hipótesis)

**La posición de un candidato en la papeleta de la elección CORE predice su resultado electoral, incluso al comparar candidatos con niveles de gasto de campaña parecidos.**

## 3. Antecedentes del tema

Existe una línea de investigación en ciencia política sobre este fenómeno, conocido como *ballot order effect* o *ballot position effect*: cuando el elector tiene poca información sobre los candidatos, tiende a usar atajos para votar, y uno de esos atajos es elegir el primer nombre de la lista.

Para Chile, el trabajo más completo es el de Mauricio Morales Quiroga y Ariel Becerra (2018), publicado en la revista *Colombia Internacional* bajo el título "El efecto de la posición del candidato en la papeleta de votación. El caso de las elecciones locales chilenas de 2008 y 2012". Con una base de casi 19 mil candidatos a concejal, encontraron que ir primero en la lista aumenta tanto el porcentaje de votos como la probabilidad de ser electo, y que ese efecto es más fuerte bajo voto obligatorio que bajo voto voluntario. El estudio ya incorpora el gasto de campaña en su análisis, y aun así el efecto de la posición se mantiene.

Ese mismo artículo menciona un trabajo anterior, de Morales y Navia (2015), que estudió específicamente la elección de consejeros regionales de 2013 con la misma pregunta. Ese documento quedó como *working paper* y no encontramos una versión de acceso público; solo sabemos de su existencia porque aparece citado dentro de Morales y Becerra (2018).

**Qué aporta nuestro proyecto por sobre estos antecedentes:**
- Usa datos actuales de la elección CORE 2024, no de una elección de hace más de una década.
- Convierte un hallazgo que hoy existe solo en papers académicos en un reportaje visual pensado para el público general, no para especialistas.

## 4. Datos

**Qué datos necesitamos para probar la hipótesis:**
- Resultado de cada candidato a CORE: votos obtenidos y si salió electo.
- Posición del candidato dentro de su lista.
- Tamaño de la lista y número de listas que compitieron en esa circunscripción.
- Gasto de campaña declarado por cada candidato.

**Qué tenemos y qué falta conseguir:**
- **Resultados electorales:** ya los tenemos, a través del Sistema Integrado de Información Territorial de la Biblioteca del Congreso Nacional, complementado con el Boletín Final de Consejeros Regionales de SERVEL.
- **Gasto de campaña:** ya tenemos el archivo con esta información, descargado desde SERVEL, pero viene consolidado con las cuatro elecciones municipales y regionales de 2024 juntas (alcaldes, concejales, gobernadores y CORE), así que hay que filtrarlo para quedarnos solo con los candidatos a Consejero Regional. Además, ya enviamos una Solicitud de Transparencia pidiendo un desglose más ordenado y detallado del gasto por candidato, porque el archivo actual entrega los montos de forma más agregada de lo que necesitamos (plazo de respuesta: 5 días hábiles).
- **Posición en la papeleta:** no está disponible. SERVEL publicó este dato durante la campaña en la página de facsímiles de las cédulas electorales, pero esa página fue eliminada del sitio una vez terminado el proceso electoral. Ya enviamos una Solicitud de Transparencia pidiéndolo directamente (plazo de respuesta: 5 días hábiles).
- **Plan B:** trabajar con los datos de la elección de Diputados 2025, que ya tenemos completos (resultados, posición en la papeleta y gasto), aplicando la misma hipótesis y el mismo método de comparación a esa elección en lugar de CORE.

**Qué datos no existen y cómo los conseguiremos:**
- No existe una tabla que ya cruce resultados con gasto de campaña por candidato: ese cruce lo construimos nosotras, uniendo ambas bases por el nombre de cada candidato.
- El porcentaje de votos dentro de la propia lista tampoco viene calculado en ninguna de las fuentes; ese cálculo también lo hacemos nosotras.

**Qué datos son públicos y cuáles no:**
- Todas las fuentes que usamos son públicas por ley: los resultados electorales y las declaraciones de gasto de campaña están disponibles sin necesidad de autorización especial.
- No usaremos ningún dato personal sensible: es información que los propios candidatos deben declarar por postular a un cargo de elección popular.

**Qué datos son confiables y cuáles no:**
- Los resultados electorales son de fuente oficial (BCN/SERVEL), así que son totalmente confiables.
- Las declaraciones de gasto dependen de lo que cada candidato reporta. Es esperable que algunos no hayan declarado gasto: Morales y Becerra (2018) encontraron esto en cerca de un cuarto de su muestra de concejales.

## 5. Preguntas que se pueden responder con los datos

- ¿Los candidatos que van primeros en su lista obtienen, en promedio, más votos que el resto?
- ¿Esa ventaja se mantiene cuando comparamos candidatos con niveles de gasto de campaña parecidos?
- ¿El efecto es más fuerte en listas con muchos candidatos que en listas cortas?
- ¿Hay candidatos que ganaron sin ir primeros en su lista y sin ser de los que más gastaron? ¿Qué tienen en común esos casos?

## 6. Historia visual

Queremos que el reportaje se sienta como estar parado frente a una papeleta real, tratando de decidir a quién votar sin conocer a nadie de la lista. Esa sensación de "elegir a ciegas" es el punto de partida emocional de la historia, antes de mostrar ningún gráfico.

**Idea narrativa**: abrir con una papeleta simulada e interactiva, donde el lector tiene que elegir un nombre sin más información que el número y el apellido de cada candidato (tal como le pasaría a un elector real frente a una lista de cien desconocidos). Después de elegir, se revela el dato: la mayoría de la gente tiende a marcar los primeros números. Desde ahí se despliega el resto del reportaje, respondiendo por qué eso pasa.

**Elementos gráficos que nos gustaría usar**:

- **Papeleta ilustrada interactiva:** una recreación visual propia de una cédula CORE. Sirve como pieza de apertura y como referencia a la que se puede volver durante todo el reportaje. 
- **Gráfico de dispersión interactivo:** posición en la papeleta vs. porcentaje de votos, con cada punto coloreado según el grupo de gasto del candidato (bajo, medio, alto), para ver de un vistazo si el patrón se repite en los tres grupos. Nos inspiramos en el recurso que usa *"Vigilantes de la pantalla"* (Colomba Bolognesi, Cecilia Orueta y Trinidad Riobó, COM208), que cruza denuncias y sanciones del CNTV en un gráfico de dispersión donde al pasar el mouse sobre cada punto aparece el nombre del programa.
- **Fichas de candidatos destacados:** tarjetas breves (nombre, posición, gasto, resultado) para los casos que rompen el patrón general (quienes ganaron yendo últimos y gastando poco), dándole rostro humano a los datos. Nos basamos en la sección "Casos clave" del mismo proyecto sobre el CNTV, que presenta los cinco programas más denunciados como fichas individuales con nombre, año y una breve descripción del caso.
- **Gráfico de "fuerza del efecto" según tamaño de lista:** barras o líneas que muestren cómo cambia el efecto del orden según cuántos candidatos tenía la lista, comparando circunscripciones con listas cortas, medianas y muy largas (algunas superaron los cien candidatos). Nos inspira cómo *"¿Qué le pasó a la Generación Dorada?"* (Ignacio Muñoz, Martín Silva y Cristóbal Navarro, COM208) divide a los jugadores de la selección en tres grupos comparables (generación dorada, recambio estable y recambio fallido) y visualiza cada grupo por separado para poder compararlos.
- **Mapa regional del efecto:** un mapa de Chile donde el color de cada región indique qué tan fuerte fue el efecto del orden ahí, con un buscador que permita filtrar por región o por macrozona (norte, centro, sur), similar al mapa de calor regional interactivo de *"Anúlemelo"* (Florencia Aguirre, Erick Liu y Vicente Soza, COM208), que usa ese mismo recurso para mostrar cómo varían los votos nulos y blancos según el territorio.

La narrativa avanza de lo general (¿existe el efecto?) a lo particular.

## 7. Resultados

**Mínimo que se puede contar con los datos disponibles:**
Con solo los resultados electorales y la posición en la papeleta podemos mostrar si existe una diferencia clara en el resultado electoral según la posición: un gráfico de dispersión, el promedio de votos por posición, y si esa ventaja se mantiene o no en listas de distinto tamaño. Esto ya es una historia completa: si el orden en la papeleta importa en Chile, respondida con datos reales de una elección actual.

**Máximo que se podría contar:**
Con las tres bases completas (resultados, posición y gasto) podemos mostrar si la ventaja de ir primero se mantiene incluso comparando candidatos con gasto parecido, identificar en qué regiones o tipos de circunscripción el efecto es más fuerte, y cerrar con los casos que rompen el patrón. En ese escenario, el reportaje no solo responde si el orden importa, sino cuánto importa y bajo qué condiciones — dejando al lector con una cifra memorable, no solo con una conclusión abstracta.

---

## Fuentes citadas en esta propuesta

- Morales Quiroga, Mauricio y Ariel Becerra. 2018. "El efecto de la posición del candidato en la papeleta de votación. El caso de las elecciones locales chilenas de 2008 y 2012". *Colombia Internacional*, núm. 96, pp. 29-55. DOI: [10.7440/colombiaint96.2018.02](https://doi.org/10.7440/colombiaint96.2018.02). Texto completo: https://www.redalyc.org/journal/812/81257495002/html/
- Morales, Mauricio y Patricio Navia. 2015. "Does the Place on the List Affect the Chances of Winning in an Open-list System? The Case of Chile in the Regional Elections of 2013". Working paper, Universidad Diego Portales (citado en Morales y Becerra 2018; sin versión de acceso público encontrada).
- Biblioteca del Congreso Nacional de Chile (BCN) — Sistema Integrado de Información Territorial, Elecciones Históricas CORES: https://www.bcn.cl/siit/elecciones_historicas/eleciones.html?tipo=Cores
- Servicio Electoral de Chile (SERVEL) — Resultados electorales históricos / Boletín Final de Consejeros Regionales 2024: https://www.servel.cl/biblioteca-de-documentos/resultados-electorales-historicos/
- Servicio Electoral de Chile (SERVEL) — Ingresos y gastos electorales de candidatos y candidatas: http://www-doc.servel.cl/?tipo=ingresosygastos
- Bolognesi, Colomba, Cecilia Orueta y Trinidad Riobó. "Vigilantes de la pantalla: cómo la audiencia fiscaliza a la televisión chilena". Proyecto COM-208. https://triobo.github.io/Repo_Proyecto_CNTV/
- Aguirre, Florencia, Erick Liu y Vicente Soza. "ANÚLEMELO: el voto que no elige presidente". Proyecto COM-208. https://liuerick.github.io/Anulemelo/
- Muñoz, Ignacio, Martín Silva y Cristóbal Navarro. "¿Qué le pasó a la Generación Dorada?". Proyecto COM-208. https://ignaciomunozm.github.io/Grupo-Futbol/
