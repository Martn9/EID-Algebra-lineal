"""
analisis_varianza.py
Responsable: Deris Aranquiz
Proyecto: PCA Mundial 2026
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("Cargando datos...")

# 1. Cargar los datos originales y los resultados de Martin L.
dataset = pd.read_csv("dataset_mundial_2026.csv")
# Le decimos a pandas que ignore todo lo que esté después de un '#'
pca_2d = pd.read_csv("resultados_pca_2d.csv", comment='#')

# Leer los autovalores que calculó Martin L.
# (Martin L. debe exportar un archivo autovalores.csv)
autovalores_df = pd.read_csv("autovalores.csv")
autovalores = autovalores_df["Autovalores"].values

# 2. Cálculos simples para el gráfico de barras (Scree Plot)
var_total = sum(autovalores)
var_exp_pct = [(i / var_total) * 100 for i in autovalores]
var_acum_pct = np.cumsum(var_exp_pct)

# ==========================================
# GRÁFICO 1: Scatter Plot 2D (Todos los países en Positivo)
# ==========================================
print("Generando Scatter Plot 2D de todos los países...")

# Creamos un lienzo un poco más grande para que quepan bien los 48 textos
fig, ax = plt.subplots(figsize=(13, 9))

# Líneas de referencia en el centro (coordenada 0,0)
ax.axhline(0, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)
ax.axvline(0, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)

# Pasamos el PC1 a positivo multiplicando por -1. El PC2 lo dejamos igual.
PC1_positivo = pca_2d["PC1"].values * -1
PC2_original = pca_2d["PC2"].values

# Dibujamos todos los puntos en el mapa
ax.scatter(PC1_positivo, PC2_original, color='blue', s=50, edgecolors='black', alpha=0.7, zorder=3)

# Ciclo simple para ponerle el nombre a TODOS los 48 países sin excepción
paises = dataset["Pais"].tolist()
for i in range(len(paises)):
    # Ponemos el texto un poquito desplazado (+0.08) para que no tape el punto azul
    ax.text(PC1_positivo[i] + 0.08, PC2_original[i] + 0.05, paises[i], fontsize=7, alpha=0.85)

# Títulos y nombres de los ejes
ax.set_title("PCA - Mapa de Proyección de las 48 Selecciones (Mundial 2026)", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("PC1 — Jerarquía General del Equipo (Favoritos a la Derecha)", fontsize=11, labelpad=8)
ax.set_ylabel("PC2 — Volatilidad Ofensiva/Defensiva (Anomalías de Goles)", fontsize=11, labelpad=8)
ax.grid(True, linestyle=':', alpha=0.5, zorder=0)

# Guardamos la imagen en alta definición (dpi=300) para que no se pixele al imprimir
plt.tight_layout()
plt.savefig("scatter_pca_mundial2026.png", dpi=300, bbox_inches='tight')
plt.show()

print("[OK] Gráfico Scatter Plot guardado en alta resolución.")
# ==========================================
# GRÁFICO 2: Varianza Explicada (Scree Plot)
# ==========================================
plt.figure(figsize=(8, 5))
componentes = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6']

# Gráfico de barras y línea superpuesta simple
plt.bar(componentes, var_exp_pct, color='skyblue', label='Varianza por componente')
plt.plot(componentes, var_acum_pct, color='red', marker='o', label='Varianza Acumulada')

# Poner los porcentajes arriba de los puntos de la línea roja
for i in range(len(componentes)):
    plt.text(i, var_acum_pct[i] + 2, f"{var_acum_pct[i]:.1f}%", ha='center', fontsize=9)

plt.title("Varianza Retenida por el PCA")
plt.xlabel("Componentes Principales")
plt.ylabel("Porcentaje de Varianza (%)")
plt.legend()
plt.grid(True, axis='y', linestyle=':')

plt.savefig("scree_plot.png")
plt.show()

print("Gráficos generados con éxito.")
# ==========================================
# GRÁFICO 3: Probabilidad de Ganar el Mundial (Todos los países)
# ==========================================
print("Generando Ranking de Probabilidades...")

# 1. Invertir el PC1 para que los favoritos tengan el puntaje más alto
puntajes_pca = pca_2d["PC1"] * -1

# 2. Transformación matemática a Probabilidad (Normalización)
# Desplazamos los puntos restando el mínimo para no tener probabilidades negativas
puntajes_positivos = puntajes_pca - puntajes_pca.min()

# Calculamos el porcentaje dividiendo por el total (la suma dará 100%)
probabilidades = (puntajes_positivos / puntajes_positivos.sum()) * 100

# 3. Crear el DataFrame con todos los países
df_ranking = pd.DataFrame({
    "Pais": dataset["Pais"],
    "Probabilidad": probabilidades
})

# Ordenamos de mayor a menor probabilidad
df_ranking = df_ranking.sort_values(by="Probabilidad", ascending=False)

# 4. Generar el gráfico
# Usamos un gráfico muy alto (10x12) para que quepan los 48 países cómodamente
plt.figure(figsize=(10, 12))

# Graficamos todas las barras (invertidas con [::-1] para que el 1° quede arriba)
barras = plt.barh(df_ranking["Pais"][::-1], df_ranking["Probabilidad"][::-1], color='#1a9e3f')

# Ajustes estéticos
plt.title("Probabilidad Matemática de Ganar el Mundial 2026\n(Basado en Análisis de Componentes Principales)", fontsize=14, fontweight='bold')
plt.xlabel("Probabilidad (%)", fontsize=12)
plt.xlim(0, df_ranking["Probabilidad"].max() + 1) # Dar un poco de espacio a la derecha
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Agregar el numerito del porcentaje al final de cada barra
for index, value in enumerate(df_ranking["Probabilidad"][::-1]):
    plt.text(value + 0.1, index, f"{value:.1f}%", va='center', fontsize=8)

plt.tight_layout()
plt.savefig("probabilidad_mundial_todos.png", bbox_inches='tight')
plt.show()

print("¡Gráfico de probabilidades generado con éxito!")