import numpy as np
import pandas as pd

df = pd.read_csv("dataset_mundial_2026.csv")

# solo columnas numericas (las 6 features)
num = df.select_dtypes(include=[np.number])
X = num.values.astype(float)

# estandarizar (media 0, desviacion 1)
mu = X.mean(axis=0)
sigma = X.std(axis=0, ddof=0)
sigma[sigma == 0] = 1.0  # evitar division por cero
X_std = (X - mu) / sigma

n = X_std.shape[0]

# matriz de covarianza por multiplicacion de matrices
cov = (X_std.T @ X_std) / (n - 1)

# autovalores y autovectores 
autovalores, autovectores = np.linalg.eig(cov)

# eig puede devolver complejos por error numerico
autovalores = autovalores.real
autovectores = autovectores.real

# ordenar de MAYOR a MENOR
orden = np.argsort(autovalores)[::-1]
autovalores = autovalores[orden]
autovectores = autovectores[:, orden]

# tomar los 2 componentes principales y proyectar
W = autovectores[:, :2]          # (6 x 2)
proy = X_std @ W                 # (n x 2)

# guardar resultados
out = pd.DataFrame(proy, columns=["PC1", "PC2"])
out.to_csv("resultados_pca_2d.csv", index=False)

var_total = autovalores.sum()
var_exp = autovalores[:2] / var_total * 100
print("Autovalores (ordenados):", np.round(autovalores, 4))
print(f"Varianza explicada PC1: {var_exp[0]:.2f}%  PC2: {var_exp[1]:.2f}%")
print(f"Acumulada (PC1+PC2): {var_exp.sum():.2f}%")
print("resultados_pca_2d.csv", proy.shape)
