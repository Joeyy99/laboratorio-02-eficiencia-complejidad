# Laboratorio 02: eficiencia y complejidad

## El problema

Este laboratorio trata de encontrar qué números se repiten dentro de un arreglo de n enteros. Para resolverlo comparamos dos formas de hacerlo y vimos cuál se comporta mejor cuando el arreglo crece.

El algoritmo A ordena el arreglo de mayor a menor con inserción y después revisa cada elemento contra su vecino, porque si hay repetidos van a quedar uno al lado del otro. El algoritmo B no ordena nada: toma cada valor, busca sus copias más adelante en el arreglo y las va tachando para no volver a contarlas.

## Hipótesis

Antes de correr el código pensamos que los dos iban a ser cuadráticos, porque A usa inserción (que tiene dos ciclos anidados) y B también tiene un ciclo dentro de otro. Entonces, si n se multiplica por 10, esperábamos que las operaciones y el tiempo se multiplicaran más o menos por 100 en ambos.

También pensamos que B iba a hacer menos operaciones que A, ya que al tachar las copias se evita revisar otra vez valores que ya se contaron, mientras que A tiene que mover elementos para ordenar y después recorrer todo de nuevo.

## Cómo hicimos las pruebas

Usamos Python 3 desde la terminal de VS Code en una MacBook. Probamos con n = 100 y n = 1000, y los arreglos se llenaron con números aleatorios entre 1 y n. Para que la comparación fuera justa, los arreglos se generan una sola vez por cada tamaño y los dos algoritmos trabajan con exactamente los mismos datos. También dejamos la semilla fija en 42, así los números salen iguales cada vez que se corre el programa.

Cada medición se repitió 3 veces y se sacó el promedio del tiempo. Además de medir el tiempo, contamos operaciones dentro del código. En A contamos las comparaciones y asignaciones del ordenamiento más las comparaciones entre vecinos. En B contamos las veces que se revisa si un elemento está tachado, las comparaciones entre datos y las marcas de tachado. Al final el programa también verifica que A y B encuentren los mismos repetidos, y en ningún caso salió advertencia.

## Resultados

Esto fue lo que salió en la terminal (la captura está en la carpeta `results`):

| Algoritmo | n | Operaciones | Tiempo (ms) | Repetidos |
|-----------|-----:|------------:|------------:|----------:|
| A | 100 | 5.501 | 0,890 | 28 |
| A | 1.000 | 513.880 | 127,947 | 271 |
| B | 100 | 3.564 | 0,523 | 28 |
| B | 1.000 | 367.130 | 66,098 | 271 |

Los dos algoritmos encontraron la misma cantidad de repetidos (28 y 271), lo cual nos dice que ambos están bien implementados.

## Conclusiones

Lo primero que notamos es que los dos crecen de forma cuadrática. Al pasar de 100 a 1000 elementos, las operaciones de A se multiplicaron por unas 93 veces y las de B por unas 103, o sea, cerca de 100 como habíamos supuesto. Si fueran lineales solo se habrían multiplicado por 10.

Lo segundo es que B salió mejor que A en esta prueba. Con n = 1000, B hizo 367.130 operaciones contra 513.880 de A, y tardó 66 ms contra casi 128 ms. Creemos que se debe al tachado: con números aleatorios entre 1 y 1000 el arreglo solo tiene 637 valores distintos, así que 363 elementos se tachan y B no tiene que recorrerlos como valor base.

Eso sí, esta ventaja depende de los datos. Si casi no hubiera repetidos, B haría cerca de 500.000 operaciones, parecido a lo de A. Además, solo probamos dos tamaños y con 3 repeticiones, así que los resultados sirven como una buena indicación pero no como una prueba definitiva. En `analysis.md` explicamos esto con más detalle.

## Contenido del repositorio

- `README.md`: este documento.
- `analysis.md`: la interpretación de los resultados y por qué escala cada algoritmo como lo hace.
- `src/comparacion_algoritmos.py`: el código con los dos algoritmos y el conteo de operaciones.
- `results/`: la tabla en Excel, la tabla en texto y la captura de la ejecución.

Para correrlo basta con ejecutar `python3 src/comparacion_algoritmos.py`. Las operaciones y los repetidos deberían salir idénticos porque la semilla es fija, pero los tiempos cambian según el computador.


## Autores

- Joel Matias Tapa Tamayo
- Luis David Dueñas Flores

Noviembre de 2026
