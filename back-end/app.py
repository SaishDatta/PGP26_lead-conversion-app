from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Load trained model
model = joblib.load("best_lead_conversion_model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return "Lead Conversion Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Create base dataframe
        input_df = pd.DataFrame([{
            "age": data["age"],
            "website_visits": data["website_visits"],
            "time_spent_on_website": data["time_spent_on_website"],
            "page_views_per_visit": data["page_views_per_visit"],
            "profile_completed": data["profile_completed"],
            "print_media_type1": data["print_media_type1"],
            "print_media_type2": data["print_media_type2"],
            "digital_media": data["digital_media"],
            "educational_channels": data["educational_channels"],
            "referral": data["referral"],
            "current_occupation": data["current_occupation"],
            "first_interaction": data["first_interaction"],
            "last_activity": data["last_activity"]
        }])

        # ✅ ADD FEATURE ENGINEERING (IMPORTANT)
        input_df["log_website_visits"] = np.log1p(input_df["website_visits"])
        input_df["log_time_spent"] = np.log1p(input_df["time_spent_on_website"])

        probability = model.predict_proba(input_df)[0][1]

        return jsonify({
            "conversion_probability": round(float(probability), 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
