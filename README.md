# ⚙️ System Metrics Anomaly Detection

A lightweight observability simulator that generates system metrics (CPU, Memory, Latency), detects anomalies using statistical techniques, and correlates incidents — built using NumPy.

---

## 📌 Overview

This project demonstrates how anomaly detection works on system-level metrics using statistical methods. It simulates server behavior, injects failures, and identifies abnormal patterns across multiple signals.

It is designed as a **learning-focused, minimal AIOps-style pipeline** using NumPy (no heavy ML frameworks).

---

## 🧠 Architecture

```id="arch01"
Metrics Generator (CPU, Memory, Latency)
        ↓
Baseline Statistics
        ↓
Failure Injection
        ↓
Anomaly Detection (Threshold + Z-score + IQR)
        ↓
Correlation Engine (Multi-signal)
        ↓
Dashboard + Output Files
```

---

## 📊 Generated Metrics

The system simulates three key infrastructure metrics for each server:

### 🔹 CPU Usage (%)

* Represents processor utilization
* Normal range: ~40% – 80%
* Failure simulation: sudden spikes (>90%)

### 🔹 Memory Usage (%)

* Represents RAM consumption
* Slightly higher variance than CPU
* Failure simulation: memory pressure / leaks

### 🔹 Latency (ms)

* Represents response time of the system
* Lower values are healthy
* Failure simulation: sharp increase during incidents

These metrics are generated using **NumPy random distributions** to mimic realistic system behavior.

---

## ⚙️ Features

### ✅ Metrics Simulation

* Multi-server support
* CPU, Memory, Latency generation
* Controlled randomness using NumPy

### ✅ Baseline Modeling

* Mean
* Standard deviation
* 95th percentile (p95)

### ✅ Failure Injection

* Simulates production-like incidents
* Multi-metric spikes (CPU + Memory + Latency)

### ✅ Anomaly Detection

* Static threshold detection
* Z-score method
* IQR (Interquartile Range)
* Consensus filtering (reduces false positives)

### ✅ Correlation Engine

* Multi-metric anomaly correlation
* Incident detection using “2+ signals rule”
* Reduces alert noise

### ✅ Output Pipeline

* Saves structured outputs (CSV + JSON)
* Clean separation of logic and IO

---

## 📁 Project Structure

```id="struct01"
system-metrics-anomaly-detection/

├── src/
│   ├── metrics_generator.py
│   ├── baseline.py
│   ├── failure_simulation.py
│   ├── anomaly_detection.py
│   ├── anomaly_report.py
│   ├── correlation_engine.py
│   ├── dashboard.py
│   ├── output_writer.py
│   ├── config.py
│
├── data/
│   ├── metrics_clean.csv
│   ├── metrics_with_failures.csv
│
├── output/
│   ├── baseline.json
│   ├── incidents.json
│   ├── dashboard.csv
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash id="run01"
pip install -r requirements.txt
```

### 2. Run the pipeline

```bash id="run02"
python main.py
```

---

## 📊 Sample Output

### 🔹 Baseline Profile

=========== BASELINE PROFILE ===========

web-01
 CPU : mean=59.7, std=4.3, p95=66.8
 MEM : mean=63.9, std=7.9, p95=77.9
 LAT : mean=17.9, std=3.0, p95=22.8

app-01
 CPU : mean=72.2, std=6.1, p95=82.4
 MEM : mean=77.5, std=10.0, p95=94.8
 LAT : mean=25.0, std=4.3, p95=31.5

db-01
 CPU : mean=44.9, std=4.1, p95=51.3
 MEM : mean=55.4, std=5.8, p95=63.9
 LAT : mean=11.8, std=2.1, p95=15.0

Saved: output/baseline.json

Saved: data/metrics_with_failures.csv
 
### 🔹 Anomaly Detection


======= ANOMALY DETECTION REPORT =======

web-01
cpu alerts     : [45, 46, 47, 139]
memory alerts  : [40, 45, 46, 47, 89, 91, 129, 136, 153, 156]
latency alerts : [45, 46, 47]

app-01
cpu alerts     : [46, 56, 68, 113, 120, 121, 122, 160]
memory alerts  : [1, 2, 5, 7, 16, 17, 19, 20, 21, 25, 26, 33, 34, 35, 37, 40, 42, 49, 50, 51, 53, 62, 63, 76, 77, 78, 84, 85, 101, 103, 108, 109, 111, 117, 118, 120, 121, 122, 126, 127, 129, 132, 145, 152, 161, 166, 168, 175]
latency alerts : [48, 120, 121, 122, 177]

db-01
cpu alerts     : [15, 30, 51, 93, 119, 144, 146, 178]
memory alerts  : [5, 19, 47, 49, 57, 124, 126, 153, 177]
latency alerts : [6, 16, 33, 36, 68, 81, 94, 138, 146, 176]

### 🔹 Correlated Incidents

--------- Correlated Incidents ---------

web-01 - confirmed incidents:
2026-01-01 00:45:00 | cpu: 91.0% | mem: 92.0% | lat: 85.0 ms
2026-01-01 00:46:00 | cpu: 94.0% | mem: 95.0% | lat: 110.0 ms
2026-01-01 00:47:00 | cpu: 89.0% | mem: 90.0% | lat: 92.0 ms

app-01 - confirmed incidents:
2026-01-01 02:00:00 | cpu: 95.0% | mem: 97.0% | lat: 120.0 ms
2026-01-01 02:01:00 | cpu: 98.0% | mem: 99.0% | lat: 145.0 ms
2026-01-01 02:02:00 | cpu: 93.0% | mem: 95.0% | lat: 118.0 ms

db-01 - confirmed incidents:
2026-01-01 02:26:00 | cpu: 54.7% | mem: 51.8% | lat: 7.3 ms
Saved: output/incidents.json

### 🔹 Dashboard Summary

================ SUMMARY DASHBOARD ================

server     cpu_mean   mem_mean   lat_p95    incidents
-----------------------------------------------------------------
web-01     60.2       64.4       23.2       11
app-01     72.6       77.6       32.5       55
db-01      44.9       55.4       15.0       26
Saved: output/dashboard.csv


## 🧪 Data Outputs

### 📁 `data/`

* `metrics_clean.csv` → Normal system behavior
* `metrics_with_failures.csv` → Injected anomalies

### 📁 `output/`

* `baseline.json` → Baseline statistics
* `incidents.json` → Correlated incidents
* `dashboard.csv` → System summary

---

## 🧠 Key Concepts Demonstrated

* Time-series simulation
* Multi-metric anomaly detection
* Z-score and IQR methods
* Incident correlation logic
* NumPy-based data processing
* Modular pipeline design (Separation of Concerns)

---

## 🔥 Future Improvements

* Add metric dependencies (CPU → Latency relationship)
* Introduce anomaly severity scoring
* Real-time streaming simulation
* Streamlit dashboard visualization
* ML-based anomaly detection models

---

## 📌 Author

AIOps Engineer

---

## ⭐ Support

If you found this useful, consider giving it a ⭐ on GitHub!
