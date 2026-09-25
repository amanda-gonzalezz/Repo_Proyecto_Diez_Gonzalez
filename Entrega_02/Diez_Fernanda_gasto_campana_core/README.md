 # Documentación del proceso — Base de datos de gasto de campaña (CORE 2024)

**Responsable:** Fernanda Diez

## Explicación del proceso de limpieza

**Herramientas usadas:** Python (librerías `pandas` y `openpyxl`), ejecutado en un notebook de Google Colaboratory.

**Paso 1 — Inspección del archivo original.** El archivo de SERVEL (`Reporte_Ingresos_Gastos_Definitivas2024.xlsx`) pesa cerca de 60 MB y tiene 10 hojas: una hoja resumen de auditoría, una hoja maestra de "INGRESOS Y GASTOS" con 352.687 filas (una por transacción, mezclando las cuatro elecciones de octubre 2024: Alcalde, Concejal, Consejero Regional y Gobernador Regional), y ocho hojas más de "Formularios Auxiliares" (101 a 108) con el detalle de cada tipo de documento de respaldo. Decidimos trabajar directamente con la hoja "INGRESOS Y GASTOS", porque ya consolida en una sola tabla la información que están repartida entre los ocho formularios auxiliares, evitando tener que sumarla nosotras formulario por formulario.

**Paso 2 — Filtrado.** De las 352.687 filas totales, filtramos solo las que cumplían tres condiciones a la vez: `ELECCIÓN = "CONSEJERO REGIONAL"` (para descartar las otras tres elecciones), `TIPO = "GASTO"` (para descartar los ingresos, que no nos interesan para esta base) y `TIPO CUENTA = "Candidato"` (para descartar el gasto declarado a nombre de un partido político en general, que no se puede atribuir a un candidato específico). Esto dejó 38.618 transacciones de gasto individuales.

**Paso 3 — Agregación.** Cada candidato aparece en el archivo original con tantas filas como transacciones de gasto haya hecho. Agrupamos esas filas por candidato y sumamos el monto de todas sus transacciones, generando una sola fila por candidato con su `gasto_total_declarado`. También contamos cuántas transacciones tuvo cada uno, por si en el análisis futuro interesa distinguir entre un candidato con un solo gasto grande y otro con muchos gastos chicos.

**Paso 4 — Construcción del identificador de cruce.** Como el equipo necesita cruzar esta base con la Base de datos 1 (resultados electorales), construimos `id_candidato` normalizando el nombre del candidato (mayúsculas, sin tildes, espacios reemplazados por guión bajo) y concatenándolo con la circunscripción, también normalizada. 

**Paso 5 — Verificación del cruce.** Al aplicar el `id_candidato` al archivo de gasto, 2.323 de 2.333 candidatos con gasto (99,6%) cruzaron de inmediato contra el universo completo de 2.515 candidatos de la Base de datos 1. Revisamos manualmente los 10 casos que no cruzaron, y encontramos que en todos los casos el archivo de SERVEL tenía un apellido compuesto escrito sin espacio (por ejemplo, "RODRIGUEZPENA" en vez de "RODRIGUEZ PEÑA"). Corregimos esos 10 casos a mano, comparando el nombre sin ningún espacio contra el universo completo, hasta llegar a un cruce del 100%.

**Paso 6 — Unión con el universo completo.** Unimos la tabla de gasto agregado contra el universo completo de 2.515 candidatos usando un *left join* (no un *inner join*), para que ningún candidato quedara fuera de la base aunque no hubiera declarado gasto. A los 185 candidatos sin ningún registro de gasto les asignamos `gasto_total_declarado = 0` y `declara_gasto = "No"`, en vez de dejarlos fuera de la tabla o con un valor vacío. Dejar esos casos fuera habría sesgado cualquier análisis posterior hacia los candidatos que sí gastan.

**Paso 7 — Estado de auditoría.** Agregamos el estado de aprobación de la cuenta de cada candidato (Aprueba, Aprueba con Observaciones, Rechaza), extraído de la hoja "Resultado Auditoria Cuentas" del mismo archivo. Lo incluimos como columna aparte, sin excluir a los candidatos con cuenta rechazada, para que cualquier análisis futuro pueda decidir si los excluye o no, en vez de que esa decisión quede escondida en la limpieza.

