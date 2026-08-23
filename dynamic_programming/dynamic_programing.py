from typing import List, Tuple
import time
import statistics


def solve_method(
    jobs: List[Tuple[str, str, int, int]], 
    capacity_W: int
) -> Tuple[int, List[str]]:
    
    if capacity_W <= 0:
        return (0, [])

    n = len(jobs)

    DP = [0] * (capacity_W + 1)

    keep = [[False] * (capacity_W + 1) for _ in range(n)]

    for i in range(n):
        job_id, job_name, w_i, v_i = jobs[i]

        for c in range(capacity_W, w_i - 1, -1):
            
            if DP[c - w_i] + v_i > DP[c]:
                DP[c] = DP[c - w_i] + v_i
                keep[i][c] = True 

    best_relief = DP[capacity_W]

    chosen_ids = []
    current_c = capacity_W

    for i in range(n - 1, -1, -1):
        if keep[i][current_c]:
            job_id, job_name, w_i, v_i = jobs[i]
            chosen_ids.append(job_id)    
            current_c -= w_i             

    chosen_ids.reverse()

    return (best_relief, chosen_ids)
