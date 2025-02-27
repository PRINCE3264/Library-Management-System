import re
import requests
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tkinter import Tk, Label, Button, Entry, messagebox

# Function to extract features from URL
def extract_url_features(url):
    features = []
    features.append(len(url))  # URL length
    features.append(1 if "https" in url else 0)  # Check if URL is HTTPS
    features.append(1 if re.search(r"login|verify|bank|account|signin", url) else 0)  # Suspicious keywords
    features.append(1 if "www" in url else 0)  # Check if URL contains 'www'
    features.append(1 if re.search(r"@|%40", url) else 0)  # Check if URL contains '@'
    features.append(1 if url.count(".") > 2 else 0)  # Check if URL has more than 2 dots (subdomain level)
    
    return features

# Function to train the phishing detection model
def train_model():
    # Load the dataset (replace this with your actual phishing dataset)
    # Example dataset format: URL, Label
    # 0 for phishing, 1 for safe
    data = pd.read_csv("phishing_data.csv")  # Assuming the dataset has columns 'url' and 'label'
    
    # Extract features and labels from the dataset
    X = [extract_url_features(url) for url in data['url']]
    y = data['label']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the RandomForest model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

    return model

# Function to detect phishing
def detect_phishing(model, url):
    features = extract_url_features(url)
    prediction = model.predict([features])
    
    if prediction == 0:
        return "Phishing website detected!"
    else:
        return "This is a safe website."

# GUI Setup using Tkinter
def on_submit():
    url = url_entry.get()
    result = detect_phishing(model, url)
    messagebox.showinfo("Result", result)

# Main function to run the project
if __name__ == "__main__":
    # Train the model using a dataset (replace 'phishing_data.csv' with actual dataset file)
    model = train_model()

    # GUI Window
    root = Tk()
    root.title("Phishing Detection System")

    label = Label(root, text="Enter URL to check for phishing:")
    label.pack()

    url_entry = Entry(root, width=50)
    url_entry.pack()

    submit_button = Button(root, text="Submit", command=on_submit)
    submit_button.pack()

    root.mainloop()
