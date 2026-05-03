# imports
import numpy as np
import pandas as pd
import os
import json

from src.metrics_generator import generate_metrics
from src.baseline import compute_baseline, print_baseline
from src.failure_simulation import inject_failures
from src.anomaly_report import print_anomaly_report
from src.dashboard import print_summary_dashboard
from src.correlation_engine import correlate_incidents
from src.raw_anomaly_report import print_raw_anomalies


from src.output_writer import (
    save_metrics,
    save_baseline,
    save_incidents,
    save_dashboard
)

# Step 1
server_names, cpu, memory, latency, timestamps = generate_metrics()

# Step 2
save_metrics(server_names, cpu, memory, latency, "metrics_clean.csv")

baseline = compute_baseline(server_names, cpu, memory, latency)
print_baseline(baseline)
save_baseline(baseline)

# Step 3
cpu, memory, latency = inject_failures(cpu, memory, latency)
save_metrics(server_names, cpu, memory, latency, "metrics_with_failures.csv")

# Step 4
print_anomaly_report(server_names, cpu, memory, latency)
print_raw_anomalies(server_names, cpu, memory, latency, timestamps)
# Step 5
results = correlate_incidents(cpu, memory, latency, server_names, timestamps)
save_incidents(results)

# Step 6
print_summary_dashboard(server_names, cpu, memory, latency,results)
save_dashboard(server_names, cpu, memory, latency, results)