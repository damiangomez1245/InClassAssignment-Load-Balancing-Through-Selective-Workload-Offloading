import os
import zipfile
import subprocess



code_greedy = """from typing import List, Tuple

def greedy_heuristic(
        jobs: List[Tuple[str, str, int, int]],
        capacity_W: int,
) -> Tuple[int, List[str]]:
    if capacity_W <= 0:
        return 0, []

    sorted_jobs = sorted(
        jobs,
        key=lambda job: (
            -(job[3] / job[2]),
            job[2],
            job[0]
        )
    )

    best_load_releif = 0
    chosen_ids = []
    remaining_capacity = capacity_W

    for job in sorted_jobs:
        job_id, name, migration_cost, load_relief = job

        if migration_cost <= remaining_capacity:
            chosen_ids.append(job_id)
            best_load_releif += load_relief
            remaining_capacity -= migration_cost

    return best_load_releif, chosen_ids
"""

code_dp = """from typing import List, Tuple

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
"""

code_bb = """from typing import List, Tuple
from greedy import greedy_heuristic

def solve_branch_and_bound(jobs: List[Tuple[str, str, int, int]], capacity_W: int) -> Tuple[int, List[str]]:
    if capacity_W <= 0:
        return 0, []

    sorted_jobs = sorted(
        jobs,
        key=lambda j: (- (j[3] / j[2]), j[2], j[0])
    )
    n = len(sorted_jobs)
    
    # Initialize incumbent with Greedy to prune branches early
    best_value, best_selection = greedy_heuristic(jobs, capacity_W)

    def compute_upper_bound(index, current_cost, current_relief):
        bound = current_relief
        rem_cap = capacity_W - current_cost
        for i in range(index, n):
            j_id, name, cost, relief = sorted_jobs[i]
            if rem_cap >= cost:
                rem_cap -= cost
                bound += relief
            else:
                bound += (rem_cap / cost) * relief
                break
        return bound

    def backtrack(index, current_cost, current_relief, current_ids):
        nonlocal best_value, best_selection

        if current_relief > best_value:
            best_value = current_relief
            best_selection = list(current_ids)

        if index == n:
            return

        ub = compute_upper_bound(index, current_cost, current_relief)
        if ub <= best_value:
            return

        j_id, name, cost, relief = sorted_jobs[index]
        if current_cost + cost <= capacity_W:
            current_ids.append(j_id)
            backtrack(index + 1, current_cost + cost, current_relief + relief, current_ids)
            current_ids.pop()

        if compute_upper_bound(index + 1, current_cost, current_relief) > best_value:
            backtrack(index + 1, current_cost, current_relief, current_ids)

    backtrack(0, 0, 0, [])
    return best_value, best_selection
"""

