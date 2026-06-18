# ML Model Monitoring & Maintenance Plan

## 1. Overview
Deploying the `model.pkl` artifact via FastAPI is only the first phase. In production, predictive models naturally degrade due to changes in consumer behaviour, macroeconomic factors, or marketing campaign shifts. This document outlines our strategy to monitor the D2C Churn Predictor post-deployment.

## 2. Drift Detection Metrics
We will actively monitor the incoming payload data to the API for two types of drift:

### A. Data Drift (Feature Drift)
We will log the distributions of incoming API requests and compare them to our September 2025 training baseline. Alerts will trigger if:
* **Missing Values:** The rate of `Unknown` values in `skin_type` exceeds 25%.
* **Numeric Shifts:** The median `monetary_180d` value drops or spikes by more than 15% (indicating a change in pricing or a new type of low-intent customer traffic).
* **Categorical Shifts:** The proportion of traffic from "Google Search" suddenly spikes above the historical training baseline.

### B. Concept Drift (Target Drift)
The relationship between our features and actual churn may change (e.g., if we release a vastly improved mobile app, `last_visit_days_ago` might become a less lethal predictor of churn). We will measure this by calculating the actual ground-truth churn rate of the API-scored customers after 60 days have passed, comparing the model's expected precision against actual retention rates.

## 3. Performance Logging
All POST requests to the `/predict` endpoint will be logged asynchronously to a data warehouse (e.g., Snowflake or BigQuery) with the following schema:
* `timestamp`
* `customer_id` (if provided)
* `input_features` (JSON string)
* `predicted_probability`
* `api_latency_ms`

## 4. Retraining Schedule
* **Cadence:** The model will undergo a forced retraining cycle every **90 days**.
* **Trigger-Based:** If API monitoring detects severe Data Drift (e.g., a massive influx of a new `acquisition_channel` like TikTok that the model has never seen), an emergency retraining will be triggered using the most recent 30 days of data.