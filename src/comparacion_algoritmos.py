"""
Laboratorio 02: Benchmarking de algoritmos para detectar elementos repetidos.

Algoritmo A: ordenar de mayor a menor (inserción) y comparar vecinos.
Algoritmo B: contar y tachar (para cada valor, buscar copias adelante y tacharlas).

Para una comparación justa, los arreglos se generan UNA sola vez por tamaño
y los dos algoritmos trabajan exactamente con los mismos datos.
Cada medición se repite REPETICIONES veces y se reporta el tiempo promedio.
"""

import random
import time

# ---------------- Configuración ----------------
TAMANOS = [100, 1000]     # tamaños de entrada (n) a probar
REPETICIONES = 3          # veces que se repite cada medición
SEMILLA = 42              # semilla fija para que los datos sean reproducibles


# ---------------- Algoritmo A: ordenar + vecinos ----------------
def algoritmo_a(datos):
    """Devuelve (repetidos, operaciones). Trabaja sobre una copia de los datos."""
    a = datos.copy()
    comparaciones_orden = 0
    asignaciones_orden = 0
    comparaciones_vecinos = 0

    # Ordenamiento por inserción, de mayor a menor
    for i in range(1, len(a)):
        clave = a[i]
        asignaciones_orden += 1
        j = i - 1

        while j >= 0:
            comparaciones_orden += 1
            if a[j] < clave:
                a[j + 1] = a[j]
                asignaciones_orden += 1
                j -= 1
            else:
                break

        a[j + 1] = clave
        asignaciones_orden += 1

    # Comparar cada elemento con su vecino
    repetidos = []
    for i in range(1, len(a)):
        comparaciones_vecinos += 1
        if a[i] == a[i - 1]:
            if not repetidos or repetidos[-1] != a[i]:
                repetidos.append(a[i])

    operaciones = comparaciones_orden + asignaciones_orden + comparaciones_vecinos
    return repetidos, operaciones


# ---------------- Algoritmo B: contar y tachar ----------------
def algoritmo_b(datos):
    """Devuelve (repetidos, operaciones). No modifica los datos."""
    n = len(datos)
    tachado = [False] * n
    verificaciones_tachado = 0
    comparaciones_datos = 0
    marcas_tachado = 0
    repetidos = []

    for i in range(n):
        verificaciones_tachado += 1
        if tachado[i]:
            continue

        copias = 0
        for j in range(i + 1, n):
            comparaciones_datos += 1
            if datos[j] == datos[i]:
                copias += 1
                tachado[j] = True
                marcas_tachado += 1

        if copias > 0:
            repetidos.append(datos[i])

    operaciones = verificaciones_tachado + comparaciones_datos + marcas_tachado
    return repetidos, operaciones


# ---------------- Medición ----------------
def medir(algoritmo, datos):
    """Ejecuta el algoritmo REPETICIONES veces. Devuelve (repetidos, operaciones, tiempo_ms_promedio)."""
    tiempos = []
    repetidos, operaciones = [], 0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter_ns()
        repetidos, operaciones = algoritmo(datos)
        fin = time.perf_counter_ns()
        tiempos.append((fin - inicio) / 1_000_000)

    return repetidos, operaciones, sum(tiempos) / len(tiempos)


def main():
    random.seed(SEMILLA)

    # Se generan los datasets una sola vez: ambos algoritmos usan los mismos
    datasets = {n: [random.randint(1, n) for _ in range(n)] for n in TAMANOS}

    algoritmos = [
        ("A", "Ordenar + vecinos", algoritmo_a),
        ("B", "Contar y tachar", algoritmo_b),
    ]

    filas = []
    for letra, _, funcion in algoritmos:
        for n in TAMANOS:
            repetidos, operaciones, tiempo_ms = medir(funcion, datasets[n])
            filas.append((letra, n, operaciones, tiempo_ms, set(repetidos)))

    # Verificación: ambos algoritmos deben encontrar los mismos datos repetidos
    for n in TAMANOS:
        conjuntos = [f[4] for f in filas if f[1] == n]
        if any(c != conjuntos[0] for c in conjuntos):
            print(f"ADVERTENCIA: los algoritmos difieren en los repetidos para n = {n}")

    # ---------------- Tabla de resultados ----------------
    print("Algoritmos:")
    for letra, nombre, _ in algoritmos:
        print(f"  {letra} = {nombre}")
    print(f"Mediciones: promedio de {REPETICIONES} repeticiones | semilla = {SEMILLA}")
    print()

    encabezado = f"{'Algoritmo':<10}{'n':>8}{'operaciones':>14}{'tiempo':>14}{'repetidos':>12}"
    print(encabezado)
    print("-" * len(encabezado))
    for letra, n, operaciones, tiempo_ms, repetidos in filas:
        print(f"{letra:<10}{n:>8,}{operaciones:>14,}{tiempo_ms:>11.3f} ms{len(repetidos):>12}"
              .replace(",", "."))


if __name__ == "__main__":
    main()