**Paso 8 — Chequeo final de calidad.** Verificamos que la base final no tuviera valores nulos, que no hubiera `id_candidato` duplicados, y que ningún monto de gasto fuera negativo o absurdamente alto. El único valor nulo genuino que apareció fue en `subpacto` (1.733 candidatos), que reemplazamos por el texto explícito `"No aplica"`, porque no es un dato faltante sino un caso donde esa variable simplemente no corresponde.

**Paso 9 — Chequeo de outliers (método IQR).** Aplicamos el método del rango intercuartílico visto en clase para detectar valores atípicos en `gasto_total_declarado`: calculamos el primer y tercer cuartil, el IQR (diferencia entre ambos), y marcamos como outlier todo candidato con gasto por sobre Q3 + 1,5×IQR (equivalente a $14.734.090). Encontramos 163 candidatos (6,5%) en esa condición. A diferencia del ejemplo de clase donde los outliers eran valores sintéticos inventados para practicar la técnica, acá se trata de candidatos reales que efectivamente gastaron montos altos, concentrados en parte en circunscripciones de Santiago. Decidimos **no eliminarlos**, ya que hacerlo habría significado borrar justamente los casos más relevantes para responder "¿quién gastó más?", una de nuestras preguntas de investigación. En vez de eso, agregamos la columna `outlier_gasto_iqr` para dejar la marca visible y que la decisión de incluir o excluir estos casos en una visualización específica se tome en la etapa de análisis, con criterio editorial, no de forma automática en la limpieza.

## Fuentes de datos utilizadas

- **SERVEL — "Reporte de Ingresos y Gastos Definitivas 2024"**: elegimos esta fuente porque es la única fuente oficial y pública del gasto de campaña declarado por cada candidato, tal como exige la Ley N° 19.884. No existe ninguna fuente alternativa o privada con esta información.
- **Base de datos 1 del equipo (resultados electorales, Amanda González)**: se reutilizó como fuente del universo de candidatos y de las variables de identificación (nombre, región, circunscripción, pacto, subpacto, partido), porque ya estaba validada por el equipo y así se garantiza que ambas bases individuales compartan exactamente el mismo listado de candidatos y el mismo esquema de `id_candidato`, permitiendo el cruce entre ambas sin duplicar trabajo ni arriesgar inconsistencias de nombres.

## Preguntas que se pueden responder con esta base limpia

**Aclaración importante:** esta base, por sí sola, **no permite responder una de las preguntas centrales del proyecto** (¿gastar más significa sacar más votos?), porque no incluye los votos de cada candidato. Esa información está en la Base de datos 1 (resultados electorales, a cargo de Amanda). Lo que sí permite esta base, cruzándola después con esa otra, es justamente construir esa comparación: una vez unidas ambas por `id_candidato`, se podrá calcular la relación entre `gasto_total_declarado` y los votos obtenidos.

Mientras tanto, se construyó una tabla dinámica (pivot table) sobre esta base para ver qué preguntas más simples ya se pueden responder solo con el gasto. **Estos son resultados preliminares y exploratorios**:

1. **¿Cuánto gasta en promedio un candidato, y cambia según el pacto al que pertenece?** Los independientes puros son los que más gastan en promedio (aprox. $9,87 millones), seguidos por Chile Vamos RN (aprox. $7,42 millones) y Chile Vamos UDI (aprox. $6,58 millones).
2. **¿Cuántos candidatos no declararon ningún gasto?** 185 candidatos (7,4% del total) aparecen con $0 de gasto declarado.
3. **¿El gasto tiene relación con si la cuenta fue aprobada o rechazada por SERVEL?** Sí, ya que entre los candidatos con cuenta rechazada, un 30% no declaró gasto, mientras que entre los aprobados esa cifra baja a un 5,3%, sugiriendo que ambas cosas están conectadas.
4. **¿En qué circunscripción se gasta más en promedio?** Santiago IV es la más alta, con aprox. $17,5 millones promedio por candidato, muy por sobre el resto del país.
