import numpy as np
from src.anomaly_detection import detect_anomalies

def print_summary_dashboard(server_names, cpu, memory, latency):

    print("\n================ SUMMARY DASHBOARD ================\n")
    print(f"{'server':<10} {'cpu_mean':<10} {'mem_mean':<10} {'lat_p95':<10} {'incidents'}")
    print("-" * 65)

    for i, name in enumerate(server_names):

        cpu_a = detect_anomalies(cpu[:, i])
        mem_a = detect_anomalies(memory[:, i])
        lat_a = detect_anomalies(latency[:, i], static_threshold=50)

        # simple incident definition (correlated signals)
        incidents = cpu_a | mem_a | lat_a

        print(f"{name:<10} "
              f"{cpu[:, i].mean():<10.1f} "
              f"{memory[:, i].mean():<10.1f} "
              f"{np.percentile(latency[:, i], 95):<10.1f} "
              f"{len(incidents)}")