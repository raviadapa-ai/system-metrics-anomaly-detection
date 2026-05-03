from src.anomaly_detection import detect_anomalies

def correlate_incidents(cpu, memory, latency, server_names, timestamps):

    results = {}

    print("\n--------- Correlated Incidents ---------")

    for i, name in enumerate(server_names):

        cpu_a = detect_anomalies(cpu[:, i])
        mem_a = detect_anomalies(memory[:, i])
        lat_a = detect_anomalies(latency[:, i], static_threshold=50)

        incidents = []

        for idx in sorted(cpu_a | mem_a | lat_a):

            score = sum([
                idx in cpu_a,
                idx in mem_a,
                idx in lat_a
            ])

            if score >= 2:
                incidents.append({
                    "timestamp": str(timestamps[idx]),  # ✅ FIXED
                    "minute": int(idx),
                    "cpu": round(cpu[idx, i], 1),
                    "memory": round(memory[idx, i], 1),
                    "latency": round(latency[idx, i], 1)
                })

        results[name] = incidents

        # PRINT
        if incidents:
            print(f"\n{name} - confirmed incidents:")
            for inc in incidents:
                print(
                    f"{inc['timestamp']} | "
                    f"cpu: {inc['cpu']}% | "
                    f"mem: {inc['memory']}% | "
                    f"lat: {inc['latency']} ms"
                )
        else:
            print(f"\n{name} - no confirmed incidents")

    return results