import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Initialize label encoders and the model globally
label_encoders = {column: LabelEncoder() for column in ['who', 'how', 'why']}
model = DecisionTreeClassifier()

# Define the GUI styling
style = ttk.Style()
style.theme_use('clam')  # Using 'clam' theme for a more modern look
style.configure('TButton', font=('Helvetica', 11), padding=5)
style.configure('TLabel', font=('Helvetica', 11), padding=5)
style.configure('TCombobox', font=('Helvetica', 11), padding=5)

# Function definitions as previously described...

def load_data(filepath):
    # Loading data
    data = pd.read_csv(filepath)

    # Ensure you have no duplicates and sort the values for better UX in the dropdown
    unique_who = sorted(data['who'].unique())
    unique_how = sorted(data['how'].unique())
    unique_why = sorted(data['why'].unique())

    # Encoding the labels
    for column, le in label_encoders.items():
        data[column] = le.fit_transform(data[column])

    X = data[['who', 'how', 'why']]
    y = data['replaced']

    # Splitting data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Decision tree classifier
    model.fit(X_train, y_train)

    return unique_who, unique_how, unique_why

def predict_replacement(who, how, why):
    # Map the string inputs back to the encoded labels
    who_encoded = label_encoders['who'].transform([who])[0]
    how_encoded = label_encoders['how'].transform([how])[0]
    why_encoded = label_encoders['why'].transform([why])[0]
    inputs = pd.DataFrame([[who_encoded, how_encoded, why_encoded]], columns=['who', 'how', 'why'])
    prediction = model.predict(inputs)
    return "Replaces" if prediction[0] else "Does not replace"

# GUI for the model
def on_predict():
    who = who_cb.get()
    how = how_cb.get()
    why = why_cb.get()
    result = predict_replacement(who, how, why)
    messagebox.showinfo("Prediction", result)

def update_comboboxes(who, how, why):
    who_cb['values'] = who
    how_cb['values'] = how
    why_cb['values'] = why
    who_cb.set('Select')
    how_cb.set('Select')
    why_cb.set('Select')

def load_csv():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        unique_who, unique_how, unique_why = load_data(filepath)
        update_comboboxes(unique_who, unique_how, unique_why)

# GUI for the model
root = tk.Tk()
root.title("Toilet Paper Replacement Predictor")

# Set a minimum window size
root.minsize(300, 200)

# Creating a frame for the comboboxes
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill='x')

# Adding labels and comboboxes to the frame with padding for a better layout
ttk.Label(input_frame, text="Who:").pack(side='top', fill='x')
who_cb = ttk.Combobox(input_frame)
who_cb.pack(side='top', fill='x', pady=5)

ttk.Label(input_frame, text="How:").pack(side='top', fill='x')
how_cb = ttk.Combobox(input_frame)
how_cb.pack(side='top', fill='x', pady=5)

ttk.Label(input_frame, text="Why:").pack(side='top', fill='x')
why_cb = ttk.Combobox(input_frame)
why_cb.pack(side='top', fill='x', pady=5)

# Creating a frame for the buttons
button_frame = ttk.Frame(root, padding="10")
button_frame.pack(fill='x')

# Adding buttons to the button frame
predict_button = ttk.Button(button_frame, text="Predict", command=on_predict)
predict_button.pack(side='left', expand=True, pady=10)

load_button = ttk.Button(button_frame, text="Load CSV", command=load_csv)
load_button.pack(side='left', expand=True, pady=10)

# Credits Label
credits_label = tk.Label(
    root,
    text="Credits: P&G, UC IRiS Team (Jay Arms, Nate Morehouse, Drielly Queiroga)",
    font=('Helvetica', 8),
    pady=10
)
credits_label.pack(side='bottom', fill='x')

root.mainloop()


'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Initialize label encoders globally
label_encoders = {column: LabelEncoder() for column in ['who', 'how', 'why']}
model = DecisionTreeClassifier()

def load_data(filepath):
    # Loading data
    data = pd.read_csv(filepath)

    # Ensure you have no duplicates and sort the values for better UX in the dropdown
    unique_who = sorted(data['who'].unique())
    unique_how = sorted(data['how'].unique())
    unique_why = sorted(data['why'].unique())

    # Encoding the labels
    for column, le in label_encoders.items():
        data[column] = le.fit_transform(data[column])

    X = data[['who', 'how', 'why']]
    y = data['replaced']

    # Splitting data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Decision tree classifier
    model.fit(X_train, y_train)

    return unique_who, unique_how, unique_why

def predict_replacement(who, how, why):
    # Map the string inputs back to the encoded labels
    who_encoded = label_encoders['who'].transform([who])[0]
    how_encoded = label_encoders['how'].transform([how])[0]
    why_encoded = label_encoders['why'].transform([why])[0]
    inputs = pd.DataFrame([[who_encoded, how_encoded, why_encoded]], columns=['who', 'how', 'why'])
    prediction = model.predict(inputs)
    return "Replaces" if prediction[0] else "Does not replace"

# GUI for the model
def on_predict():
    who = who_cb.get()
    how = how_cb.get()
    why = why_cb.get()
    result = predict_replacement(who, how, why)
    messagebox.showinfo("Prediction", result)

def update_comboboxes(who, how, why):
    who_cb['values'] = who
    how_cb['values'] = how
    why_cb['values'] = why
    who_cb.set('Select')
    how_cb.set('Select')
    why_cb.set('Select')

def load_csv():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        unique_who, unique_how, unique_why = load_data(filepath)
        update_comboboxes(unique_who, unique_how, unique_why)

root = tk.Tk()
root.title("Toilet Paper Replacement Predictor")

# Creating comboboxes
who_cb = ttk.Combobox(root)
how_cb = ttk.Combobox(root)
why_cb = ttk.Combobox(root)

tk.Label(root, text="Who:").pack()
who_cb.pack()

tk.Label(root, text="How:").pack()
how_cb.pack()

tk.Label(root, text="Why:").pack()
why_cb.pack()

tk.Button(root, text="Predict", command=on_predict).pack()
tk.Button(root, text="Load CSV", command=load_csv).pack()

root.mainloop()
'''