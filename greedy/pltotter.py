import matplotlib.pyplot as plt

def generate_figures(results, workload_name):
   
    capacities = results['Greedy']['capacities']
    
    plt.figure(figsize=(8, 5))
    
    plt.plot(capacities, results['Greedy']['runtimes'], label='Greedy', marker='o')
    plt.plot(capacities, results['DP']['runtimes'], label='Dynamic Programming', marker='s')
    plt.plot(capacities, results['BB']['runtimes'], label='Branch-and-Bound', marker='^')
    
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
    for i in range(len(capacities)):
        opt_val = results['DP']['values'][i]
        greedy_val = results['Greedy']['values'][i]
        greedy_gap.append(opt_val - greedy_val)
        
    plt.plot(capacities, greedy_gap, label='Greedy Gap', color='red', marker='x', linestyle='--')
    
    plt.title(f'Greedy Value Gap vs Capacity - Workload {workload_name}')
    plt.xlabel('Offloading Capacity (W)')
    plt.ylabel('Load Relief Gap (Optimal - Greedy)')
    plt.grid(True, ls="--", alpha=0.5)
    plt.legend()
    
    plt.savefig(f'greedy_gap_vs_capacity_{workload_name}.png', format='png', bbox_inches='tight')
    plt.savefig(f'greedy_gap_vs_capacity_{workload_name}.pdf', format='pdf', bbox_inches='tight')
    plt.close()
    
    print(f"Figuras para {workload_name} generadas exitosamente (PNG y PDF).")