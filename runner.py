import time
import statistics
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
    """Mide la mediana del tiempo de ejecución en milisegundos."""
    times = []
    for _ in range(repetitions):
        start_time = time.perf_counter()
        method(jobs, W) 
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000) 
    
    return statistics.median(times)

if __name__ == "__main__":
    print("--- Pruebas del Algoritmo Greedy ---")
    
    for w in capacities:
        alivio, elegidos = greedy_heuristic(C2, w)
        mediana_ms = measure_runtime(greedy_heuristic, C2, w)
        
        print(f"Capacidad: {w} | Alivio: {alivio} | Tiempo: {mediana_ms:.4f} ms | Elegidos: {elegidos}")