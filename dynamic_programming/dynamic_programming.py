from typing import List, Tuple
import time
import statistics


def solve_method(
    jobs: List[Tuple[str, str, int, int]], 
    capacity_W: int
) -> Tuple[int, List[str]]:
    
    # Caso borde: Si la capacidad es 0, no podemos migrar nada
    if capacity_W <= 0:
        return (0, [])

    n = len(jobs)

    # 1. "Use a one-dimensional capacity array"
    # DP[c] guardará el mejor alivio que podemos obtener con capacidad c
    DP = [0] * (capacity_W + 1)

    # 2. "Include the bookkeeping required"
    # keep[i][c] será True si decidimos empacar el job 'i' cuando teníamos capacidad 'c'
    # Se inicializa una matriz de n filas por (capacity_W + 1) columnas con False
    keep = [[False] * (capacity_W + 1) for _ in range(n)]

    # Procesamos cada job exactamente una vez
    for i in range(n):
        job_id, job_name, w_i, v_i = jobs[i]

        # 3. "Updated in descending order: c = W, W - 1, ..., w_i"
        # En Python, el range(inicio, fin, paso) se detiene antes de llegar al 'fin'.
        # Por eso usamos w_i - 1, para que el ciclo incluya a w_i.
        for c in range(capacity_W, w_i - 1, -1):
            
            # Si tomar el trabajo actual mejora el alivio que ya teníamos registrado...
            if DP[c - w_i] + v_i > DP[c]:
                DP[c] = DP[c - w_i] + v_i
                keep[i][c] = True # Anotamos en el historial que sí lo tomamos

    # El resultado del máximo alivio estará al final de nuestra lista 1D
    best_relief = DP[capacity_W]

    # 4. Reconstrucción de la selección (Reconstruct a concrete optimal set)
    chosen_ids = []
    current_c = capacity_W

    # Recorremos los trabajos de atrás hacia adelante
    for i in range(n - 1, -1, -1):
        if keep[i][current_c]:
            job_id, job_name, w_i, v_i = jobs[i]
            chosen_ids.append(job_id)    # Lo agregamos a la respuesta
            current_c -= w_i             # Restamos el costo consumido

    # Invertimos la lista de IDs para mantener el orden original de los datos
    chosen_ids.reverse()

    return (best_relief, chosen_ids)
