# OptiCrop - Model Training Code
# Run this in Google Colab or Jupyter Notebook
# Dataset: Crop_recommendation.csv (Kaggle - Crop Recommendation Dataset)
# Columns: N, P, K, temperature, humidity, ph, rainfall, label

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Step 1: Load the dataset
df = pd.read_csv("Crop_recommendation.csv")
print("Dataset shape:", df.shape)
print(df.head())

# Step 2: Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Step 3: Check class distribution
print("\nCrop classes:\n", df['label'].value_counts())

# Step 4: Split features and target
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 6: Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 7: Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 8: Save the trained model
pickle.dump(model, open("model.pkl", "wb"))
print("\nModel saved as model.pkl")
