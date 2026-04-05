# NumPy AIOps Anomaly Detection Pipeline

A pure NumPy pipeline that simulates IT infrastructure 
monitoring and detects anomalies across multiple servers 
and metrics.

## What it does

- Generates synthetic CPU, memory and latency metrics
  for 3 servers over 3 hours
- Detects anomalies using 3 methods:
  - Static threshold
  - Z-score dynamic threshold
  - IQR interquartile range method
- Correlates alerts across metrics to confirm incidents
- Produces a summary dashboard with per-server statistics

## Why this matters in AIOps

Single-metric alerting creates noise. This pipeline only 
raises a confirmed incident when CPU, memory and latency 
are all anomalous at the same minute — the same principle 
used in production AIOps platforms like Moogsoft and 
Dynatrace.

## Output example





## Tools used

- Python 3.11
- NumPy

## How to run

pip install numpy
python pipeline.py
