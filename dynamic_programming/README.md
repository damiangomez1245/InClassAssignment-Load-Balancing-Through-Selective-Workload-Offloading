Código: Dynamic Programming

Version: Python 3.13.6

Commandos para correr el código:
    python .\main.py

Dependencias y versiones: Módulos estándar de Python (typing, time, statistics). Para la generación de gráficas a nivel general se requerirá matplotlib (v3.7+).

Instrucciones para correr el código:
    -Verificiar que los datos que quieras poner estan puestos en main.py
    -si se desea cambiarlos tienes que cambiar las siguientes variables
        -workload_name (Aunque este es opcional) (línea: 9)
        -cost_lookup luego de "for job in" (línea: 36)
        -greedy_gap para que use v_greedy_XX[i] (línea: 70)
    -también se puede cambiar el rango de las veces que se puede correr en "for i in range(X)" (línea: 54)

Instruccioens para la generación de figuras:
    -las figuras ya están programadas en el main.py
    -solo basta con correr el código
    -se pueden cambiar los valores de v_greedy_XX por las que tu quieras (línea: 40-41)

Número de repeticiones: 5

deterministic tie-breaking rules;
any fixed random seeds, if randomness is used;
expected output files and directories.
A grader should be able to reproduce the complete experiment and all figures by following only the README.
