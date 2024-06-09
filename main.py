import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
import joblib

# Load the trained model and scaler
classifier = joblib.load('classifier_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict_diabetes():
    try:
        input_data = (
            int(entry_pregnancies.get()),
            float(entry_glucose.get()),
            float(entry_blood_pressure.get()),
            float(entry_skin_thickness.get()),
            float(entry_insulin.get()),
            float(entry_bmi.get()),
            float(entry_dpf.get()),
            int(entry_age.get())
        )
        
        input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
        input_data_df = pd.DataFrame(input_data_as_numpy_array, columns=[
            'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
        ])
        std_data = scaler.transform(input_data_df)
        
        prediction = classifier.predict(std_data)
        
        if prediction[0] == 0:
            messagebox.showinfo("Result", "The person is not diabetic")
        else:
            messagebox.showinfo("Result", "The person is diabetic")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create the main window
root = tk.Tk()
root.title("Diabetes Prediction")

# Create and place the input fields
labels = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

(entry_pregnancies, entry_glucose, entry_blood_pressure, entry_skin_thickness, entry_insulin, entry_bmi, entry_dpf, entry_age) = entries

# Create and place the Predict button
predict_button = tk.Button(root, text="Predict", command=predict_diabetes)
predict_button.grid(row=len(labels), columnspan=2, pady=20)

# Start the GUI event loop
root.mainloop()
