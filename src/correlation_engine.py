from src.anomaly_detection import detect_anomalies

def correlate_incidents(cpu, memory, latency, server_names):

    results = {}

    for i, name in enumerate(server_names):

        cpu_a = detect_anomalies(cpu[:, i])
        mem_a = detect_anomalies(memory[:, i])
        lat_a = detect_anomalies(latency[:, i], static_threshold=50)

        # correlated incidents (2+ signals rule)
        incidents = []

        for idx in (cpu_a | mem_a | lat_a):
            score = sum([
                idx in cpu_a,
                idx in mem_a,
                idx in lat_a
            ])

            if score >= 2:
                incidents.append(int(idx))

        results[name] = sorted(set(incidents))

    return results