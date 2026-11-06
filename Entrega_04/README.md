# Entrega 04: Persona, prototipo y sistema de diseño

**Proyecto:** ¿Importa el orden? El efecto de la posición en la papeleta en la elección de Consejeros Regionales 2024

**Equipo:** Fernanda Diez y Amanda González (COM-208, UC)

## Links

- Pizarra de Miro (personas, mapa de viaje y wireframes): https://miro.com/app/board/uXjVERVzEio=/?share_link_id=659569609429 
- Página individual de Fernanda Diez: está en el README de [`Diez_Fernanda_01_gasto_vis_01`](Diez_Fernanda_01_gasto_vis_01/README.md)
- Página individual de Amanda González: está en el README de su carpeta

## Archivos

| Archivo | Qué tiene |
|---|---|
| `Perfiles de persona.pdf` | Los dos arquetipos: Camila (usuaria media) y Rodrigo (usuario extremo) |
| `Mapa de viaje.pdf` | El mapa de viaje de Camila |
| `Wireframe_prototipo.pdf` | Wireframes de baja fidelidad: 11 pantallas para computador y 3 para celular |
| `Identidad visual.pdf` | Libro de identidad visual |
| `Diez_Fernanda_01_gasto_vis_01/` | Parte individual de Fernanda |
| `Recursos_prototipo/` | Logo e íconos en SVG, imágenes PNG de los boards y los archivos HTML con que armamos los PDF |

## 1. Personas y mapa de viaje

Usamos la plantilla de arquetipo que vimos en clases (nombre, descripción, historial, recursos, emociones, objetivos y escenario).

**Camila Rojas (usuaria media).** Es profesora, tiene 31 años y vive en Quilpué. En 2024 fue a votar porque era obligatorio, pero para CORE no conocía a nadie y marcó al primero de la lista. Lee noticias en el celular, en el metro. La elegimos como usuaria media porque es justo el tipo de votante del que habla nuestra hipótesis.

**Rodrigo Fuentes (usuario extremo).** Es asesor electoral de un partido y le toca decidir el orden de las listas. Es "extremo" porque sabe mucho más que el lector promedio. No le interesa el juego de la papeleta: quiere ver cómo hicimos el análisis, buscar su región y descargar los datos. Nos sirvió para no olvidarnos de la parte de metodología.

**Mapa de viaje.** Lo hicimos con Camila porque el recorrido principal de la webstory está pensado para ella. Cada etapa es un capítulo. El momento más bajo es cuando se entera de que 2 de cada 3 electos iban primeros, porque se da cuenta de que ella hizo lo mismo. Ese momento tiene que estar porque es el dato principal, pero después del bajón vienen cosas que la ayudan a seguir leyendo: un gráfico con notas que explican qué mirar, las fichas de quienes ganaron sin ir primeros y al final la opción de buscar su región y compartir.

## 2. Manual de identidad

### Cómo llegamos a la propuesta (moodboard)

Pensamos en qué objeto resume la historia y llegamos a la papeleta. De ahí sacamos casi todo: fondo blanco, texto negro, casillas, números y listas de nombres. Después pensamos en qué hace una persona cuando revisa un documento con atención: lo marca con lápiz pasta y subraya con destacador. Esas dos cosas se transformaron en nuestros dos colores de acento.

En el moodboard juntamos una recreación de una lista de la papeleta, el destacador amarillo, el trazo de lápiz azul, los números de la cédula, la urna y los referentes del curso que ya habíamos elegido en la Entrega 01 ("ANÚLEMELO" por el mapa y "Vigilantes de la pantalla" por el gráfico de dispersión y las fichas).

### Logo

Tiene una casilla de la papeleta con la raya vertical que se hace al votar, y al lado el nombre "¿importa el orden?" en minúsculas. "el orden" va subrayado con destacador porque es lo que estamos cuestionando. Hicimos una versión normal, una en negativo (sobre azul), una a una tinta y un ícono para la pestaña del navegador.

### Color

Usamos la regla 60-30-10 de la Clase 10:

| Color | Código | % | Para qué |
|---|---|---|---|
| Blanco | `#FFFFFF` | 60% | Fondo, como el papel de la papeleta |
| Negro | `#141414` | 30% | Textos, líneas y ejes de los gráficos |
| Azul lápiz | `#2340D8` | 10% | Lo más importante: el candidato que va 1° en los gráficos y los botones principales |

