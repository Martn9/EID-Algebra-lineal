# Organización Detallada del Equipo y Tareas Críticas

Este documento establece las responsabilidades exactas de cada integrante para el proyecto "Visualización y Reducción Dimensional de Datos utilizando PCA". Es obligatorio que cada miembro lea y comprenda no solo su parte, sino la lógica general del trabajo, ya que la rúbrica indica que **las preguntas en la presentación se realizarán de manera aleatoria a cualquier integrante**.

---

## 1. Bastián Liempi: Especialista Teórico y Fundamentos

**Responsabilidad Principal:** Demostrar el dominio matemático del Análisis de Componentes Principales (PCA) mediante la redacción del Marco Teórico y la validación manual del algoritmo.

**Tareas Específicas:**
* **Redacción Teórica (LaTeX):** Debes escribir la sección del informe que explica qué es una matriz de covarianza, qué representan geométricamente los autovalores (magnitud de la varianza) y los autovectores (dirección de los nuevos ejes).
* **Desarrollo del script `ejemplo_manual.py`:** Debes crear un script en Python independiente que tome una matriz pequeña inventada (ejemplo: 3 filas por 2 columnas) y calcule el PCA paso a paso. Este script debe imprimir en consola la matriz centrada, la matriz de covarianza y los autovectores resultantes.

**Errores críticos a evitar:**
* *Error fatal:* Copiar y pegar definiciones directamente de internet o IA. La rúbrica penaliza severamente el plagio. Debes explicar el álgebra lineal con tus propias palabras y ejemplos.
* *Error en presentación:* No saber explicar cómo se pasa de la matriz original a la matriz de covarianza mediante la fórmula: `(X^T * X) / (n - 1)`.

---

## 2. Martin Hernandez: Ingeniero de Datos y Contexto

**Responsabilidad Principal:** Proveer, estructurar y justificar la matriz de datos hiperdimensional (48 selecciones x 6 métricas) que será el insumo principal del proyecto.

**Tareas Específicas:**
* **Desarrollo del script `carga_exploracion.py`:** Construir el código que contenga los datos oficiales investigados (Puntos FIFA, Valor de Mercado, % Victorias, Goles a Favor, Goles en Contra, Jugadores Ligas Top) para los 48 países clasificados al Mundial 2026.
* **Estandarización (Z-Score):** Explicar matemática y gráficamente por qué es obligatorio restar la media y dividir por la desviación estándar antes de aplicar PCA (para igualar la escala de "Millones de Euros" con la escala de "Goles").
* **Exportación:** Asegurar que el código genere el archivo físico `dataset_mundial_2026.csv` limpio y sin texto (solo números) para el siguiente paso.

**Errores críticos a evitar:**
* *Error fatal:* Entregar una matriz con datos de texto (strings) al motor PCA, lo cual rompería los cálculos matriciales.
* *Error en presentación:* Dudar si el profesor pregunta por el origen de los datos. Debes defender que es un dataset basado en métricas reales y auditadas para evitar ruido estadístico.

---

## 3. Martin Lopez: Desarrollador del Algoritmo Core

**Responsabilidad Principal:** Programar el motor matemático de reducción dimensional utilizando estrictamente operaciones de álgebra lineal pura.

**Tareas Específicas:**
* **Desarrollo del script `motor_pca.py`:** Este script debe leer el archivo `dataset_mundial_2026.csv`.
* **Cálculos Matriciales en Numpy:** Debes calcular la matriz de covarianza multiplicando matrices (`X_std.T @ X_std`). Luego, debes extraer los autovalores y autovectores utilizando exclusivamente la función `numpy.linalg.eig`.
* **Proyección:** Multiplicar la matriz estandarizada original por los 2 autovectores principales para reducir las 6 columnas iniciales a solo 2 nuevas coordenadas (PC1 y PC2). Guardar este resultado en `resultados_pca_2d.csv`.

**Errores críticos a evitar:**
* *Error fatal:* **Prohibido utilizar la librería `scikit-learn` (sklearn.decomposition.PCA)**. Si usas librerías automáticas, el equipo obtendrá calificación mínima en "Implementación Computacional", ya que el objetivo es demostrar que saben programar el álgebra subyacente.
* *Error matemático:* Olvidar ordenar los autovalores de mayor a menor. Si no los ordenas, podrías proyectar los datos sobre el eje menos importante, arruinando los resultados.

---

## 4. Deris Aranquiz: Analista de Varianza y Compilador

**Responsabilidad Principal:** Interpretar visualmente los resultados matemáticos, generar los gráficos finales y compilar el documento LaTeX definitivo.

**Tareas Específicas:**
* **Desarrollo del script `analisis_varianza.py`:** Leer el archivo `resultados_pca_2d.csv` generado por Martin L.
* **Visualización:** Generar un Gráfico de Dispersión (Scatter Plot) en 2D. El eje X (PC1) representará la "Jerarquía/Probabilidad de ganar el Mundial" y el eje Y (PC2) representará la "Volatilidad de Goles". Cada punto debe ser una selección nacional.
* **Varianza Explicada (Scree Plot):** Crear un gráfico de barras que demuestre qué porcentaje de la información original de las 6 variables logramos retener al usar solo 2 ejes.
* **Compilación en LaTeX:** Juntar la teoría de Bastián, la justificación de datos de Martin H., el código de Martin L. y tus gráficos en un único documento coherente, asegurando el formato y la bibliografía.

**Errores críticos a evitar:**
* *Error fatal:* Mostrar un gráfico sin poder explicar qué significan matemáticamente los ejes. Debes tener claro que los ejes no son variables directas, sino combinaciones lineales de las 6 variables originales.
* *Error logístico:* No revisar que los códigos de los anexos coincidan exactamente con la explicación del texto. Debes ser el filtro de calidad antes de subir el PDF a la plataforma universitaria el 23 de junio.