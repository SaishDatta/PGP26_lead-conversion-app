from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load trained model
model = joblib.load("best_lead_conversion_model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return "Lead Conversion Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Convert input JSON to DataFrame
    input_df = pd.DataFrame([data])

    # Predict probability
    probability = model.predict_proba(input_df)[0][1]

    return jsonify({
        "conversion_probability": round(probability, 4)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