Colores de apoyo: amarillo destacador `#FFE44D` (para resaltar frases y cifras en el texto, nunca como color de letra), verde `#1E8C5A` (todo lo que tiene que ver con el gasto), gris `#9A9A9A` (el resto de los candidatos en los gráficos) y gris claro `#EEEEEE` (fondos de cajas y fichas).

Dejamos el azul para pocas cosas a propósito. Si en un gráfico algo está en azul, es porque iba primero en su lista, entonces el color también ayuda a entender el dato.

### Tipografía

| Fuente | Dónde la usamos | Por qué |
|---|---|---|
| Poppins (Bold y Medium, Google Fonts) | Títulos, cifras grandes y botones | Es simple y redonda, se lee bien en el celular y hace el tema menos frío |
| Inter (Regular y SemiBold, Google Fonts) | Texto de la crónica | Está hecha para pantallas, los párrafos largos se leen cómodos |
| Courier New (fuente web segura) | Datos, etiquetas de gráficos y la papeleta | Parece escrita a máquina, como un documento oficial, y está en todos los computadores |

### Recursos gráficos

- **Íconos:** 16 íconos de línea en negro (menú, bajar, casilla, gráfico, gasto, ficha, mapa, buscar, compartir, descargar, info, cerrar, siguiente, anterior, urna y lista).
- **Botones:** redondeados. El principal es azul; al pasar el mouse se oscurece y se subraya; desactivado queda gris. Los secundarios son blancos con borde negro.
- **Ficha de candidatura:** circunscripción, nombre, posición en la lista, gasto y resultado.
- **Etiquetas y notas:** etiquetas de color para las categorías de los gráficos (azul = 1° de la lista, gris = resto, verde = gasto) y notas cortas al lado de los datos con una flecha.
- **Fotografía:** blanco y negro, tipo documental, en planos de detalle (manos, lápices, papeletas, urnas). Sin caras de candidatos para no favorecer a nadie. Pueden ser fotos nuestras o de archivo con licencia libre.
- **Ilustración:** dibujos de línea simple en negro con un poco de azul o amarillo, para explicar procesos como votar o armar una lista.
- **Patrón:** una grilla de casillas vacías con algunas marcadas, de fondo en la portada y entre capítulos.

## 3. Wireframes

- Link al prototipo: https://miro.com/app/board/uXjVERVzEio=/?share_link_id=659569609429
- PDF: `Wireframe_prototipo.pdf`

### Estructura

La webstory se lee haciendo scroll hacia abajo y está dividida en 5 capítulos. Va de lo general a lo particular, como lo planteamos en la Entrega 01.

| # | Pantalla | Qué pasa | Recursos |
|---|---|---|---|
| 00 | Portada | Título en forma de pregunta, foto y botón "Empezar" | Botón principal, foto |
| 01 | Menú | Lista de capítulos para saltar de uno a otro | Menú ☰ y barra de progreso |
| 02-03 | Cap. 1: Elige a ciegas | El lector marca un nombre en una papeleta con nombres que no conoce y después le mostramos el dato | Papeleta interactiva |
| 04 | Cap. 2: El efecto | 204 de los 302 electos iban primeros | Cifra grande, crónica y la visualización de Amanda |
| 05 | Cap. 3: ¿Y la plata? | El gasto ayuda, pero no explica todo | La visualización de Fernanda, con botones para filtrar por gasto y una nota |
| 06 | Cap. 4: Las excepciones | Candidatos que ganaron sin ir primeros y gastando poco | Fichas en carrusel |
| 07 | Cap. 5: Tu región | El lector busca su región | Mapa con buscador |
| 08 | Crónicas | Links a nuestras páginas individuales | Tarjetas con imagen |
| 09 | Cierre | "La próxima vez que votes, ¿vas a marcar al primero?" | Botones de compartir y metodología |
| 10 | Metodología | Fuentes, cómo hicimos el cruce y descarga de datos | Acordeón y botón de descarga |

### Flujo

- **Camila** sigue el camino normal, de la portada al cierre. Cada capítulo responde una pregunta y termina llevando al siguiente.
- **Rodrigo** puede usar el menú para ir directo a "Tu región", después a la metodología y descargar el CSV, sin pasar por la papeleta.
- Cada gráfico tiene una nota que explica qué mirar, para que Camila no se pierda. La parte técnica queda al final en un acordeón, así está para quien la necesite pero no molesta al resto.
- Tomamos dos ideas de la Clase 10. La papeleta interactiva es una interfaz esqueumórfica, porque imita un objeto real que todos conocen. Las casillas, flechas y botones son affordances: el lector ya sabe cómo usarlos sin que se lo expliquemos.
- En celular (M1 a M3) todo va en una columna, las casillas son más grandes para el dedo y la información del gráfico aparece con un toque.
- Los wireframes están en gris porque en esta etapa estamos probando la estructura, no los colores.

