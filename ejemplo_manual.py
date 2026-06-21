import numpy as np


def cargar_datos():
    """Matriz inventada 3x2 con variables CORRELACIONADAS.

    Se eligen datos correlacionados a proposito: asi la covarianza tiene
    terminos fuera de la diagonal y los autovectores resultan ser ejes
    NUEVOS (rotados ~45 grados), no las columnas originales. Eso es lo que
    realmente demuestra PCA: los componentes son combinaciones lineales
    de las variables originales.
    """
    return np.array([
        [2.0, 1.0],
        [3.0, 3.0],
        [4.0, 2.0],
    ])


def centrar(D):
    """Resta la media de cada columna -> matriz centrada en el origen."""
    medias = np.mean(D, axis=0)
    return D - medias, medias


def covarianza(X_centrada):
    """Sigma = (X^T @ X) / (n - 1). Misma formula que motor_pca.py."""
    n = X_centrada.shape[0]
    return (X_centrada.T @ X_centrada) / (n - 1)


def descomponer(Sigma):
    """Autovalores/autovectores ordenados de MAYOR a menor varianza."""
    autovalores, autovectores = np.linalg.eig(Sigma)
    orden = np.argsort(autovalores)[::-1]
    return autovalores[orden], autovectores[:, orden]


def validacion_teorica_pca():
    print("=" * 50)
    print("   VALIDACION TEORICA: PCA MANUAL")
    print("=" * 50, "\n")

    # NOTA: este ejemplo solo CENTRA (no estandariza) porque las 2 variables
    # estan en la misma escala. La estandarizacion Z-score es obligatoria en
    # el dataset real (motor_pca.py) porque ahi se mezclan euros con goles.
    D = cargar_datos()
    print("Paso 1: Matriz de Datos Originales (D)")
    print(D, "\n")

    X, medias = centrar(D)
    print(f"Medias por columna: mu_X = {medias[0]}, mu_Y = {medias[1]}")
    print("\nPaso 2: Matriz Centrada (X = D - medias)")
    print(X, "\n")

    n = X.shape[0]
    Sigma = covarianza(X)
    print("Paso 3: Matriz de Covarianza (Sigma)")
    print(f"Sigma = (X^T @ X) / (n - 1)  con  n - 1 = {n - 1}")
    print(Sigma, "\n")

    autovalores, autovectores = descomponer(Sigma)
    var_total = autovalores.sum()

    print("Paso 4: Autovalores y Autovectores (ordenados)")
    for i, lam in enumerate(autovalores):
        vec = np.round(autovectores[:, i], 2)
        vec[vec == -0.0] = 0.0  # evita el "-0." en la impresion
        porcentaje = lam / var_total * 100
        print(f"Componente Principal {i + 1}:")
        print(f"  Autovalor (varianza)   = {lam:.2f}  ({porcentaje:.1f}% del total)")
        print(f"  Autovector (direccion) = {vec}\n")

    print("=" * 50)
    print("Calculo finalizado. Debe coincidir con el desarrollo")
    print("matematico manual del Marco Teorico en LaTeX.")
    print("=" * 50)


if __name__ == "__main__":
    validacion_teorica_pca()
