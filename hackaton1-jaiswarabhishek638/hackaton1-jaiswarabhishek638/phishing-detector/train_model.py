import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
df = pd.read_csv('phishing_extract/dataset_phishing.csv')

# Select a subset of features
features = [
    'length_url', 'length_hostname', 'nb_dots', 'nb_hyphens', 'nb_at', 'nb_qm', 
    'nb_and', 'nb_eq', 'nb_underscore', 'nb_slash', 'nb_www', 'nb_com', 
    'ratio_digits_url', 'ratio_digits_host'
]

# Separate features (X) and target (y)
X = df[features]
y = df['status']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'phishing_model.pkl')

print("Model trained and saved as phishing_model.pkl")