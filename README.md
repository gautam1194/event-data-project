# Event Data Project

This repository contains code and documentation for a 14-day e-commerce event dataset analysis project.

## Folder Overview
- **part1-data-quality/**: Validates incoming raw event data.
- **part2-transformation/**: Transforms raw events into analytics-ready tables.
- **part3-analysis/**: Executive summary and supporting analysis.
- **part4-monitoring/**: Daily monitoring of key metrics in production.

## How to Run
1. Install dependencies: `pip install pandas numpy`
2. Place all 14 event CSV files in the project root:
events_20250223.csv
events_20250224.csv
...
events_20250308.csv
3. Run data quality checks: `python part1-data-quality/data_quality_check.py`
4. Run transformation pipeline: `python part2-transformation/transform_pipeline.py`
5. Run monitoring checks: `python part4-monitoring/monitoring.py`

## AI Usage Description

In this project, I leveraged AI in multiple stages to streamline the data pipeline, improve accuracy, and accelerate insights. AI was not just a black-box tool; I integrated it thoughtfully to make it my own solution tailored for e-commerce event data

### 1. Data Quality Framework (Part 1)
AI helped in pattern recognition and anomaly detection within the raw event data: Automated detection of irregularities and Custom validation logic
By combining AI insights with Python code, I created a data quality framework that can detect both known and potential future issues, making the pipeline robust before data enters analytics.

### 2. Transformation Pipeline (Part 2)
AI helped determine practical sessionization approaches given anonymized client_id and event patterns
This enabled me to convert 14 days of raw, unstructured events into actionable analytics tables, ready for marketing insights and attribution modeling.

### 3. Business Analysis (Part 3)
AI assisted in interpreting trends and summarizing business insights: Pattern recognition in user behavior and Marketing attribution insights

### 4. Monitoring & Production Readiness (Part 4)
AI informed the design of monitoring logic for production pipelines: Suggested key business-critical metrics to monitor daily (sessions, total events, anomalies in traffic).
Provided threshold-setting strategies to distinguish between normal fluctuations and actual issues, reducing false alerts.

## How I Made It My Own

I customized AI recommendations to suit the specific data schema, event types, and business context of this e-commerce dataset.
Rather than blindly applying models, I translated AI insights into maintainable, production-ready Python scripts, integrating all 14 daily files.

I used ChatGPT, helping me identify gaps in traditional ETL approaches, propose improvements, and guide decisions around sessionization, attribution, and monitoring logic.

### Every AI suggestion was interpreted and adapted—for example, AI suggested anomaly detection strategies, but I implemented them using Pandas and Python for full transparency and control.

Result: The final pipeline is scalable, auditable, and tailored to the company’s marketing analytics needs, while still leveraging AI guidance for best practices.
