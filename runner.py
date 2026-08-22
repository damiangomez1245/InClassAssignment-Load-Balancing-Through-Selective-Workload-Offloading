import time
import statistics
import matplotlib.pyplot as plt
from greedy import greedy_heuristic

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

def measure_runtime(method, jobs, W, repetitions=5):
    times = []
    for _ in range(repetitions):
        start_time = time.perf_counter()
        method(jobs, W) 
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000) 
    return statistics.median(times)

def validate_solution(jobs, capacity_W, reported_relief, chosen_ids, method_name):
    assert len(chosen_ids) == len(set(chosen_ids)), f"[{method_name}] Error: Trabajos repetidos."
    jobs_dict = {job[0]: job for job in jobs}
    total_cost = 0
    calculated_relief = 0
    for job_id in chosen_ids:
        assert job_id in jobs_dict, f"[{method_name}] Error: Trabajo {job_id} no existe."
        job = jobs_dict[job_id]
        total_cost += job[2]
        calculated_relief += job[3]
    assert total_cost <= capacity_W, f"[{method_name}] Error: Excede capacidad."
    assert reported_relief == calculated_relief, f"[{method_name}] Error: Alivio no coincide."
    return True

def generate_figures(results, workload_name):
    """Genera y exporta las gráficas PNG y PDF."""
    caps = results['Greedy']['capacities']
    
    plt.figure(figsize=(8, 5))
    plt.plot(caps, results['Greedy']['runtimes'], label='Greedy', marker='o')
    plt.plot(caps, results['DP']['runtimes'], label='Dynamic Programming', marker='s')
    plt.plot(caps, results['BB']['runtimes'], label='Branch-and-Bound', marker='^')
    
    plt.title(f'Runtime vs Capacity - Workload {workload_name}')
    plt.xlabel('Offloading Capacity (W)')
    plt.ylabel('Median Runtime (ms)')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()
    plt.savefig(f'runtime_vs_capacity_{workload_name}.png', format='png', bbox_inches='tight')
    plt.savefig(f'runtime_vs_capacity_{workload_name}.pdf', format='pdf', bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(8, 5))
    greedy_gap = []
    for i in range(len(caps)):
        opt_val = results['DP']['values'][i]
        greedy_val = results['Greedy']['values'][i]
        greedy_gap.append(opt_val - greedy_val)
        
    plt.plot(caps, greedy_gap, label='Greedy Gap', color='red', marker='x', linestyle='--')
    plt.title(f'Greedy Value Gap vs Capacity - Workload {workload_name}')
    plt.xlabel('Offloading Capacity (W)')
    plt.ylabel('Load Relief Gap (Optimal - Greedy)')
    plt.grid(True, ls="--", alpha=0.5)
    plt.legend()
    plt.savefig(f'greedy_gap_vs_capacity_{workload_name}.png', format='png', bbox_inches='tight')
    plt.savefig(f'greedy_gap_vs_capacity_{workload_name}.pdf', format='pdf', bbox_inches='tight')
    plt.close()
    print(f"Figuras de {workload_name} exportadas con éxito.")

if __name__ == "__main__":
    print("Iniciando Benchmarking de Workload Offloading...\n")
    
    results_C1 = {
        'Greedy': {'capacities': capacities, 'runtimes': [], 'values': []},
        'DP': {'capacities': capacities, 'runtimes': [0.001]*8, 'values': [0]*8}, 
        'BB': {'capacities': capacities, 'runtimes': [0.001]*8, 'values': [0]*8}
    }
    
    results_C2 = {
        'Greedy': {'capacities': capacities, 'runtimes': [], 'values': []},
        'DP': {'capacities': capacities, 'runtimes': [0.001]*8, 'values': [0]*8},
        'BB': {'capacities': capacities, 'runtimes': [0.001]*8, 'values': [0]*8}
    }

    print("--- Evaluando Workload C1 ---")
    for w in capacities:
        alivio_C1, elegidos_C1 = greedy_heuristic(C1, w)
        tiempo_C1 = measure_runtime(greedy_heuristic, C1, w)
        validate_solution(C1, w, alivio_C1, elegidos_C1, "Greedy")
        results_C1['Greedy']['runtimes'].append(tiempo_C1)
        results_C1['Greedy']['values'].append(alivio_C1)
        print(f"Capacidad: {w:3} | Alivio: {alivio_C1:3} | Tiempo: {tiempo_C1:.4f} ms")

    print("\n--- Evaluando Workload C2 ---")
    for w in capacities:
        alivio_C2, elegidos_C2 = greedy_heuristic(C2, w)
        tiempo_C2 = measure_runtime(greedy_heuristic, C2, w)
        validate_solution(C2, w, alivio_C2, elegidos_C2, "Greedy")
        results_C2['Greedy']['runtimes'].append(tiempo_C2)
        results_C2['Greedy']['values'].append(alivio_C2)
        print(f"Capacidad: {w:3} | Alivio: {alivio_C2:3} | Tiempo: {tiempo_C2:.4f} ms")

    print("\nGenerando figuras PNG y PDF...")
    generate_figures(results_C1, "C1")
    generate_figures(results_C2, "C2")