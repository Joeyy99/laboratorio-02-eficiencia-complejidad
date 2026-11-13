# Análisis: ¿cuál escala mejor y por qué?

## Qué pasó con los números

Si miramos cuánto creció cada algoritmo al pasar de n = 100 a n = 1000 (es decir, 10 veces más datos), las operaciones de A se multiplicaron por 93,4 y las de B por 103. El tiempo creció todavía más: 143,8 veces en A y 126,4 veces en B. Si pensamos que el costo es algo como n elevado a un exponente, esos factores dan exponentes de más o menos 2 en las operaciones (1,97 para A y 2,01 para B), y un poco más de 2 en el tiempo. Con eso queda claro que ambos son cuadráticos.

## Por qué A es cuadrático

El ordenamiento por inserción toma cada elemento y lo va moviendo hacia atrás hasta encontrar su lugar. Cuando los datos están desordenados, casi la mitad de los pares están "al revés" (en promedio n(n-1)/4 pares), y cada uno de esos pares cuesta una comparación y un desplazamiento. Entonces el trabajo total queda cerca de n²/2.

Lo comprobamos con los datos: para n = 100, n²/2 es 5.000 y medimos 5.501, y para n = 1000 es 500.000 y medimos 513.880. La diferencia pequeña viene de la parte lineal del algoritmo y de que los datos son aleatorios. La revisión de vecinos solo hace n-1 comparaciones, así que casi no se nota al lado del ordenamiento.

Algo interesante es que A no siempre es cuadrático. Probamos aparte con un arreglo que ya venía ordenado de mayor a menor y con n = 1000 hizo apenas 3.996 operaciones. Con el arreglo ordenado al revés (de menor a mayor) subió a 1.001.997. Entonces A depende mucho del orden en que llegan los datos.

## Por qué B es cuadrático

B tiene un ciclo que recorre el arreglo y, para cada elemento que no está tachado, otro ciclo que busca copias hacia adelante. En el peor caso, que sería no tener ningún repetido, nada se tacha y las comparaciones son (n-1) + (n-2) + ... + 1, que da n(n-1)/2. Sumando las verificaciones queda n(n+1)/2, es decir, 500.500 para n = 1000. Probamos aparte un arreglo sin repetidos y salió justo ese número.

Cuando sí hay repetidos, cada elemento tachado se salta su recorrido, y por eso en nuestra prueba B hizo 367.130 operaciones y no 500.500. En el extremo, si todos los valores fueran iguales, B casi no tendría que hacer nada (2.998 operaciones con n = 1000), porque tacha todo en la primera pasada.

## Entonces, ¿cuál escala mejor?

En la práctica, con estos datos, B fue mejor. Hizo un 28,6 % menos de operaciones y tardó casi la mitad del tiempo en n = 1000 (A tardó 1,94 veces más).

Hay un detalle que nos llamó la atención. A hizo 1,40 veces más operaciones que B, pero tardó 1,94 veces más. Eso significa que las operaciones de A son más "caras". Con n = 1000, A gastó unos 0,249 microsegundos por operación y B unos 0,180. Nuestra idea es que en A muchas de las operaciones son asignaciones sobre la lista (los desplazamientos), mientras que en B casi todo son comparaciones, y en Python no cuestan lo mismo. Pero esto es una suposición, porque el experimento no está diseñado para comprobarlo.

Tampoco podemos decir que B siempre sea mejor. Su ventaja viene de que hay duplicados que tachar. Si los datos casi no tuvieran repetidos, B quedaría muy parecido a A, y si el arreglo viniera ya ordenado, A sería lineal y le ganaría a B.

## Limitaciones

Hay varias cosas que hay que tener en cuenta antes de sacar conclusiones fuertes:

Solo usamos dos tamaños. Con dos puntos se puede calcular un exponente, pero no se puede confirmar que la curva sea de verdad n². Lo ideal sería probar más tamaños, por ejemplo 100, 500, 1000, 2000 y 5000.

Solo hicimos 3 repeticiones por medición. Con n = 100 el tiempo es menor a 1 ms, así que cualquier cosa que esté haciendo el computador en ese momento afecta bastante. Creemos que por eso los exponentes de tiempo (2,16 y 2,10) salieron un poco por encima de los de operaciones (1,97 y 2,01), que son más confiables porque se cuentan dentro del código y no cambian de una corrida a otra.

Además, usamos una sola semilla y un solo tipo de datos. Como el resultado de B depende de cuántos repetidos haya, habría que probar con otras cantidades de duplicados. Y por último, "operación" no significa lo mismo en A que en B, así que comparar los conteos entre algoritmos es solo orientativo. Lo que es más sólido es ver cómo crece cada uno por separado.

## Conclusión

Los dos algoritmos son cuadráticos, y en nuestras pruebas B resultó más rápido y con menos operaciones gracias al tachado, aunque esa ventaja depende de que haya números repetidos y no cambia el orden de crecimiento. Para asegurar esto en general habría que probar con más tamaños y más tipos de datos.

Como comentario extra, existen formas mucho mejores de resolver este problema, como usar un `set` o un diccionario en Python, que lo hace en tiempo lineal, o usar `sorted()` en lugar de inserción. No las incluimos porque el laboratorio pedía comparar estas dos estrategias en particular, las cuales fueron ideadas por nosotros mismos sabiendo que podían ser cualesquiera siempre que resuelvan el problema.