## 4. Hipótesis y trabajo en grupo

### Hipótesis actualizada

> Existe una correlación entre la posición de una candidatura dentro de su lista en la elección CORE 2024 y su resultado electoral, y esa correlación es más fuerte que la del gasto de campaña: la ventaja de ir primero se mantiene en todos los niveles de gasto.

### Por qué la cambiamos

En la Entrega 03 miramos cada factor por separado. El gasto tiene una correlación débil con el resultado (r = 0,24, gráfico de Fernanda) y 2 de cada 3 electos iban primeros en su lista (gráfico de Amanda). Para esta entrega hicimos un primer cruce de los dos. Dejamos solo las listas con 3 o más candidatos (2.091 candidaturas), porque en una lista de 1 o 2 personas ir primero no significa mucho. Después separamos a los candidatos en tres grupos del mismo tamaño según cuánto gastaron:

| Gasto | % de votos en su lista: 1° | % de votos en su lista: resto | % electos: 1° | % electos: resto |
|---|---|---|---|---|
| Bajo (hasta $1,5 millones) | 31,0% | 13,2% | 19,1% | 1,3% |
| Medio ($1,5 a $4,75 millones) | 36,9% | 15,0% | 27,5% | 4,8% |
| Alto (más de $4,75 millones) | 42,7% | 21,0% | 50,2% | 12,0% |

En los tres grupos, el que va primero saca más del doble de votos que el resto. O sea, la ventaja de ir primero sigue estando aunque comparemos candidatos que gastaron parecido. Esto apoya la hipótesis, pero todavía es un cálculo preliminar: nos falta ver si cambia según el tamaño de la lista y la región.

### Preguntas de investigación

1. ¿Existe una correlación entre la posición de una candidatura en su lista y el % de votos que obtiene dentro de ella?
2. ¿Existe una correlación entre el gasto declarado y el % de votos? (Respondida en la Entrega 03: sí, pero débil, r = 0,24.)
3. ¿La correlación entre posición y resultado se mantiene si comparamos candidaturas con gasto parecido? (Primer cruce: sí, ver tabla.)
4. ¿El efecto cambia según el tamaño de la lista y según la región?
5. ¿Qué tienen en común los electos que no iban primeros ni estaban entre los que más gastaron?

### Cómo nos vamos a dividir el trabajo

| Tarea | Quién |
|---|---|
| Papeleta interactiva (cap. 1) y texto de inicio | Fernanda |
| Gráfico de dispersión con filtros por gasto (cap. 3) y tabla del cruce | Fernanda |
| Gráfico de electos por región (cap. 2) y mapa con buscador (cap. 5) | Amanda |
| Elegir y escribir las fichas de excepciones (cap. 4) | Amanda |
| Armar la página en HTML y CSS con la identidad, metodología y revisión final | Las dos |

## Fuentes

- SERVEL. Resultados electorales históricos y Boletín Final de Consejeros Regionales 2024. https://www.servel.cl/biblioteca-de-documentos/resultados-electorales-historicos/
- SERVEL. Ingresos y gastos electorales de candidatos y candidatas. http://www-doc.servel.cl/?tipo=ingresosygastos
- Biblioteca del Congreso Nacional, SIIT. Elecciones históricas CORE. https://www.bcn.cl/siit/elecciones_historicas/eleciones.html?tipo=Cores
- Morales Quiroga, M. y Becerra, A. (2018). "El efecto de la posición del candidato en la papeleta de votación. El caso de las elecciones locales chilenas de 2008 y 2012". *Colombia Internacional*, 96, 29-55. https://doi.org/10.7440/colombiaint96.2018.02
- Plantilla de arquetipo basada en "The Persona Core Poster", Creative Companion (2011), vista en clases. https://creativecompanion.wordpress.com/2011/05/05/the-persona-core-poster/
- Clase 10 del curso (UX/UI, arquetipos, mapa de viaje, wireframes, regla 60-30-10 y affordances).
- Referentes COM-208: Aguirre, Liu y Soza, "ANÚLEMELO" (https://liuerick.github.io/Anulemelo/); Bolognesi, Orueta y Riobó, "Vigilantes de la pantalla" (https://triobo.github.io/Repo_Proyecto_CNTV/).
- Tipografías: Poppins e Inter (Google Fonts, https://fonts.google.com) y Courier New (fuente web segura).
