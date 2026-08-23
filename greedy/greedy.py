from typing import List, Tuple

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

if __name__ == "__main__":
    C1 = [
        ("P01", "Health Chek Service", 1, 6),
        ("P02", "Cachw Refresh", 2, 11),
        ("P03", "Log Processing", 3, 16)
    ]

    alivio, elegidos = greedy_heuristic(C1, 4)
    print(f"Alivio total: {alivio}")
    print(f"Trabajos elegidos: {elegidos}")