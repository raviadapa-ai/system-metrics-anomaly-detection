from src.anomaly_detection import detect_anomalies
import numpy as np

def print_summary_dashboard(server_names, cpu, memory, latency, results):

    print("\n================ SUMMARY DASHBOARD ================")

    print(f"{'server':<10} {'cpu_mean':<10} {'mem_mean':<10} {'lat_p95':<10} {'raw_anomalies':<18} {'correlated_incidents'}")
    print("-" * 90)

    for i, name in enumerate(server_names):

        cpu_mean = round(cpu[:, i].mean(), 1)
        mem_mean = round(memory[:, i].mean(), 1)
        lat_p95 = round(np.percentile(latency[:, i], 95), 1)

        cpu_a = detect_anomalies(cpu[:, i])
        mem_a = detect_anomalies(memory[:, i])
        lat_a = detect_anomalies(latency[:, i], static_threshold=50)

        raw_anomalies = len(cpu_a | mem_a | lat_a)
        correlated = len(results[name])

        print(f"{name:<10} {cpu_mean:<10} {mem_mean:<10} {lat_p95:<10} {raw_anomalies:<18} {correlated}")



#

#     print("\n================ SUMMARY DASHBOARD ================")
#     print("server     cpu_mean   mem_mean   lat_p95    raw_anomalies   correlated_incidents")
#     print("-"*80)

#     for i, name in enumerate(server_names):

#         cpu_a = detect_anomalies(cpu[:, i])
#         mem_a = detect_anomalies(memory[:, i])
#         lat_a = detect_anomalies(latency[:, i], static_threshold=50)

#         # 🔴 Raw anomalies (union of all)
#         raw_anomalies = len(cpu_a | mem_a | lat_a)

#         # 🟢 Correlated incidents (from your function)
#         correlated_incidents = len(results[name])

#         print(f"{name}       "
#               f"{round(cpu[:, i].mean(),1)}       "
#               f"{round(memory[:, i].mean(),1)}       "
#               f"{round(np.percentile(latency[:, i],95),1)}       "
#               f"{raw_anomalies:<18} "
#               f"{correlated_incidents}")