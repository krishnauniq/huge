from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "🌱 JeeVan API is live and running!"

# ================= PREDICTION ROUTE =================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Extract values from request
        N = float(data.get("N", 0))
        P = float(data.get("P", 0))
        K = float(data.get("K", 0))
        temperature = float(data.get("temperature", 0))
        humidity = float(data.get("humidity", 0))
        ph = float(data.get("ph", 0))
        rainfall = float(data.get("rainfall", 0))

        # 👉 Here you should load your ML model
        # For now, I’ll just create a simple dummy rule-based logic
        if ph < 5.5:
            crop = "Potato"
        elif temperature > 30 and rainfall > 200:
            crop = "Rice"
        elif N > 100:
            crop = "Maize"
        else:
            crop = "Wheat"

        return jsonify({"recommended_crop": crop})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
