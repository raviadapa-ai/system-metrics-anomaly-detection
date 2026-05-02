from src.anomaly_detection import detect_anomalies

def print_anomaly_report(server_names, cpu, memory, latency):

    print("\n======= ANOMALY DETECTION REPORT =======")

    for i, name in enumerate(server_names):

        cpu_alerts = [int(x) for x in detect_anomalies(cpu[:, i])]
        memory_alerts = [int(x) for x in detect_anomalies(memory[:, i])]
        latency_alerts = [int(x) for x in detect_anomalies(latency[:, i], static_threshold=50)]

        #cpu_alerts = detect_anomalies(cpu[:, i])
        #memory_alerts = detect_anomalies(memory[:, i])
        #latency_alerts = detect_anomalies(latency[:, i], static_threshold=50)

        print(f"\n{name}")

        print(f"cpu alerts     : {sorted(cpu_alerts)}")
        print(f"memory alerts  : {sorted(memory_alerts)}")
        print(f"latency alerts : {sorted(latency_alerts)}")