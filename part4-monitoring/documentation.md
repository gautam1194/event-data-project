# Part 4: Production Monitoring Documentation

## Overview
This monitoring system ensures the correctness of daily event ingestion and transformation logic. It is designed to detect anomalies similar to those identified in the 14-day dataset (notably the complete absence of purchase events).

---

# What We Monitor and Why

## 1. Event Volume Monitoring
We track:
- Total events per day
- Total sessions per day
- Event counts by type (page_viewed, add_to_cart, checkout_started, purchase)

Why:
- Sudden drops (e.g., purchase events = 0) indicate tracking failures.
- Sudden spikes may indicate duplication or bot traffic.

## 2. Schema & Field Health
- Missing columns
- Null spikes in client_id, timestamp, event_name
- Malformed JSON in event_data

Why:
- Schema drift is the #1 cause of pipeline failures.

## 3. Funnel Health Monitoring
- ATC → Checkout → Purchase conversion flow
- Daily conversion rate trends
- Alerts triggered if revenue events drop below expected range

Why:
- Detect failures in checkout or payment systems early.

## 4. Traffic Source Distribution
- Distribution of utm sources
- Direct vs search vs internal

Why:
- Sudden source skew often indicates broken UTM tracking.

## 5. Session Integrity Monitoring
- Average session length
- Page depth
- Device breakdown

Why:
- UX issues often show up as changes in dwell time or device mix.

---

# Detection Logic

## 1. Anomaly Detection
Examples:
- purchase events < threshold (e.g., <1 for the day)
- total events drop >50% vs 7-day average
- client_id nulls >0
- invalid timestamps detected

## 2. Threshold Strategy
### Critical Alerts:
- purchase events = 0  
- timestamp errors >0  
- missing event_name values  
- >20% spike in duplicates  

### Warning Alerts:
- Daily event count ±20% from 7-day moving average  
- Page views drop >25%  

## 3. Alerting Mechanisms
- Simple cron-based Python/SQL job
- Slack/email notifications
- Error logs stored in monitoring_results table

---

# Would This Monitoring Catch the Real Issues Seen in the Dataset?

### Yes — specifically:
## 1. Zero purchase events
This monitoring system immediately raises a **critical alert**.

## 2. Normal pageview/ATC/checkout but missing conversions
This highly abnormal funnel pattern triggers:
- Funnel drop-off alert
- Purchase anomaly alert

## 3. Timestamp issues
None were found, but if present, monitoring would catch them.

## 4. Schema issues
All fields validated; monitoring protects against future regressions.

---

# Is the Detection Methodology Sound?
Yes, because:
- It uses historical baselines (7-day rolling)
- Combines threshold-based and anomaly-detection methods
- Distinguishes “Warning” vs “Critical” to reduce alert fatigue

---

# Practical for Daily Operations?
Absolutely:
- Lightweight SQL checks
- Runs in <5 seconds
- Easy integrations (Airflow, dbt, Dagster, n8n)
- Clear actionable alert messages

---
