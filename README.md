# Diabetes Prediction using SVM
This repository contains a project for predicting diabetes using a Support Vector Machine (SVM) model. The project includes a Jupyter notebook for training the model, a Python script for a Tkinter-based GUI application, and the dataset used for training and evaluation.

# Contents
diabetes-prediction-using-svm.ipynb: A Jupyter notebook that demonstrates the following:

Data loading and preprocessing
Model training using SVM
Model evaluation and performance metrics

main.py: A Python script that provides a graphical user interface (GUI) for predicting diabetes. Key features include:

Loading a pre-trained SVM model and scaler
Collecting user input for features like Pregnancies, Glucose, Blood Pressure, etc.
Displaying the prediction result (diabetic or non-diabetic)

diabetes.csv: The dataset used for training and evaluating the model. It includes the following columns:

Pregnancies
Glucose
BloodPressure
SkinThickness
Insulin
BMI
DiabetesPedigreeFunction
Age
Outcome (0: non-diabetic, 1: diabetic)

# Dataset
The dataset (diabetes.csv) contains data collected from the Pima Indian population. Each row represents a patient, and the columns contain medical predictor variables and one target variable (Outcome).

# Model
The SVM model is trained to predict the likelihood of diabetes based on the provided features. The model is saved using joblib and can be loaded for predictions in the GUI application.

# Acknowledgments
This project is based on the Pima Indians Diabetes Database, available on Kaggle.
