# Entrega 04, parte individual: Fernanda Diez

## Pieza narrativa individual (Tarea 03)

- **Título:** Gasto de campaña vs. resultado electoral: ¿sirve gastar más?
- **Página publicada:** https://fernandadiezd.github.io/cronica-core-fernanda-diez/ ⚠️ *(cambiar por el link real una vez activado GitHub Pages)*
- **Archivos HTML:** carpeta [`sitio_web/`](sitio_web/)

La página es solo el **wireframe en HTML** (sin CSS), como pide el enunciado. Usa las etiquetas vistas en clases:

| Etiqueta | Para qué la usé |
|---|---|
| `<head>` con `<title>`, `<meta charset="utf-8">`, `author`, `description` y `keywords` | Información para el navegador; `utf-8` para que se vean bien las tildes y la ñ |
| `<header>`, `<main>`, `<section>`, `<footer>` | Ordenar la página en partes: presentación, crónica dividida en secciones y fuentes |
| `<h1>` y `<h2>` | Título de la crónica y subtítulos de cada sección (jerarquía de títulos) |
| `<p>` | Párrafos de la crónica |
| `<figure>`, `<img>` (con `alt`) y `<figcaption>` | La imagen de la visualización, su descripción para lectores de pantalla y la fuente |
| `<a href="..." target="_blank">` | Enlaces a las fuentes (SERVEL, BCN, Morales y Becerra) y al repositorio |
| `<ul>` y `<li>` | Lista de cifras clave y lista de fuentes |
| `<strong>` | Destacar las cifras más importantes |

La imagen se llama con ruta relativa (`vis_01.jpg`, en la misma carpeta que `index.html`), así funciona igual en el repositorio grupal y en GitHub Pages.

## Respaldo de la visualización

Carpeta [`visualizacion/`](visualizacion/):

| Archivo | Qué es |
|---|---|
| `vis_01.html` | Versión interactiva del gráfico (zoom y tooltip con nombre, partido, circunscripción, gasto, posición y % de votos) |
| `vis_01.jpg` | Versión estática (la misma que usa la crónica) |
| `codigo_visualizacion.ipynb` | Notebook de Colab con el código en Altair |
| `gasto_vs_resultado_electoral.csv` | Base usada: 2.515 candidaturas CORE 2024, gasto declarado cruzado con resultado electoral |

**Cambios respecto de la Entrega 03:** ninguno en los datos ni en el gráfico. Solo se actualizó la ruta del CSV dentro del notebook para que apunte a esta carpeta de la Entrega 04.

## Análisis breve

Mi visualización responde una de las preguntas del proyecto: *¿existe una correlación entre el gasto de campaña declarado y el porcentaje de votos obtenido?* Sí existe, pero es débil (r de Pearson = 0,24). Quienes salieron electos gastaron más (mediana de $7,5 millones contra $2,3 millones), pero hubo 8 electos que no declararon gasto. Por eso en el reportaje el gasto es la explicación que todos esperan, y después la comparamos con la posición en la lista, que es nuestra hipótesis principal. En la webstory, este gráfico va en el **Capítulo 3: "¿Y la plata?"** (ver wireframes de la entrega grupal).

## Fuentes

- Servicio Electoral de Chile (SERVEL). Ingresos y gastos electorales de candidatos y candidatas: http://www-doc.servel.cl/?tipo=ingresosygastos
- SERVEL. Resultados electorales históricos: https://www.servel.cl/biblioteca-de-documentos/resultados-electorales-historicos/
- Biblioteca del Congreso Nacional, SIIT. Elecciones históricas CORE: https://www.bcn.cl/siit/elecciones_historicas/eleciones.html?tipo=Cores
- Morales Quiroga, M. y Becerra, A. (2018). "El efecto de la posición del candidato en la papeleta de votación". *Colombia Internacional*, 96, 29-55. https://doi.org/10.7440/colombiaint96.2018.02
