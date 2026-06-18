from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Test if the API is successfully running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API is live and model is loaded."}

def test_predict_endpoint():
    """Test if the model successfully predicts churn for a valid JSON payload."""
    # A dummy payload mimicking our previous manual test
    payload = {
        "city_tier": "Tier 1",
        "age_group": "25-34",
        "acquisition_channel": "Google Search",
        "loyalty_tier": "Not Enrolled",
        "preferred_category": "Baby Care",
        "skin_type": "Unknown",
        "marketing_consent": 1,
        "recency_days": 26,
        "frequency_180d": 1,
        "monetary_180d": 450.00,
        "return_rate_180d": 0.0,
        "avg_discount_pct_180d": 0.15,
        "avg_rating_180d": 3.0,
        "category_diversity_180d": 1,
        "ticket_count_90d": 0,
        "negative_ticket_rate_90d": 0.0,
        "avg_resolution_hours_90d": 0.0,
        "days_since_signup": 30,
        "sessions_30d": 1,
        "product_views_30d": 2,
        "cart_adds_30d": 0,
        "wishlist_adds_30d": 0,
        "abandoned_carts_30d": 0,
        "email_opens_30d": 0,
        "campaign_clicks_30d": 0,
        "last_visit_days_ago": 26
    }
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "churn_probability" in data
    assert type(data["churn_probability"]) == float