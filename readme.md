Integrante 1: Especialista Teórico y Fundamentos          *BASTI*
Este rol no necesita que nadie escriba código ni busque datos para comenzar; se basa puramente en la investigación matemática.
Tareas de Informe:
•	Redactar la sección completa "I. Marco Teórico".
•	Explicar los fundamentos del PCA, su objetivo de reducción dimensional, las proyecciones vectoriales y su interpretación geométrica.
•	Definir la matriz de covarianza, su interpretación estadística y la relación entre variables.
•	Explicar la dirección de máxima varianza, los componentes principales y qué representan los autovalores y autovectores en el PCA.
•	Desarrollar un ejemplo matemático simple paso a paso utilizando un conjunto de datos bidimensionales inventado.
•	Documentar en el informe el cálculo de la media, el centrado de datos, la matriz de covarianza y la interpretación de autovalores del ejemplo manual.
Tareas de Código:
•	Programar un script independiente (ej. ejemplo_manual.py) que resuelva tu ejemplo bidimensional paso a paso sin usar librerías avanzadas, validando tus cálculos teóricos.


Integrante 2: Ingeniero de Datos y Contexto.         *MARTIN H.*
Este integrante define la materia prima del proyecto, pero los demás pueden avanzar usando datos falsos (dummy data) mientras este rol finaliza su búsqueda. Una sugerencia interesante para este integrante es buscar un dataset relacionado con el modelamiento matemático de formas de onda o procesamiento de audio, lo cual le dará un giro mucho más profundo al trabajo que el clásico conjunto "Iris".
Tareas de Informe:
•	Desarrollar íntegramente la sección "II. Representación de datos".
•	Seleccionar y justificar un conjunto de datos reales.
•	Explicar cómo se representa el conjunto mediante matrices, indicando qué son las filas, columnas, variables totales y dimensión original.
•	Documentar el análisis preliminar de los datos, incluyendo dimensiones y estadísticas básicas.
•	Investigar y redactar qué aplicaciones modernas de computación utilizan técnicas de reducción dimensional para la sección de conclusiones.
Tareas de Código:
•	Crear el script carga_exploracion.py que importe el dataset elegido y automatice la generación de gráficos iniciales y la búsqueda de patrones.


Integrante 3: Desarrollador del Algoritmo Core.             *MARTIN L.*
Este rol construye el "motor" del PCA. Para no depender del Integrante 2, debe programar funciones en Python que reciban cualquier matriz genérica (usando una matriz aleatoria de NumPy por el momento).
Tareas de Informe:
•	Redactar la sección "III. Implementación computacional - A). Implementación".
•	Explicar teóricamente cómo la proyección sobre los componentes principales permite reducir la dimensionalidad de los datos.
•	Analizar de forma visual si aparecen agrupaciones o separaciones en los datos procesados una vez que el código esté listo.
Tareas de Código:
•	Construir el archivo motor_pca.py con una función principal que cargue datos, los centre y calcule la matriz de covarianza.
•	Integrar en la misma función la obtención de autovalores, autovectores, la aplicación del PCA y la reducción a 2 dimensiones.
•	Programar la lógica de visualización mediante gráficos 2D o 3D para ilustrar el antes y el después de aplicar PCA.



Integrante 4: Analista de Varianza y Compilador.         *DERIS* 
Este rol analiza los resultados del algoritmo. Para avanzar de inmediato, puede programar sus scripts gráficos asumiendo que recibirá una simple lista de números (los autovalores) del Integrante 3.
Tareas de Informe:
•	Redactar la sección "III. Implementación computacional - B). Análisis".
•	Explicar cómo se interpreta la varianza explicada por cada componente principal.
•	Analizar estadísticamente cuánta información o varianza se conserva en la implementación tras reducir la dimensionalidad.
•	Discutir exhaustivamente las ventajas y limitaciones generales del uso de PCA, evaluando la pérdida de información y la reducción de ruido.
•	Asumir el rol de compilador final: juntar las partes del texto, listar el lenguaje y bibliotecas usadas, organizar el código fuente documentado y estructurar la bibliografía.
Tareas de Código:
•	Crear el script analisis_varianza.py que genere los gráficos de la varianza explicada por componente y la distribución acumulada.
•	Asegurar que el código final genere proyecciones finales claras de los datos.


*Nota importante para el equipo:*
Deben tener extremo cuidado de escribir el código y los textos de forma original y crítica, ya que la copia directa desde inteligencias artificiales puede ser motivo de anulación del proyecto. Además, como la presentación exige responder preguntas de manera aleatoria a cualquier integrante, todos deben entender las 4 partes antes de exponer. Tienen plazo para subir todo esto a más tardar el 23 de junio de 2026 a las 11:59h.