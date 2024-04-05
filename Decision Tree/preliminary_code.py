import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import tkinter as tk
from tkinter import messagebox

#loading data system
data = pd.read_csv('survey_data.csv')
label_encoders = {}
for column in ['who', 'how', 'why']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

X = data[['who', 'how', 'why']]
y = data['replaced']  #involve a binary replacement survey

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#simple decision tree clasifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

def predict_replacement(who, how, why):
    inputs = pd.DataFrame([[who, how, why]], columns=['who', 'how', 'why'])
    for column, le in label_encoders.items():
        inputs[column] = le.transform(inputs[column])
    prediction = model.predict(inputs)
    return "Replaces" if prediction[0] else "Does not replace"

#gui of the model
def on_predict():
    who = who_var.get()
    how = how_var.get()
    why = why_var.get()
    result = predict_replacement(who, how, why)
    messagebox.showinfo("Prediction", result)

root = tk.Tk()
root.title("Toilet Paper Replacement Predictor")

who_var = tk.StringVar()
how_var = tk.StringVar()
why_var = tk.StringVar()

tk.Label(root, text="Who:").pack()
tk.Entry(root, textvariable=who_var).pack()
tk.Label(root, text="How:").pack()
tk.Entry(root, textvariable=how_var).pack()
tk.Label(root, text="Why:").pack()
tk.Entry(root, textvariable=why_var).pack()

tk.Button(root, text="Predict", command=on_predict).pack()

root.mainloop()