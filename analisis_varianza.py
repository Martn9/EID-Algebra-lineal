"""
analisis_varianza.py
Responsable: Deris Aranquiz — Analista de Varianza y Compilador
Proyecto: Visualización y Reducción Dimensional de Datos utilizando PCA
         Mundial 2026 · Álgebra Lineal · EID

DESCRIPCIÓN GENERAL:
    Este script lee los resultados del motor PCA (resultados_pca_2d.csv) y el
    dataset original (dataset_mundial_2026.csv) para producir dos gráficos:

    1. Scatter Plot 2D — Cada selección proyectada sobre (PC1, PC2).
       · PC1 (eje X): Combinación lineal de todas las métricas que captura
         la "jerarquía general" de un equipo (62.4 % de la varianza).
       · PC2 (eje Y): Captura principalmente la "volatilidad ofensiva/defensiva"
         (18.16 % de varianza adicional).
       Los ejes NO son variables directas; son combinaciones lineales de las
       6 variables originales calculadas por numpy.linalg.eig en motor_pca.py.

    2. Scree Plot — Gráfico de barras que muestra qué porcentaje de
       información retiene cada componente principal.

IMPORTANTE: Los autovalores se recalculan EXACTAMENTE igual que en motor_pca.py
(misma fórmula, mismo orden) para garantizar coherencia entre scripts.
NO se usa scikit-learn en ningún paso.

Archivos de entrada:
    · resultados_pca_2d.csv   → generado por motor_pca.py
    · dataset_mundial_2026.csv → generado por carga_exploracion.py

Archivos de salida:
    · scatter_pca_mundial2026.png
    · scree_plot_varianza.png
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ─────────────────────────────────────────────────────────────────────────────
# 0. CONFIGURACIÓN VISUAL GLOBAL
# ─────────────────────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 150,
})

# ─────────────────────────────────────────────────────────────────────────────
# 1. CARGA DE DATOS
# ─────────────────────────────────────────────────────────────────────────────
print("=" * 60)
print("   ANÁLISIS DE VARIANZA — PCA MUNDIAL 2026")
print("=" * 60)

try:
    pca_2d  = pd.read_csv("resultados_pca_2d.csv")
    dataset = pd.read_csv("dataset_mundial_2026.csv")
    print("[OK] Archivos cargados correctamente.")
except FileNotFoundError as e:
    print(f"\n[ERROR] Archivo no encontrado: {e}")
    print("  → Asegúrate de haber ejecutado primero:")
    print("      python carga_exploracion.py")
    print("      python motor_pca.py")
    raise SystemExit(1)

paises = dataset["Pais"].tolist()
PC1    = pca_2d["PC1"].values
PC2    = pca_2d["PC2"].values

if len(paises) != len(PC1):
    print(f"[ERROR] El dataset tiene {len(paises)} países pero PCA tiene {len(PC1)} filas.")
    raise SystemExit(1)

print(f"[OK] Selecciones cargadas: {len(paises)} equipos / {pca_2d.shape[1]} componentes.\n")

# ─────────────────────────────────────────────────────────────────────────────
# 2. RECÁLCULO DE VARIANZA EXPLICADA
#    Se usa exactamente la misma lógica que motor_pca.py para que los
#    porcentajes del Scree Plot sean coherentes con los del motor.
# ─────────────────────────────────────────────────────────────────────────────
num = dataset.select_dtypes(include=[np.number]).values.astype(float)
mu    = num.mean(axis=0)
sigma = num.std(axis=0, ddof=0)
sigma[sigma == 0] = 1.0          # evitar división por cero (igual que motor_pca)
X_std = (num - mu) / sigma

n   = X_std.shape[0]
cov = (X_std.T @ X_std) / (n - 1)   # matriz de covarianza por multiplicación

autovalores, _ = np.linalg.eig(cov)
autovalores     = autovalores.real
autovalores     = np.sort(autovalores)[::-1]   # mayor → menor

var_total    = autovalores.sum()
var_exp_pct  = (autovalores / var_total) * 100
var_acum_pct = np.cumsum(var_exp_pct)

n_comp = len(autovalores)   # 6 componentes
print("Varianza explicada por componente:")
for i in range(n_comp):
    print(f"  PC{i+1}: {var_exp_pct[i]:6.2f}%   (acumulada: {var_acum_pct[i]:6.2f}%)")
print()

# ─────────────────────────────────────────────────────────────────────────────
# 3. CONFIGURACIÓN DE COLORES POR CONFEDERACIÓN
#    Asignar una confederación a cada país según el orden de carga_exploracion.py
# ─────────────────────────────────────────────────────────────────────────────
CONF_COLORES = {
    "CONMEBOL": "#1a9e3f",   # verde
    "UEFA":     "#1565c0",   # azul
    "CONCACAF": "#e65100",   # naranja
    "AFC":      "#6a1b9a",   # morado
    "CAF":      "#b71c1c",   # rojo
    "OFC":      "#795548",   # marrón
}

# Cada selección tiene exactamente la confederación correspondiente
# (mismo orden que datos_oficiales en carga_exploracion.py)
conf_por_pais = {
    # CONMEBOL (6)
    "Argentina": "CONMEBOL", "Brasil": "CONMEBOL", "Colombia": "CONMEBOL",
    "Ecuador": "CONMEBOL", "Paraguay": "CONMEBOL", "Uruguay": "CONMEBOL",
    # UEFA (16)
    "Alemania": "UEFA", "Austria": "UEFA", "Belgica": "UEFA",
    "Bosnia y Herzegovina": "UEFA", "Croacia": "UEFA", "Chequia": "UEFA",
    "Escocia": "UEFA", "Espana": "UEFA", "Francia": "UEFA",
    "Inglaterra": "UEFA", "Noruega": "UEFA", "Paises Bajos": "UEFA",
    "Portugal": "UEFA", "Suecia": "UEFA", "Suiza": "UEFA", "Turkiye": "UEFA",
    # CONCACAF (6)
    "Canada": "CONCACAF", "Curazao": "CONCACAF", "Estados Unidos": "CONCACAF",
    "Haiti": "CONCACAF", "Mexico": "CONCACAF", "Panama": "CONCACAF",
    # AFC (9)
    "Arabia Saudita": "AFC", "Australia": "AFC", "Corea del Sur": "AFC",
    "Iran": "AFC", "Irak": "AFC", "Japon": "AFC",
    "Jordania": "AFC", "Qatar": "AFC", "Uzbekistan": "AFC",
    # CAF (10)
    "Argelia": "CAF", "Cabo Verde": "CAF", "Costa de Marfil": "CAF",
    "Egipto": "CAF", "Ghana": "CAF", "Marruecos": "CAF",
    "Republica Democratica del Congo": "CAF", "Senegal": "CAF",
    "Sudafrica": "CAF", "Tunez": "CAF",
    # OFC (1)
    "Nueva Zelanda": "OFC",
}

colores = [CONF_COLORES[conf_por_pais[p]] for p in paises]

# Países con etiqueta visible (los más extremos o relevantes en el scatter)
ETIQUETAS_DESTACADAS = {
    "Argentina", "Brasil", "Francia", "Espana", "Inglaterra",
    "Alemania", "Portugal", "Japon", "Marruecos", "Senegal",
    "Canada", "Estados Unidos", "Mexico", "Qatar", "Nueva Zelanda",
    "Irak", "Jordania", "Curazao"
}

# ─────────────────────────────────────────────────────────────────────────────
# 4. GRÁFICO 1 — SCATTER PLOT 2D
# ─────────────────────────────────────────────────────────────────────────────
print("[...] Generando Scatter Plot...")

fig, ax = plt.subplots(figsize=(14, 9))

# Líneas de referencia en cero (cuadrantes conceptuales)
ax.axhline(0, color='gray', linewidth=0.8, linestyle='--', alpha=0.6)
ax.axvline(0, color='gray', linewidth=0.8, linestyle='--', alpha=0.6)

# Dibujar puntos
scatter = ax.scatter(PC1, PC2, c=colores, s=70, edgecolors='white',
                     linewidths=0.6, alpha=0.92, zorder=3)

# Etiquetas solo para los países destacados
for i, pais in enumerate(paises):
    if pais in ETIQUETAS_DESTACADAS:
        offset_x = 0.06
        offset_y = 0.06
        # Ajuste manual para evitar superposición en casos puntuales
        if pais == "Argentina":
            offset_y = 0.12
        elif pais == "Francia":
            offset_x = 0.06
            offset_y = -0.15
        elif pais == "Espana":
            offset_y = 0.12
        elif pais == "Nueva Zelanda":
            offset_x = -1.2
            offset_y = 0.12
        ax.annotate(
            pais,
            xy=(PC1[i], PC2[i]),
            xytext=(PC1[i] + offset_x, PC2[i] + offset_y),
            fontsize=7.5,
            color='#1a1a2e',
            fontweight='bold',
            ha='left',
        )

# Leyenda de confederaciones
leyenda = [
    mpatches.Patch(color=color, label=conf)
    for conf, color in CONF_COLORES.items()
]
ax.legend(handles=leyenda, title="Confederación", title_fontsize=9,
          fontsize=8, loc='lower left', framealpha=0.9)

# Títulos y etiquetas de ejes
ax.set_xlabel(
    f"PC1 — Jerarquía General del Equipo  ({var_exp_pct[0]:.1f}% varianza)\n"
    r"[Combinación lineal: +Puntos FIFA, +Valor Mercado, +%Victorias, +GF, −GC, +Ligas Top]",
    fontsize=10, labelpad=10
)
ax.set_ylabel(
    f"PC2 — Volatilidad Ofensiva/Defensiva  ({var_exp_pct[1]:.1f}% varianza)\n"
    r"[Combinación lineal: +Puntos FIFA, +Valor, −%Victorias, −GF, −GC]",
    fontsize=10, labelpad=10
)
ax.set_title(
    "PCA — Proyección de las 48 Selecciones del Mundial 2026\n"
    f"Varianza total capturada: {var_acum_pct[1]:.1f}%  (PC1 + PC2)",
    fontsize=14, fontweight='bold', pad=15
)

# Anotación explicativa sobre los ejes
ax.text(0.98, 0.98,
        "NOTA: Los ejes PC1 y PC2 NO son variables originales.\n"
        "Son combinaciones lineales de las 6 métricas del dataset,\n"
        "calculadas mediante autovectores de la matriz de covarianza.",
        transform=ax.transAxes, fontsize=7.5, va='top', ha='right',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow',
                  edgecolor='gray', alpha=0.85))

ax.grid(True, linestyle=':', alpha=0.4, zorder=0)
plt.tight_layout()
plt.savefig("scatter_pca_mundial2026.png", bbox_inches='tight')
print("[OK] Gráfico 'scatter_pca_mundial2026.png' guardado.")
plt.show()

# ─────────────────────────────────────────────────────────────────────────────
# 5. GRÁFICO 2 — SCREE PLOT (Varianza explicada por componente)
# ─────────────────────────────────────────────────────────────────────────────
print("[...] Generando Scree Plot...")

fig2, ax2 = plt.subplots(figsize=(9, 6))

componentes = [f"PC{i+1}" for i in range(n_comp)]
colores_barras = ['#1565c0' if i < 2 else '#90caf9' for i in range(n_comp)]

barras = ax2.bar(componentes, var_exp_pct, color=colores_barras,
                 edgecolor='white', linewidth=1.2, zorder=3)

# Línea de varianza acumulada
ax2_twin = ax2.twinx()
ax2_twin.plot(componentes, var_acum_pct, color='#e65100', marker='o',
              linewidth=2, markersize=7, label='Varianza acumulada', zorder=4)
ax2_twin.set_ylabel("Varianza Acumulada (%)", fontsize=11, color='#e65100')
ax2_twin.tick_params(axis='y', labelcolor='#e65100')
ax2_twin.set_ylim(0, 110)
ax2_twin.axhline(80, color='#e65100', linestyle='--', linewidth=0.8,
                 alpha=0.5)

# Etiqueta de porcentaje sobre cada barra
for barra, pct, acum in zip(barras, var_exp_pct, var_acum_pct):
    ax2.text(barra.get_x() + barra.get_width() / 2,
             barra.get_height() + 0.5,
             f"{pct:.1f}%",
             ha='center', va='bottom', fontsize=9, fontweight='bold',
             color='#1a1a2e')

# Etiqueta de acumulado sobre la línea
for i, acum in enumerate(var_acum_pct):
    ax2_twin.annotate(f"{acum:.1f}%",
                      xy=(i, acum),
                      xytext=(i + 0.08, acum + 2.5),
                      fontsize=8, color='#e65100')

ax2.set_xlabel("Componente Principal", fontsize=11, labelpad=8)
ax2.set_ylabel("Varianza Explicada (%)", fontsize=11)
ax2.set_title(
    "Scree Plot — Varianza Explicada por Componente Principal\n"
    "PCA sin sklearn · Calculado con numpy.linalg.eig",
    fontsize=13, fontweight='bold', pad=12
)
ax2.set_ylim(0, 75)
ax2.grid(True, axis='y', linestyle=':', alpha=0.4, zorder=0)

# Leyenda descriptiva
parche_azul = mpatches.Patch(color='#1565c0', label='PC1 y PC2 seleccionados (retienen 80.6%)')
parche_claro = mpatches.Patch(color='#90caf9', label='PC3–PC6 descartados (19.4% restante)')
linea_naranja = plt.Line2D([0], [0], color='#e65100', marker='o',
                            linewidth=2, label='Varianza acumulada')
ax2.legend(handles=[parche_azul, parche_claro, linea_naranja],
           fontsize=8.5, loc='upper right', framealpha=0.9)

plt.tight_layout()
plt.savefig("scree_plot_varianza.png", bbox_inches='tight')
print("[OK] Gráfico 'scree_plot_varianza.png' guardado.")
plt.show()

# ─────────────────────────────────────────────────────────────────────────────
# 6. RESUMEN FINAL EN CONSOLA
# ─────────────────────────────────────────────────────────────────────────────
print()
print("=" * 60)
print("   RESUMEN DE RESULTADOS")
print("=" * 60)
print(f"  Componentes seleccionados  : PC1 + PC2")
print(f"  Varianza capturada PC1     : {var_exp_pct[0]:.2f}%")
print(f"  Varianza capturada PC2     : {var_exp_pct[1]:.2f}%")
print(f"  Varianza TOTAL retenida    : {var_acum_pct[1]:.2f}%")
print(f"  Varianza descartada (PC3-6): {100 - var_acum_pct[1]:.2f}%")
print()
print("  Interpretación de los ejes:")
print("  PC1 — Alta puntuación FIFA + Valor mercado + %Victorias")
print("        + Goles a favor - Goles en contra + Ligas Top")
print("        → Equipo con mayor PC1 es el favorito general.")
print()
print("  PC2 — Captura diferencial ofensivo/defensivo:")
print("        Equipos con PC2 alto: más goles pero también")
print("        más concedidos (alta volatilidad de marcador).")
print()
print("  Archivos generados:")
print("  · scatter_pca_mundial2026.png")
print("  · scree_plot_varianza.png")
print("=" * 60)
