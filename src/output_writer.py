import pandas as pd
import json
import os
import numpy as np

# -------------------------------
# Save metrics
# -------------------------------
def save_metrics(server_names, cpu, memory, latency, filename):

    os.makedirs("data", exist_ok=True)

    rows = []
    for i, name in enumerate(server_names):
        for t in range(cpu.shape[0]):
            rows.append({
                "server": name,
                "timestamp": pd.Timestamp("2026-01-01") + pd.Timedelta(minutes=t),
                "cpu": cpu[t, i],
                "memory": memory[t, i],
                "latency": latency[t, i]
            })

    df = pd.DataFrame(rows)
    df.to_csv(f"data/{filename}", index=False)

    print(f"\n Saved: data/{filename}")


# -------------------------------
# Save baseline
# -------------------------------
def save_baseline(baseline):

    os.makedirs("output", exist_ok=True)

    with open("output/baseline.json", "w") as f:
        json.dump(baseline, f, indent=4)

    print("Saved: output/baseline.json")


# -------------------------------
# Save incidents
# -------------------------------
def save_incidents(results):

    with open("output/incidents.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Saved: output/incidents.json")


# -------------------------------
# Save dashboard
# -------------------------------
def save_dashboard(server_names, cpu, memory, latency, results):

    rows = []

    for i, name in enumerate(server_names):
        rows.append({
            "server": name,
            "cpu_mean": round(cpu[:, i].mean(), 1),
            "mem_mean": round(memory[:, i].mean(), 1),
            "lat_p95": round(np.percentile(latency[:, i], 95), 1),
            "incidents": len(results[name])
        })

    df = pd.DataFrame(rows)
    df.to_csv("output/dashboard.csv", index=False)

    print("Saved: output/dashboard.csv")