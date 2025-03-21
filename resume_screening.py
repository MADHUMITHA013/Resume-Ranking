# -*- coding: utf-8 -*-
"""RESUME SCREENING

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JpfThjgyioO6412wSf7LWg2VEb3j09kz
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

df = pd.read_csv("/content/archive (1).zip")

label_encoders = {}
categorical_columns = ["Education", "Certifications", "Job Role", "Recruiter Decision"]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

X = df[["Experience (Years)", "Education", "Certifications", "Projects Count", "AI Score (0-100)", "Salary Expectation ($)"]]
y = df["Recruiter Decision"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

def rank_resumes(job_role, top_n=10):
    job_role_encoded = label_encoders["Job Role"].transform([job_role])[0]
    relevant_resumes = df[df["Job Role"] == job_role_encoded]
    ranked_resumes = relevant_resumes.sort_values(by="AI Score (0-100)", ascending=False)
    return ranked_resumes.head(top_n)

job_role_to_rank = "Data Scientist"
top_resumes = rank_resumes(job_role_to_rank)
print(top_resumes)