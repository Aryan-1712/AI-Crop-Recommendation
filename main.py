import tkinter as tk
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset and model
df = pd.read_csv("Crop_recommendation.csv")
model = pickle.load(open('crop_recommendation_model.pkl', 'rb'))

# Main GUI window
root = tk.Tk()
root.title("🌾 AI Crop Recommendation System")
root.geometry("450x550")
root.configure(bg="#e8f5e9")

# Title
tk.Label(root, text="🌾 Crop Recommendation System", font=("Arial", 16, "bold"),
         bg="#81c784", fg="white").pack(pady=10)

# Input fields
labels = ["Nitrogen (N)", "Phosphorus (P)", "Potassium (K)",
          "Temperature (°C)", "Humidity (%)", "pH Value", "Rainfall (mm)"]
entries = []

for label in labels:
    frame = tk.Frame(root, bg="#e8f5e9")
    frame.pack(pady=3)
    tk.Label(frame, text=label, width=20, anchor="w", bg="#e8f5e9").pack(side="left", padx=5)
    entry = tk.Entry(frame, width=10)
    entry.pack(side="left", padx=5)
    entries.append(entry)

# Functions
def predict_crop():
    try:
        values = [float(entry.get()) for entry in entries]
        sample = np.array([values])
        prediction = model.predict(sample)[0]
        result_label.config(text=f"🌱 Recommended Crop: {prediction}", fg="#2e7d32", font=("Arial", 12, "bold"))
    except ValueError:
        result_label.config(text="⚠️ Please enter valid numeric values.", fg="red", font=("Arial", 11, "bold"))

def clear_fields():
    for entry in entries:
        entry.delete(0, tk.END)
    result_label.config(text="")

def plot_crop_distribution():
    plt.figure(figsize=(10,5))
    sns.countplot(data=df, x='label', palette='viridis', order=df['label'].value_counts().index)
    plt.title("Crop Distribution in Dataset")
    plt.xticks(rotation=45)
    plt.xlabel("Crops")
    plt.ylabel("Number of Samples")
    plt.tight_layout()
    plt.show()

def plot_feature_importance():
    importances = model.feature_importances_
    features = df.columns[:-1]
    importance_df = pd.DataFrame({'Feature': features, 'Importance': importances})
    plt.figure(figsize=(8,5))
    sns.barplot(x='Importance', y='Feature', data=importance_df, palette='magma')
    plt.title("Feature Importance for Crop Prediction")
    plt.tight_layout()
    plt.show()

# Buttons
tk.Button(root, text="Predict Crop", command=predict_crop, bg="#388e3c", fg="white",
          font=("Arial", 12, "bold"), width=20).pack(pady=10)

tk.Button(root, text="Clear All", command=clear_fields, bg="#c62828", fg="white",
          font=("Arial", 11, "bold"), width=20).pack(pady=5)

tk.Button(root, text="Show Crop Distribution", command=plot_crop_distribution, bg="#1976d2", fg="white",
          font=("Arial", 11, "bold"), width=25).pack(pady=5)

tk.Button(root, text="Show Feature Importance", command=plot_feature_importance, bg="#f57c00", fg="white",
          font=("Arial", 11, "bold"), width=25).pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", bg="#e8f5e9", font=("Arial", 12))
result_label.pack(pady=10)

# Footer
tk.Label(root, text="Developed by Aryan Sharma", font=("Arial", 9), bg="#e8f5e9", fg="gray").pack(side="bottom", pady=10)

# Run GUI
root.mainloop()

#Sample input : 90, 42, 43, 20.8, 82, 6.5, 200