# AI-Powered Cybersecurity Threat Detection System

> Student project — industry-aligned, GitHub-ready, uses public datasets + virtual simulation.

## Overview
Detects network intrusion, DoS, brute-force, and anomalies using Isolation Forest + Random Forest on simulated traffic data.

## Problem Statement
Cyber attacks cost companies billions. Traditional rule-based IDS miss new patterns. AI learns normal behavior and flags deviations in real time.

## Industry Relevance
- Banks: fraud + account takeover detection
- IT / SaaS: intrusion prevention (IDS/IPS)
- Product companies: security dashboards (SIEM)

## Tech Stack
Python 3.10 | Pandas | NumPy | Scikit-learn | Matplotlib | Seaborn

## Architecture
```
Data (CSV) → Preprocess → Features → Isolation Forest / RF → Prediction → Alert CSV + Charts
```

## Dataset
KDD Cup 99 / UNSW-NB15 (public). Columns: duration, protocol, service, src_bytes, dst_bytes, flag, label (normal / DoS / probe / R2L).

## Installation
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## How to Run
```bash
python main.py
```
Produces: `outputs/alerts.csv`, `outputs/anomaly_plot.png`, `outputs/confusion_matrix.png`

## Results (Expected)
- Accuracy: ~92-96% (Random Forest on balanced sample)
- Anomaly detection: flags outliers with scores > threshold
- Confusion matrix: Normal vs Attack classification

## Screenshots / Proof
See `images/` folder for dataset preview, confusion matrix, and alert charts.

## Learning Outcomes
- Data preprocessing for security data
- Feature engineering for network flows
- Unsupervised (Isolation Forest) + supervised (Random Forest)
- Evaluation: accuracy, precision, recall, F1
- Visualization of threat patterns
- Professional GitHub repo structure

## Project Structure
```
AI-Cybersecurity-Threat-Detection/
├── data/
├── notebooks/
├── src/
├── models/
├── outputs/
├── images/
├── docs/
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---
Built by a student for placement / internship proof of work.
