# Visualización y Reducción Dimensional de Datos utilizando PCA

**Curso:** Álgebra Lineal para la Computación  
**Institución:** Universidad Católica de Temuco  
**Fecha de Entrega:** 23 de junio de 2026  

## Descripción del Proyecto
Este proyecto de investigación y desarrollo implementa el algoritmo de Análisis de Componentes Principales (PCA) mediante álgebra lineal pura (sin el uso de librerías de automatización como `scikit-learn`). 

El objetivo de la aplicación computacional es proyectar y reducir la dimensionalidad de un conjunto de datos deportivos hiperdimensional para predecir matemáticamente la probabilidad de éxito de las selecciones de fútbol en la **Copa del Mundo 2026**.

## Organización del Equipo y Roles

El trabajo fue dividido estratégicamente en cuatro módulos de desarrollo para cubrir todos los criterios de evaluación (Fundamentos matemáticos, Implementación computacional, Análisis experimental y Organización):

* **Bastián Liempi - Especialista Teórico y Fundamentos:**
    * Responsable del marco teórico, la demostración geométrica de las proyecciones y el cálculo manual de matrices.
    * **Script:** `ejemplo_manual.py` (Validación matemática paso a paso en consola).

* **Martin Hernandez - Ingeniero de Datos y Contexto:**
    * Responsable de la investigación, extracción, limpieza y estandarización estadística de las variables.
    * Generación de la matriz oficial de 48 filas (equipos clasificados) y 6 columnas (métricas de rendimiento).
    * **Script:** `carga_exploracion.py` (Generación del dataset, Z-score y análisis exploratorio).

* **Martin Lopez - Desarrollador del Algoritmo Core:**
    * Responsable de la implementación computacional del motor matemático usando `numpy`.
    * Cálculo de la Matriz de Covarianza, extracción de Autovalores/Autovectores y producto punto para la proyección dimensional.
    * **Script:** `motor_pca.py` (Motor de reducción de 6D a 2D).

* **Deris Aranquiz - Analista de Varianza y Compilador:**
    * Responsable de la interpretación de resultados, varianza explicada y compilación del documento LaTeX.
    * Visualización de los nuevos componentes ortogonales y conclusiones finales.
    * **Script:** `analisis_varianza.py` (Scree plot y gráfico de dispersión bidimensional).

## Estructura de Datos (Matriz de Entrada)
Se construyó una matriz estandarizada de 48x6 basada en estadísticas reales (Transfermarkt y FIFA). Las variables seleccionadas para el cálculo de jerarquía son:
1. Puntos FIFA.
2. Valor de Mercado de la plantilla (Millones de Euros).
3. Porcentaje de Victorias en eliminatorias.
4. Goles a Favor (Totales).
5. Goles en Contra (Totales).
6. Cantidad de jugadores en ligas Top de Europa.

## Instrucciones de Ejecución
Para replicar el experimento