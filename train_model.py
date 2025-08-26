# student_regression.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("data/StudentPerformanceFactors.csv")

# Features and Target (Exam_Score is the target now)
X = data.drop("Exam_Score", axis=1)   # independent variables
y = data["Exam_Score"]                # dependent variable

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "student_model.pkl")

print("✅ Model trained and saved successfully as student_model.pkl")
