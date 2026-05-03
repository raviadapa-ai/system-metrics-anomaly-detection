> ⚠️ Note: This project focuses on **intra-server anomaly correlation** using synthetic metrics with controlled failure injection.

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

## 🧠 Data & Correlation Design

### 📊 Metric Generation
The system generates three types of system metrics:
- CPU usage (%)
- Memory usage (%)
- Latency (ms)

These metrics are **synthetically generated using independent statistical distributions**, meaning they are not inherently correlated under normal conditions.

---

### ⚠️ Failure Injection
To simulate realistic system behavior, controlled failures are injected into the data.  
During these failure windows, multiple metrics (CPU, memory, latency) are simultaneously elevated.

This introduces **artificial correlation across metrics**, mimicking real-world incidents.

---

### 🔍 Anomaly Detection
Each metric is analyzed independently using:
- Static thresholds
- Z-score detection
- IQR-based outlier detection

---

### 🔗 Correlation Strategy

Correlation is performed **within each server only**, not across servers.

For a given server:
- CPU, memory, and latency anomalies are combined
- An incident is confirmed when **multiple signals agree (2+ rule)**

---

### 🚫 Limitations

- No cross-server correlation (distributed/system-wide failures are not detected)
- Metrics are synthetic and do not represent real production traffic patterns

---

### 🧭 Summary

| Aspect | Approach |
|-------|--------|
| Metric dependency | Independent (before failure injection) |
| Failure modeling | Multi-metric injection |
| Correlation scope | Intra-server only |
| Cross-server detection | Not implemented |

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

### 🔹 Metrics data - servers and shapes with sample records(10)

```id="struct04"

servers: ['web-01', 'app-01', 'db-01']
cpu shape: (180, 3)
cpu metrics
 [[61.5 79.8 44.4]
 [54.8 73.3 46.5]
 [63.8 69.5 49. ]
 [64.7 78.6 40.8]
 [50.2 74.6 44.5]
 [53.5 81.2 50.9]
 [60.6 73.1 42. ]
 [58.4 64.7 41.7]
 [59.9 63.8 45.8]
 [55.7 81.9 48.4]]
memory shape: (180, 3)
memory metrics
 [[51.5 77.  57.3]
 [58.4 89.3 55.6]
 [67.  55.2 54.1]
 [63.6 63.  64.5]
 [63.  68.8 51.3]
 [63.7 92.6 67.4]
 [66.6 80.8 53.6]
 [56.9 85.7 47.3]
 [70.7 66.6 55.4]
 [70.3 66.8 48.5]]
latency shape: (180, 3)
latency metrics: [[18.7 29.  10.7]
 [17.5 25.4 12.7]
 [19.3 28.2  9.2]
 [18.2 23.2 14.9]
 [18.3 24.8 11.7]
 [16.8 24.5 12.6]
 [13.8 21.7 16.7]
 [13.4 27.6 15. ]
 [20.  27.6 11.4]
 [17.2 27.4 10.8]]

```
### 🔹 Baseline Profile

```id="struct02"

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
```
---
 
### 🔹 Anomaly Detection

