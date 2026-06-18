from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# 1. Initialize the FastAPI App
app = FastAPI(title="D2C Churn Prediction API", version="1.0")

# 2. Load the AI Brain dynamically based on where this file lives
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
try:
    pipeline = joblib.load(MODEL_PATH)
except FileNotFoundError:
    pipeline = None

# 3. Define the strict Data Schema for incoming website requests
class CustomerData(BaseModel):
    city_tier: str
    age_group: str
    acquisition_channel: str
    loyalty_tier: str
    preferred_category: str
    skin_type: str
    marketing_consent: int
    recency_days: int
    frequency_180d: int
    monetary_180d: float
    return_rate_180d: float
    avg_discount_pct_180d: float
    avg_rating_180d: float
    category_diversity_180d: int
    ticket_count_90d: int
    negative_ticket_rate_90d: float
    avg_resolution_hours_90d: float
    days_since_signup: int
    sessions_30d: int
    product_views_30d: int
    cart_adds_30d: int
    wishlist_adds_30d: int
    abandoned_carts_30d: int
    email_opens_30d: int
    campaign_clicks_30d: int
    last_visit_days_ago: int

# 4. Create the Prediction Endpoint
@app.post("/predict")
def predict_churn(customer: CustomerData):
    if pipeline is None:
        raise HTTPException(status_code=500, detail="Model file not found. API cannot serve predictions.")
    
    # Convert the validated JSON payload into a Pandas DataFrame (1 row)
    df = pd.DataFrame([customer.dict()])
    
    # Predict
    prediction = pipeline.predict(df)[0]
    probability = pipeline.predict_proba(df)[0][1]
    
    status = "High Risk (Will Churn)" if prediction == 1 else "Safe (Retained)"
    
    return {
        "prediction": status,
        "churn_probability": round(probability, 4)
    }

# 5. Create a simple Health Check endpoint
@app.get("/")
def health_check():
    return {"status": "API is live and model is loaded."}


