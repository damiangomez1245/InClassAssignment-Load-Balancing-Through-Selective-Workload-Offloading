from typing import List, Tuple
import time
import statistics
import matplotlib.pyplot as plt
from dynamic_programming import solve_method

if __name__ == "__main__":
    method_name = "Dynamic Programming (1D)"
    workload_name = "Workload C2"
    
    print(f"=== {method_name} - {workload_name} ===\n")
    
    workload_C1 = [
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

    workload_C2 = [
        ("Q10", "Realtime Analytics", 10, 60),
        ("Q20", "Search Reindexing", 20, 100),
        ("Q30", "Video Transcoding", 30, 120),
        ("Q35", "Database Replication", 35, 130),
        ("Q40", "Model Inference Batch", 40, 135),
        ("Q45", "Large ETL Pipeline", 45, 140),
        ("Q50", "Database Migration", 50, 150)
    ]
    
    cost_lookup = {job[0]: job[2] for job in workload_C2}

    capacities = [20, 35, 50, 65, 80, 95, 110, 140]
    median_runtimes = []

    for W in capacities:
        runtimes_for_this_W = []
        best_load_relief = 0
        chosen_ids = []
        
        for _ in range(5):
            start_time = time.perf_counter()
            
            best_load_relief, chosen_ids = solve_method(workload_C2, W) 
            
            end_time = time.perf_counter()
            
            time_ms = (end_time - start_time) * 1000 
            runtimes_for_this_W.append(time_ms)
            
        mediana = statistics.median(runtimes_for_this_W)
        median_runtimes.append(mediana)

        total_migration_cost = sum(cost_lookup[jid] for jid in chosen_ids if jid in cost_lookup)
  
        print(f"Method Name:               {method_name}")
        print(f"Workload Name:             {workload_name}")
        print(f"Capacity (W):              {W}")
        print(f"Returned Value (Relief):   {best_load_relief}")
        print(f"Selected Job Identifiers:  {chosen_ids}")
        print(f"Total Migration Cost:      {total_migration_cost} / {W}")
        print(f"Median Runtime:            {mediana:.5f} ms")
        print(f"Raw Runtimes (ms):         {[round(r, 5) for r in runtimes_for_this_W]}")
        print("-" * 60 + "\n")

    #gráfica
    plt.figure()
    plt.plot(capacities, median_runtimes, marker='o')
    plt.title(f'Runtime vs Capacity ({workload_name})')
    plt.xlabel('Offloading Capacity W')
    plt.ylabel('Median Runtime (ms)')
    plt.grid(True)
    plt.show()