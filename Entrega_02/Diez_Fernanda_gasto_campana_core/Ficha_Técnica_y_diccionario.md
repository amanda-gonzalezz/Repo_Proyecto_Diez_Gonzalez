# Ficha Técnica y Diccionario de Datos — Gasto de campaña, Consejeros Regionales 2024

**Responsable:** Fernanda Diez

## Fuente de los datos

- **Fuente primaria:** SERVEL, "Reporte de Ingresos y Gastos Definitivas 2024" (archivo `Reporte_Ingresos_Gastos_Definitivas2024.xlsx`), descargado desde la sección "Ingresos y gastos electorales de los candidatos y candidatas" (http://www-doc.servel.cl/?tipo=ingresosygastos). Contiene el detalle línea por línea (transacción por transacción) de todos los ingresos y gastos declarados por candidaturas y partidos, para las cuatro elecciones de octubre 2024 (Alcalde, Concejal, Consejero Regional, Gobernador Regional), con 352.687 filas en total.
- **Universo de candidatos:** los 2.515 candidatos a Consejero Regional y sus columnas de identificación (nombre, región, circunscripción, pacto, subpacto, partido) provienen de la Base de datos 1 del equipo (resultados electorales, a cargo de Amanda González), construida a partir de BCN/SERVEL. Se reutiliza ese universo ya validado en vez de reconstruirlo desde cero, para que ambas bases del equipo compartan exactamente el mismo listado de candidatos y el mismo `id_candidato`. Los scripts de esta entrega buscan ese archivo primero en la carpeta de Amanda dentro del repositorio compartido (`Gonzalez_Amanda_01_datos_electorales_database_01/datos_electorales_database_limpia.csv`); si no está disponible, usan una copia de respaldo incluida en `datos_originales/` de esta misma carpeta, para que el proceso sea replicable incluso evaluando esta entrega de forma aislada.

## Metodología de la construcción de la base

La base se construyó fusionando dos fuentes: el archivo de gasto electoral de SERVEL y el universo de candidatos ya validado por el equipo (Base de datos 1). Del archivo de SERVEL (352.687 filas en total, mezclando cuatro elecciones) se filtraron únicamente las 38.618 transacciones de gasto correspondientes a candidatos individuales de Consejero Regional, y se agregaron por candidato para obtener un monto total por persona. Ese resultado se unió contra los 2.515 candidatos del universo del equipo mediante un identificador construido a partir del nombre normalizado y la circunscripción (`id_candidato`), logrando un cruce exitoso en el 99,6% de los casos de forma automática y el 100% tras corregir manualmente 10 nombres con apellidos compuestos mal escritos en el archivo original. Se agregó además el estado de auditoría de cada cuenta (Aprueba / Rechaza / Con observaciones), y los candidatos sin ningún registro de gasto quedaron explícitamente con monto $0, no fuera de la base. El detalle completo de cada paso y decisión está en el archivo `README.md` (Documentación) de esta misma carpeta.

## Alcance de los datos

- Cubre a la totalidad de los 2.515 candidatos a Consejero Regional en la elección de octubre de 2024, en las 66 circunscripciones provinciales del país.
- El gasto corresponde a lo declarado ante SERVEL entre la fecha de inscripción de candidaturas y el cierre de la rendición de cuentas post-electoral (documentos con fecha entre 2024 y comienzos de 2025, según el propio archivo de SERVEL).
- No incluye gasto de partidos políticos como tales, solo el atribuido directamente a un candidato.

## Características de los datos

- 2.515 filas, una por candidato (unidad de análisis: candidato-circunscripción).
- 13 columnas, sin valores nulos ni duplicados de `id_candidato`.
- Variable central para el análisis: `gasto_total_declarado` (numérica, en pesos chilenos).

## Otras observaciones

- **185 candidatos (7,4% del total) no declararon ningún gasto.** Es consistente con Morales y Becerra (2018), quienes reportan una proporción sin declarar bastante mayor (~25%) para concejales.
- **163 candidatos (6,5%) tienen un gasto que califica como valor atípico (outlier)** según el método IQR (umbral: $14.734.090). No se eliminaron de la base porque son candidatos reales con gasto alto, no errores de datos, y son justamente relevantes para la pregunta de investigación sobre quién gastó más (detalle completo de la decisión en la Documentación).
- **370 candidatos (14,7%) tienen su cuenta rechazada** por SERVEL, y 1.122 (44,6%) fueron aprobadas "con observaciones".

## Diccionario de datos

| Variable | Descripción | Tipo de dato | Valores posibles | Observaciones |
|---|---|---|---|---|
| `id_candidato` | Identificador único del candidato, usado para cruzar con la Base de datos 1 (resultados) | Texto | Nombre normalizado + `__` + circunscripción normalizada | Construido por el equipo, no viene de SERVEL |
| `nombre_candidato` | Nombre completo del candidato | Texto | — | Tomado de la Base de datos 1 |
| `sexo` | Sexo del candidato | Texto (categórico) | `H`, `M` | Tomado de la Base de datos 1 |
| `region` | Región de la candidatura | Texto (categórico) | 16 regiones de Chile | Tomado de la Base de datos 1 |
| `circunscripcion` | Circunscripción provincial (unidad electoral real para CORE) | Texto (categórico) | 66 circunscripciones | Tomado de la Base de datos 1 |
| `pacto` | Pacto electoral al que pertenece la lista del candidato | Texto (categórico) | — | Tomado de la Base de datos 1 |
| `subpacto` | Subpacto dentro del pacto, cuando corresponde | Texto (categórico) | Nombre del subpacto, o `"No aplica"` | `"No aplica"` reemplaza los casos sin subpacto (1.733 de 2.515) |
| `sigla_partido` | Sigla del partido político, o del carácter de independiente | Texto (categórico) | — | Tomado de la Base de datos 1 |
| `partido` | Nombre completo del partido político, o "independiente" | Texto (categórico) | — | Tomado de la Base de datos 1 |
| `gasto_total_declarado` | Suma de todos los gastos declarados por el candidato ante SERVEL | Numérico (entero, pesos chilenos) | ≥ 0, hasta $77.717.230 | 0 significa que no declaró ningún gasto |
| `num_transacciones_gasto` | Cantidad de transacciones de gasto individuales que componen el total | Numérico (entero) | ≥ 0 | Útil para detectar candidatos con un solo gasto muy grande vs. muchos gastos chicos |
| `estado_cuenta_auditoria` | Resultado de la auditoría de SERVEL sobre la cuenta del candidato | Texto (categórico) | `Aprueba`, `Aprueba con Observaciones`, `Rechaza`, `Sin información` | `Sin información` son candidatos sin registro en la hoja de auditoría del archivo |
| `declara_gasto` | Indica si el candidato declaró o no algún gasto | Texto (categórico) | `Sí`, `No` | Calculada: `Sí` si `gasto_total_declarado > 0` |
| `outlier_gasto_iqr` | Indica si el gasto del candidato es un valor atípico estadístico, según el método del rango intercuartílico (IQR) | Texto (categórico) | `Sí`, `No` | Calculada: `Sí` si `gasto_total_declarado > Q3 + 1.5×IQR` ($14.734.090). No se eliminaron estos casos de la base: corresponden a candidatos reales con gasto alto, información relevante para el análisis, no a errores de datos. Se dejan marcados para que la decisión de incluirlos o no en cada gráfico se tome en la etapa de análisis |
