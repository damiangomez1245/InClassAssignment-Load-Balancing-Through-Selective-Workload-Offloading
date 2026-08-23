GREEDY HEURISTIC
- Comandos necesarios: python runner.py
- Lenguaje y version: python 3.10+
- Dependencias y versiones: Módulos estándar de Python (typing, time, statistics). Para la generación de gráficas a nivel general se requerirá matplotlib (v3.7+).
- Instrucciones para ejecutar la prueba de rendimiento: Ejecutar el comando principal en la terminal. El script aislará la función greedy_heuristic pasándole los Workloads C1 y C2 con las capacidades definidas (20 a 140) y el caso extremo (W=0).
- Instrucciones para generar las figuras: Al terminar el ciclo de pruebas en el runner, el script recopilará los tiempos del método Greedy y los graficará automáticamente comparándolos con el resto.
- numero de repeticiones utilizadas: 5 repeticiones por cada capacidad de W. Se reportará la mediana del tiempo en milisegundos.
- reglas de desempate deterministas: Al ordenar los trabajos, se evaluan en este orden: Mayor ratio de beneficio por costo en orden descendente, menor costo de migracion en orden ascendente, orden alfabetico del id del trabajo en orden ascendente
- cualquier semilla aleatoria fija si se utiliza con aleatoridad: No aplica. El algoritmo no utiliza números aleatorios; es 100% determinista.
- Archivos y directoris de salida separados: Los tiempos de ejecución y selecciones del método Greedy se añadirán al archivo general benchmark_results.csv y sus tiempos se visualizarán en runtime_vs_capacity_C1.png y runtime_vs_capacity_C2.png

OPTIMAL DYNAMIC PROGRAMMING
-Código: Dynamic Programming
-Version: Python 3.13.6
-Commandos para correr el código:
    python .\main.py
-Dependencias y versiones: Módulos estándar de Python (typing, time, statistics). Para la generación de gráficas a nivel general se requerirá matplotlib (v3.7+).
-Instrucciones para correr el código:
    -Verificiar que los datos que quieras poner estan puestos en main.py
    -si se desea cambiarlos tienes que cambiar las siguientes variables
        -workload_name (Aunque este es opcional) (línea: 9)
        -cost_lookup luego de "for job in" (línea: 36)
        -greedy_gap para que use v_greedy_XX[i] (línea: 70)
    -también se puede cambiar el rango de las veces que se puede correr en "for i in range(X)" (línea: 54)
-Instruccioens para la generación de figuras:
    -las figuras ya están programadas en el main.py
    -solo basta con correr el código
    -se pueden cambiar los valores de v_greedy_XX por las que tu quieras (línea: 40-41)
-Número de repeticiones: 5 repeticiones por valor W, se determina el tiempo de cada una
-Reglas de desempate deterministas: Al ordenar los trabajos, se evaluan en este orden: Mayor ratio de beneficio por costo en orden descendente, menor costo de migracion en orden ascendente, orden alfabetico del id del trabajo en orden ascendente
-cualquier semilla aleatoria fija si se utiliza con aleatoridad: No aplica. El algoritmo no utiliza números aleatorios; es 100% determinista.
-Archivos y directoris de salida separados: La definición del código de resolución dynamic_programing.py está por separado a la que muestra tanto las gráficas como valores resultantes main.py


EXACT BRANCH-AND-BOUND
- Comandos necesarios
- Lenguaje y version:
- Dependencias y versiones:
- Instrucciones para ejecutar la prueba de rendimiento:
- Instrucciones para generar las figuras
- numero de repeticiones utilizadas:
- reglas de desempate deterministas:
- cualquier semilla aleatoria fija si se utiliza con aleatoridad: 
- Archivos y directoris de salida separados: