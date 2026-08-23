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
- Comandos necesarios
- Lenguaje y version:
- Dependencias y versiones:
- Instrucciones para ejecutar la prueba de rendimiento:
- Instrucciones para generar las figuras
- numero de repeticiones utilizadas:
- reglas de desempate deterministas:
- cualquier semilla aleatoria fija si se utiliza con aleatoridad: 
- Archivos y directoris de salida separados:

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