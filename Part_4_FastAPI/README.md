# 🚀 Part 4: Model Deployment (FastAPI)

## 📖 Overview
This folder contains the final, production-ready deployment of the D2C Churn Prediction model. We transitioned the machine learning pipeline from a Jupyter Notebook environment into a robust, strictly-typed REST API using **FastAPI**. 

This API is designed to receive real-time JSON payloads from a website frontend, process the data through our saved Scikit-Learn `Pipeline`, and return a real-time churn probability score.

---

## 💾 Data Setup
To run this repository locally, you will need to map the original dataset:
1. Download the dataset from this [Google Drive Link](https://drive.google.com/drive/folders/1PmLapJI1VSDgvl_AxARNKwM1MCd3WFX0?usp=sharing).
2. Place the downloaded `.csv` files inside a folder named `data/` in the root directory of this project.

---

## 📁 Directory Structure
```text
Part_4_FastAPI/
├── app/
│   ├── main.py             # The core FastAPI application and endpoints
│   └── model.pkl           # The exported ML pipeline (Preprocessor + Random Forest)
├── tests/
│   └── test_api.py         # Automated pytest suite for the API endpoints
├── monitoring_plan.md      # Strategy for detecting data/concept drift in production
├── requirements.txt        # Python dependencies
└── README.md               # This file

# ⚡ Quick Start Guide

---
## 1. Install Dependencies

Ensure you have Python installed and your virtual environment activated. Install the required packages:

Bash
pip install -r requirements.txt

## 2. Run the Automated Tests

Before launching the server, verify the API endpoints and model integration are functioning properly by running the test suite:

Bash
```
python -m pytest tests/test_api.py -v
```
or  for not seeing warnings
```
python -m pytest tests/test_api.py -v --disable-warnings
```
## 3. Launch the Live Server

Start the Uvicorn server to host the API locally:

Bash
```
uvicorn app.main:app --reload