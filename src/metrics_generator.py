import numpy as np
import pandas as pd

def generate_metrics(seed=42, n=180):
    rng = np.random.default_rng(seed)

    server_names = ['web-01', 'app-01', 'db-01']

    timestamps = pd.date_range("2026-01-01 00:00:00", periods=n, freq="1min")
    
    cpu = np.column_stack([
        np.clip(rng.normal(60, 5, n), 0, 100),
        np.clip(rng.normal(72, 6, n), 0, 100),
        np.clip(rng.normal(45, 4, n), 0, 100),
    ])

    memory = np.column_stack([
        np.clip(rng.normal(65, 8, n), 0, 100),
        np.clip(rng.normal(78, 10, n), 0, 100),
        np.clip(rng.normal(55, 6, n), 0, 100),
    ])

    latency = np.column_stack([
        np.clip(rng.normal(18, 3, n), 0, 500),
        np.clip(rng.normal(25, 4, n), 0, 500),
        np.clip(rng.normal(12, 2, n), 0, 500),
    ])

    return server_names, cpu, memory, latency, timestamps

