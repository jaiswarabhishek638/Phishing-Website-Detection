from flask import Flask, request, render_template, jsonify
import joblib
import os

app = Flask(__name__)

# --- Dummy function to extract basic features from URL ---
def extract_features(url):
    return [len(url), url.count('.'), url.count('/'), url.count('-')]

# --- Load trained model if available ---
MODEL_PATH = 'model.pkl'
model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)

# --- Home route ---
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    if request.method == 'POST':
        url = request.form.get('url')

        if not url:
            prediction = "Please enter a URL."
        else:
            # Extract features
            features = [extract_features(url)]

            # Predict using ML model if available
            if model:
                result = model.predict(features)[0]
                prediction = "Phishing" if result == 1 else "Legitimate"
            else:
                # Dummy logic if no model
                if 'phishing' in url or len(url) > 50:
                    prediction = "Phishing"
                else:
                    prediction = "Legitimate"

    return render_template('index.html', predict=prediction)

# --- Optional: API route (for AJAX / JSON testing) ---
@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.get_json()
    url = data.get('url', '')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    features = [extract_features(url)]
    prediction = "Phishing" if 'phishing' in url or len(url) > 50 else "Legitimate"
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)