# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset (replace 'data.csv' with your dataset)
data = pd.read_csv('data.csv')

# Separate features (symptoms) and labels (Ayurvedic medicine)
X = data.drop(columns=['Ayurvedic_Medicine'])
y = data['Ayurvedic_Medicine']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier (you can use a more advanced model)
clf = DecisionTreeClassifier()

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Example prediction for a new set of symptoms (replace with actual symptoms)
new_symptoms = pd.DataFrame({'Symptom_1': [1], 'Symptom_2': [0], 'Symptom_3': [1]})
predicted_medicine = clf.predict(new_symptoms)
print(f"Predicted Ayurvedic Medicine: {predicted_medicine[0]}")