code_total = """import time
import statistics
import matplotlib.pyplot as plt
from greedy import greedy_heuristic
from dynamic_programing import solve_method as solve_dp
from branch_and_bound import solve_branch_and_bound

C1 = [
    ("P01", "Health Check Service",        1,  6),
    ("P02", "Cache Refresh",               2, 11),
    ("P03", "Log Processing",              3, 16),
    ("P04", "Thumbnail Generation",        4, 21),
    ("P05", "Search Index Update",         5, 26),
    ("P06", "Analytics Batch",             6, 31),
    ("P07", "Recommendation Refresh",      7, 36),
    ("P08", "Video Processing",            8, 40),
    ("P09", "Database Maintenance",        9, 45),
    ("P10", "Machine Learning Inference", 10, 50)
]

C2 = [
    ("Q10", "Realtime Analytics",       10,  60),
    ("Q20", "Search Reindexing",        20, 100),
    ("Q30", "Video Transcoding",        30, 120),
    ("Q35", "Database Replication",     35, 130),
    ("Q40", "Model Inference Batch",    40, 135),
    ("Q45", "Large ETL Pipeline",       45, 140),
    ("Q50", "Database Migration",       50, 150)
]

capacities = [20, 35, 50, 65, 80, 95, 110, 140]

def evaluate_workload(workload, name):
    print(f"Evaluando {name}...")
    results = {
        'Greedy': {'time': [], 'gap': []},
        'DP': {'time': [], 'gap': []},
        'BB': {'time': [], 'gap': []}
    }
    
    for w in capacities:
        # Medición Greedy
        t_greedy = []
        for _ in range(5):
            t0 = time.perf_counter()
            v_g, _ = greedy_heuristic(workload, w)
            t_greedy.append((time.perf_counter() - t0) * 1000)
        med_g = statistics.median(t_greedy)
        
        # Medición DP
        t_dp = []
        for _ in range(5):
            t0 = time.perf_counter()
            v_dp, _ = solve_dp(workload, w)
            t_dp.append((time.perf_counter() - t0) * 1000)
        med_dp = statistics.median(t_dp)
        
        # Medición Branch & Bound
        t_bb = []
        for _ in range(5):
            t0 = time.perf_counter()
            v_bb, _ = solve_branch_and_bound(workload, w)
            t_bb.append((time.perf_counter() - t0) * 1000)
        med_bb = statistics.median(t_bb)
        
        # Guardar Runtimes
        results['Greedy']['time'].append(med_g)
        results['DP']['time'].append(med_dp)
        results['BB']['time'].append(med_bb)
        
        # Calcular los Gaps reales
        results['Greedy']['gap'].append(0)
        results['DP']['gap'].append(v_dp - v_g)
        results['BB']['gap'].append(v_bb - v_g)
        
    return results

if __name__ == "__main__":
    res_c1 = evaluate_workload(C1, "C1")
    res_c2 = evaluate_workload(C2, "C2")

    def plot_runtime(res, w_name):
        plt.figure(figsize=(9, 5.5))
        plt.plot(capacities, res['DP']['time'], marker='s', markersize=7, label='Dynamic Programming', color='royalblue', linewidth=2)
        plt.plot(capacities, res['BB']['time'], marker='^', markersize=7, label='Branch & Bound', color='darkorange', linewidth=2)
        plt.plot(capacities, res['Greedy']['time'], marker='o', markersize=7, label='Greedy', color='crimson', linewidth=2)
        
        plt.yscale('log')
        plt.title(f'Runtime vs Capacity - Workload {w_name}', fontsize=14, pad=15)
        plt.xlabel('Offloading Capacity (W)', fontsize=11)
        plt.ylabel('Median Runtime (ms) [Log Scale]', fontsize=11)
        plt.grid(True, which="both", ls="--", alpha=0.5)
        plt.legend(fontsize=10)
        plt.tight_layout()
        plt.savefig(f'runtime_{w_name}.png', dpi=300)
        plt.close()

    def plot_gap(res, w_name):
        plt.figure(figsize=(9, 5.5))
        
        # Linea de DP (más gruesa y con transparencia para dejar ver B&B)
        plt.plot(capacities, res['DP']['gap'], marker='s', markersize=9, label='Dynamic Programming Gap', color='royalblue', linewidth=4, alpha=0.6)
        
        # Linea de B&B (punteada encima de DP para validar que tienen el mismo valor óptimo)
        plt.plot(capacities, res['BB']['gap'], marker='^', markersize=7, label='Branch & Bound Gap', color='darkorange', linestyle='--', linewidth=2)
        
        # Linea Greedy (siempre será 0 al restarse consigo mismo)
        plt.plot(capacities, res['Greedy']['gap'], marker='o', markersize=7, label='Greedy Gap', color='crimson', linestyle='-.', linewidth=2)
        
        plt.title(f'Greedy Value Gap vs Capacity - Workload {w_name}', fontsize=14, pad=15)
        plt.xlabel('Offloading Capacity (W)', fontsize=11)
        plt.ylabel('Load Relief Gap (Optimal - Greedy)', fontsize=11)
        plt.grid(True, ls="--", alpha=0.5)
        plt.legend(fontsize=10)
        plt.tight_layout()
        plt.savefig(f'gap_{w_name}.png', dpi=300)
        plt.close()

    plot_runtime(res_c1, "C1")
    plot_gap(res_c1, "C1")
    plot_runtime(res_c2, "C2")
    plot_gap(res_c2, "C2")
    print("Gráficas exportadas con éxito.")
"""

# Escribir todos los archivos individualmente
with open("greedy.py", "w", encoding="utf-8") as f: f.write(code_greedy)
with open("dynamic_programing.py", "w", encoding="utf-8") as f: f.write(code_dp)
with open("branch_and_bound.py", "w", encoding="utf-8") as f: f.write(code_bb)
with open("total_graph.py", "w", encoding="utf-8") as f: f.write(code_total)

# Ejecutar main graph runner
subprocess.run(["python", "total_graph.py"], check=True)

# Empaquetar todo en un ZIP
zip_filename = "Benchmarking_Graphs_and_Code.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in ["greedy.py", "dynamic_programing.py", "branch_and_bound.py", "total_graph.py", 
                 "runtime_C1.png", "gap_C1.png", "runtime_C2.png", "gap_C2.png"]:
        zipf.write(file)
print(f"File created: {zip_filename}")