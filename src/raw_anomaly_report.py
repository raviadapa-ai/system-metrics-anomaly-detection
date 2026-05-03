from src.anomaly_detection import detect_anomalies
import numpy as np

def print_raw_anomalies(server_names, cpu, memory, latency, timestamps):

    print("\n======= RAW ANOMALY REPORT =======")

    for i, name in enumerate(server_names):

        cpu_a = detect_anomalies(cpu[:, i])
        mem_a = detect_anomalies(memory[:, i])
        lat_a = detect_anomalies(latency[:, i], static_threshold=50)

        # union of all anomalies
        all_points = sorted(cpu_a | mem_a | lat_a)

        print(f"\n{name} - RAW anomalies:")

        if not all_points:
            print("No anomalies")
            continue

        for idx in all_points:

            signals = []

            if idx in cpu_a:
                signals.append("cpu")
            if idx in mem_a:
                signals.append("memory")
            if idx in lat_a:
                signals.append("latency")

            print(
                f"{timestamps[idx]} | "
                f"{', '.join(signals)} | "
                f"cpu: {cpu[idx, i]:.1f}% | "
                f"mem: {memory[idx, i]:.1f}% | "
                f"lat: {latency[idx, i]:.1f} ms"
            )