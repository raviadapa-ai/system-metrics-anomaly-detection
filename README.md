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

```id="out01"
web-01
 CPU : mean=59.7, std=4.3, p95=66.8
 MEM : mean=63.9, std=7.9, p95=77.9
 LAT : mean=17.9, std=3.0, p95=22.8
```

---

### 🔹 Anomaly Detection

```id="out02"
web-01
cpu alerts     : [45, 46, 47]
memory alerts  : [45, 46, 47]
latency alerts : [45, 46, 47]
```

---

### 🔹 Correlated Incidents

```id="out03"
web-01 - CONFIRMED INCIDENTS:
minute 45 | cpu: 91.0% | mem: 92.0% | lat: 85 ms
```

---

### 🔹 Dashboard Summary

| Server | CPU Mean | Mem Mean | Latency P95 | Incidents |
| ------ | -------- | -------- | ----------- | --------- |
| web-01 | 60.2     | 64.4     | 23.2        | 11        |
| app-01 | 72.6     | 77.6     | 32.5        | 55        |
| db-01  | 44.9     | 55.4     | 15.0        | 26        |

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
