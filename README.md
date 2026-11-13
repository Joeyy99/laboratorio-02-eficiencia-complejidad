# Laboratorio 02: Eficiencia y complejidad algorítmica

Comparación experimental de dos algoritmos que resuelven el mismo problema: **detectar elementos repetidos en un arreglo de números enteros**. Para cada algoritmo se mide el número de operaciones y el tiempo de ejecución con distintos tamaños de entrada (n).

- **Curso:** Algoritmos - Eficiencia y complejidad algorítmica
- **Universidad:** Universidad Central del Ecuador - Facultad de Ingeniería y Ciencias Aplicadas
- **Lenguaje:** Python

## Algoritmos comparados

### Algoritmo A: ordenar y comparar vecinos
1. Ordena una copia del arreglo de **mayor a menor** con ordenamiento por inserción.
2. Recorre el arreglo ordenado comparando cada elemento con el anterior. Como los duplicados quedan uno al lado del otro, si dos vecinos son iguales ese dato se repitió.

Operaciones contadas: comparaciones y asignaciones del ordenamiento, y comparaciones entre vecinos.

### Algoritmo B: contar y tachar
1. Toma el primer valor que no esté tachado y busca sus copias en las posiciones siguientes.
2. Cada copia encontrada se **tacha** (se marca) para no revisarla otra vez.
3. Si el valor tuvo al menos una copia, se reporta como repetido.

Operaciones contadas: verificaciones de tachado, comparaciones entre datos y marcas de tachado.

## Requisitos

- **Python 3.8 o superior.** No se necesita instalar ninguna librería: el programa solo usa los módulos `random` y `time`, que vienen incluidos con Python.

Para comprobar que Python está instalado:

```bash
python3 --version
```

En Windows puede ser:

```bash
python --version
```

## Cómo ejecutar el proyecto

### 1. Obtener el código

Con Git:

```bash
git clone https://github.com/Joeyy99/Eficiencia-Algoritmica-Tapa-Duenas.git
cd Eficiencia-Algoritmica-Tapa-Duenas
```

O descargar el repositorio como ZIP desde GitHub (**Code → Download ZIP**), descomprimirlo y abrir una terminal dentro de la carpeta.

### 2. Ejecutar el programa

Desde la carpeta raíz del repositorio:

**macOS / Linux**

```bash
python3 src/comparacion_algoritmos.py
```

**Windows (PowerShell o CMD)**

```bash
python src/comparacion_algoritmos.py
```

Si `python` no funciona en Windows, probar con `py src/comparacion_algoritmos.py`.

### 3. Qué se debe ver

El programa genera los arreglos, ejecuta ambos algoritmos y muestra una tabla como esta:

```
Algoritmos:
  A = Ordenar + vecinos
  B = Contar y tachar
Mediciones: promedio de 3 repeticiones | semilla = 42

Algoritmo        n   operaciones        tiempo   repetidos
----------------------------------------------------------
A              100         5.501      0.195 ms          28
A            1.000       513.880     23.277 ms         271
B              100         3.564      0.117 ms          28
B            1.000       367.130     16.694 ms         271
```

Los valores de **operaciones** y **repetidos** son siempre los mismos, porque los datos se generan con una semilla fija. El **tiempo** cambia en cada ejecución y depende del computador.

## Cómo funciona la comparación

- **Mismos datos para ambos algoritmos:** los arreglos se generan una sola vez por tamaño y A y B trabajan con exactamente los mismos, para que la comparación sea justa.
- **Tres repeticiones:** cada medición se repite 3 veces y el tiempo reportado es el promedio.
- **Verificación:** el programa comprueba que A y B encuentren los mismos datos repetidos y avisa si no coinciden (columna `repetidos`).
- **Medición sin impresión:** no se imprime nada mientras corre el cronómetro, para no alterar el tiempo.

## Parámetros configurables

Al inicio de `src/comparacion_algoritmos.py` se pueden cambiar:

| Parámetro | Valor por defecto | Descripción |
|---|---|---|
| `TAMANOS` | `[100, 1000]` | Tamaños de entrada (n) a probar |
| `REPETICIONES` | `3` | Veces que se repite cada medición |
| `SEMILLA` | `42` | Semilla del generador aleatorio, para que los datos sean reproducibles |

Con `TAMANOS = [100, 1000, 10000]` el algoritmo A tardará varios segundos en el último tamaño.

## Estructura del repositorio

```
.
├── README.md        Este archivo
├── analysis.md      Análisis de los resultados
├── src/
│   └── comparacion_algoritmos.py    Programa que compara los algoritmos A y B
└── results/         Capturas y tablas de las ejecuciones
```

## Autores

- Joel Matias Tapa Tamayo
- Luis David Dueñas Flores

Noviembre de 2026
