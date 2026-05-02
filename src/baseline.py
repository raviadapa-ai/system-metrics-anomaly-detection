import numpy as np

def compute_baseline(server_names, cpu, memory, latency):

    baseline = {}

    for i, name in enumerate(server_names):

        baseline[name] = {
            "cpu_mean": float(cpu[:, i].mean()),
            "cpu_std": float(cpu[:, i].std()),
            "cpu_p95": float(np.percentile(cpu[:, i], 95)),

            "mem_mean": float(memory[:, i].mean()),
            "mem_std": float(memory[:, i].std()),
            "mem_p95": float(np.percentile(memory[:, i], 95)),

            "lat_mean": float(latency[:, i].mean()),
            "lat_std": float(latency[:, i].std()),
            "lat_p95": float(np.percentile(latency[:, i], 95)),
        }

    return baseline


def print_baseline(baseline):

    print("\n=========== BASELINE PROFILE ===========\n")

    for server, stats in baseline.items():

        print(f"{server}")
        print(f" CPU : mean={stats['cpu_mean']:.1f}, std={stats['cpu_std']:.1f}, p95={stats['cpu_p95']:.1f}")
        print(f" MEM : mean={stats['mem_mean']:.1f}, std={stats['mem_std']:.1f}, p95={stats['mem_p95']:.1f}")
        print(f" LAT : mean={stats['lat_mean']:.1f}, std={stats['lat_std']:.1f}, p95={stats['lat_p95']:.1f}\n")