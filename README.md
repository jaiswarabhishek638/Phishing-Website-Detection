# Hackathon Projects

# 🎣 Phishing Website Detection

A Flask web app that predicts whether a URL is **phishing** or **legitimate**, using a machine learning model trained on URL-based features.

## Overview

The app exposes a simple web form where a user submits a URL. The backend extracts features from the URL and feeds them into a trained `RandomForestClassifier` to classify the site as **Phishing** or **Legitimate**. A JSON API endpoint is also available for programmatic/AJAX use.

## Tech Stack

- **Backend:** Flask
- **ML:** scikit-learn (Random Forest), pandas, numpy, joblib
- **Frontend:** HTML, Tailwind CSS, Bootstrap 5, vanilla JS
- **Deployment:** Gunicorn-ready

## Project Structure

```
.
├── app.py                  # Flask app: web routes + JSON API
├── train_model.py          # Trains the RandomForest model on the dataset
├── dataset_phishing.csv    # Labeled dataset of phishing/legitimate URLs
├── templates/
│   └── index.html          # Main UI (Tailwind + Bootstrap)
├── static/
│   ├── style.css
│   └── script.js
└── requirements.txt
```

> **Note:** Place `index.html` inside a `templates/` folder and `style.css` / `script.js` inside a `static/` folder for Flask to serve them correctly.

## Dataset

`dataset_phishing.csv` contains ~11,430 labeled URL samples with 87 engineered features (URL length, hostname length, character counts, digit ratios, etc.) and a `status` column (`legitimate` / `phishing`).

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model
```bash
python train_model.py
```
This reads `dataset_phishing.csv`, trains a `RandomForestClassifier`, and saves it as `phishing_model.pkl`.

> ⚠️ `app.py` currently looks for a model file named `model.pkl`, while `train_model.py` saves `phishing_model.pkl`. Rename/copy the file (or update `MODEL_PATH` in `app.py`) so the app can find it:
> ```bash
> cp phishing_model.pkl model.pkl
> ```

### 5. Run the app
```bash
python app.py
```
Visit **http://localhost:5000** in your browser.

## Usage

- **Web UI:** Enter a URL in the form and submit to get a prediction.
- **API:** `POST /predict` with JSON body:
  ```json
  { "url": "http://example.com" }
  ```
  Response:
  ```json
  { "prediction": "Legitimate" }
  ```

## Known Limitations

- If no trained model (`model.pkl`) is found, the app falls back to a naive rule (checks for the word "phishing" in the URL or URL length > 50) — this is a placeholder, not a real detector.
- The `/` and `/predict` routes currently use **different** feature-extraction logic — the web form route can use the trained model's features, while `/predict` still uses the fallback rule. Align both routes to use the same `extract_features` pipeline that matches the features used in `train_model.py` for consistent results.
- `extract_features()` in `app.py` is a placeholder returning only 4 basic features; it should be updated to compute the same 14 features (`length_url`, `length_hostname`, `nb_dots`, etc.) used during training.

## Roadmap / Ideas

- [ ] Align feature extraction between training and inference
- [ ] Add model evaluation metrics (accuracy, precision, recall) to `train_model.py`
- [ ] Add input validation and error handling for malformed URLs
- [ ] Dockerize the app for easier deployment
- [ ] Deploy to Render/Heroku/Railway using Gunicorn

## License

This project is open source and available under the [MIT License](LICENSE).