```id="struct02"

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

======= RAW ANOMALY REPORT =======

web-01 - RAW anomalies:
2026-01-01 00:40:00 | memory | cpu: 63.7% | mem: 45.7% | lat: 19.4 ms
2026-01-01 00:45:00 | cpu, memory, latency | cpu: 91.0% | mem: 92.0% | lat: 85.0 ms
2026-01-01 00:46:00 | cpu, memory, latency | cpu: 94.0% | mem: 95.0% | lat: 110.0 ms
2026-01-01 00:47:00 | cpu, memory, latency | cpu: 89.0% | mem: 90.0% | lat: 92.0 ms
2026-01-01 01:29:00 | memory | cpu: 62.2% | mem: 45.7% | lat: 16.9 ms
2026-01-01 01:31:00 | memory | cpu: 59.5% | mem: 85.4% | lat: 12.3 ms
2026-01-01 02:09:00 | memory | cpu: 55.4% | mem: 44.5% | lat: 18.9 ms
2026-01-01 02:16:00 | memory | cpu: 61.6% | mem: 84.1% | lat: 12.6 ms
2026-01-01 02:19:00 | cpu | cpu: 74.6% | mem: 63.7% | lat: 22.0 ms
2026-01-01 02:33:00 | memory | cpu: 57.6% | mem: 47.0% | lat: 18.3 ms
2026-01-01 02:36:00 | memory | cpu: 60.7% | mem: 46.4% | lat: 18.1 ms

app-01 - RAW anomalies:
2026-01-01 00:01:00 | memory | cpu: 73.3% | mem: 89.3% | lat: 25.4 ms
2026-01-01 00:02:00 | memory | cpu: 69.5% | mem: 55.2% | lat: 28.2 ms
2026-01-01 00:05:00 | memory | cpu: 81.2% | mem: 92.6% | lat: 24.5 ms
2026-01-01 00:07:00 | memory | cpu: 64.7% | mem: 85.7% | lat: 27.6 ms
2026-01-01 00:16:00 | memory | cpu: 75.9% | mem: 85.8% | lat: 22.6 ms
2026-01-01 00:17:00 | memory | cpu: 69.6% | mem: 86.1% | lat: 31.5 ms
2026-01-01 00:19:00 | memory | cpu: 71.0% | mem: 55.5% | lat: 24.1 ms
2026-01-01 00:20:00 | memory | cpu: 74.0% | mem: 88.0% | lat: 29.8 ms
2026-01-01 00:21:00 | memory | cpu: 80.4% | mem: 89.9% | lat: 16.3 ms
2026-01-01 00:25:00 | memory | cpu: 71.7% | mem: 87.3% | lat: 26.0 ms
2026-01-01 00:26:00 | memory | cpu: 66.9% | mem: 96.0% | lat: 19.7 ms
2026-01-01 00:33:00 | memory | cpu: 69.1% | mem: 98.5% | lat: 16.5 ms
2026-01-01 00:34:00 | memory | cpu: 70.0% | mem: 95.9% | lat: 26.0 ms
2026-01-01 00:35:00 | memory | cpu: 78.0% | mem: 89.4% | lat: 28.4 ms
2026-01-01 00:37:00 | memory | cpu: 80.0% | mem: 86.6% | lat: 22.4 ms
2026-01-01 00:40:00 | memory | cpu: 70.7% | mem: 90.5% | lat: 25.2 ms
2026-01-01 00:42:00 | memory | cpu: 73.1% | mem: 85.4% | lat: 27.5 ms
2026-01-01 00:46:00 | cpu | cpu: 87.1% | mem: 78.8% | lat: 21.0 ms
2026-01-01 00:48:00 | latency | cpu: 66.9% | mem: 65.2% | lat: 13.9 ms
2026-01-01 00:49:00 | memory | cpu: 70.3% | mem: 94.8% | lat: 23.6 ms
2026-01-01 00:50:00 | memory | cpu: 63.2% | mem: 95.3% | lat: 20.3 ms
2026-01-01 00:51:00 | memory | cpu: 68.5% | mem: 91.6% | lat: 28.2 ms
2026-01-01 00:53:00 | memory | cpu: 79.2% | mem: 91.5% | lat: 26.6 ms
2026-01-01 00:56:00 | cpu | cpu: 59.1% | mem: 67.1% | lat: 24.2 ms
2026-01-01 01:02:00 | memory | cpu: 61.5% | mem: 96.0% | lat: 24.9 ms
2026-01-01 01:03:00 | memory | cpu: 63.2% | mem: 86.9% | lat: 18.7 ms
2026-01-01 01:08:00 | cpu | cpu: 89.4% | mem: 67.2% | lat: 24.5 ms
2026-01-01 01:16:00 | memory | cpu: 74.6% | mem: 88.0% | lat: 26.9 ms
2026-01-01 01:17:00 | memory | cpu: 69.7% | mem: 88.6% | lat: 27.6 ms
2026-01-01 01:18:00 | memory | cpu: 71.2% | mem: 88.3% | lat: 35.8 ms
2026-01-01 01:24:00 | memory | cpu: 74.8% | mem: 90.9% | lat: 20.9 ms
2026-01-01 01:25:00 | memory | cpu: 78.1% | mem: 89.0% | lat: 34.2 ms
2026-01-01 01:41:00 | memory | cpu: 61.5% | mem: 92.4% | lat: 28.7 ms
2026-01-01 01:43:00 | memory | cpu: 74.7% | mem: 56.8% | lat: 28.4 ms
2026-01-01 01:48:00 | memory | cpu: 70.2% | mem: 90.1% | lat: 30.0 ms
2026-01-01 01:49:00 | memory | cpu: 71.4% | mem: 51.3% | lat: 28.8 ms
2026-01-01 01:51:00 | memory | cpu: 72.9% | mem: 93.6% | lat: 28.3 ms
2026-01-01 01:53:00 | cpu | cpu: 56.6% | mem: 74.2% | lat: 18.6 ms
2026-01-01 01:57:00 | memory | cpu: 69.8% | mem: 92.3% | lat: 25.7 ms
2026-01-01 01:58:00 | memory | cpu: 61.5% | mem: 96.4% | lat: 26.2 ms
2026-01-01 02:00:00 | cpu, memory, latency | cpu: 95.0% | mem: 97.0% | lat: 120.0 ms
2026-01-01 02:01:00 | cpu, memory, latency | cpu: 98.0% | mem: 99.0% | lat: 145.0 ms
2026-01-01 02:02:00 | cpu, memory, latency | cpu: 93.0% | mem: 95.0% | lat: 118.0 ms
2026-01-01 02:06:00 | memory | cpu: 70.0% | mem: 100.0% | lat: 30.0 ms
2026-01-01 02:07:00 | memory | cpu: 79.8% | mem: 86.5% | lat: 20.7 ms
2026-01-01 02:09:00 | memory | cpu: 82.4% | mem: 87.7% | lat: 21.3 ms
2026-01-01 02:12:00 | memory | cpu: 82.5% | mem: 87.1% | lat: 22.8 ms
2026-01-01 02:25:00 | memory | cpu: 76.4% | mem: 86.3% | lat: 27.8 ms
2026-01-01 02:32:00 | memory | cpu: 67.8% | mem: 85.2% | lat: 18.7 ms
2026-01-01 02:40:00 | cpu | cpu: 58.3% | mem: 80.3% | lat: 24.1 ms
2026-01-01 02:41:00 | memory | cpu: 73.8% | mem: 87.5% | lat: 24.2 ms
2026-01-01 02:46:00 | memory | cpu: 68.5% | mem: 90.4% | lat: 28.3 ms
2026-01-01 02:48:00 | memory | cpu: 62.5% | mem: 53.0% | lat: 27.6 ms
2026-01-01 02:55:00 | memory | cpu: 73.4% | mem: 88.5% | lat: 24.7 ms
2026-01-01 02:57:00 | latency | cpu: 73.6% | mem: 69.4% | lat: 13.2 ms

db-01 - RAW anomalies:
2026-01-01 00:05:00 | memory | cpu: 50.9% | mem: 67.4% | lat: 12.6 ms
2026-01-01 00:06:00 | latency | cpu: 42.0% | mem: 53.6% | lat: 16.7 ms
2026-01-01 00:15:00 | cpu | cpu: 54.3% | mem: 61.9% | lat: 11.8 ms
2026-01-01 00:16:00 | latency | cpu: 44.2% | mem: 63.6% | lat: 16.6 ms
2026-01-01 00:19:00 | memory | cpu: 43.2% | mem: 43.7% | lat: 12.7 ms
2026-01-01 00:30:00 | cpu | cpu: 35.8% | mem: 55.0% | lat: 12.2 ms
2026-01-01 00:33:00 | latency | cpu: 46.8% | mem: 64.9% | lat: 7.5 ms
2026-01-01 00:36:00 | latency | cpu: 48.0% | mem: 48.1% | lat: 16.2 ms
2026-01-01 00:47:00 | memory | cpu: 48.3% | mem: 37.4% | lat: 9.3 ms
2026-01-01 00:49:00 | memory | cpu: 39.8% | mem: 33.1% | lat: 12.4 ms
2026-01-01 00:51:00 | cpu | cpu: 35.7% | mem: 57.7% | lat: 12.0 ms
2026-01-01 00:57:00 | memory | cpu: 50.3% | mem: 68.5% | lat: 9.7 ms
2026-01-01 01:08:00 | latency | cpu: 39.5% | mem: 60.5% | lat: 16.0 ms
2026-01-01 01:21:00 | latency | cpu: 46.3% | mem: 45.8% | lat: 6.5 ms
2026-01-01 01:33:00 | cpu | cpu: 53.3% | mem: 62.9% | lat: 9.7 ms
2026-01-01 01:34:00 | latency | cpu: 45.3% | mem: 54.3% | lat: 16.0 ms
2026-01-01 01:59:00 | cpu | cpu: 55.4% | mem: 58.7% | lat: 11.7 ms
2026-01-01 02:04:00 | memory | cpu: 44.8% | mem: 42.4% | lat: 10.1 ms
2026-01-01 02:06:00 | memory | cpu: 41.9% | mem: 41.9% | lat: 9.7 ms
2026-01-01 02:18:00 | latency | cpu: 37.0% | mem: 59.8% | lat: 7.6 ms
2026-01-01 02:24:00 | cpu | cpu: 33.1% | mem: 50.4% | lat: 11.8 ms
2026-01-01 02:26:00 | cpu, latency | cpu: 54.7% | mem: 51.8% | lat: 7.3 ms
2026-01-01 02:33:00 | memory | cpu: 44.7% | mem: 69.7% | lat: 10.5 ms
2026-01-01 02:56:00 | latency | cpu: 42.8% | mem: 62.9% | lat: 17.8 ms
2026-01-01 02:57:00 | memory | cpu: 49.6% | mem: 71.9% | lat: 8.4 ms
2026-01-01 02:58:00 | cpu | cpu: 35.4% | mem: 51.5% | lat: 12.6 ms
```


### 🔹 Correlated Incidents

```id="struct03"
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
```

### 🔹 Dashboard Summary

```id="struct04"
================ SUMMARY DASHBOARD ================
server     cpu_mean   mem_mean   lat_p95    raw_anomalies      correlated_incidents
------------------------------------------------------------------------------------------
web-01     60.2       64.4       23.2       11                 3
app-01     72.6       77.6       32.5       55                 3
db-01      44.9       55.4       15.0       26                 1
Saved: output/dashboard.csv

```
---

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
