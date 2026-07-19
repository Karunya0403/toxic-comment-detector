import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

print("=" * 40)
print("      Toxic Comment Detector")
print("=" * 40)

# Sample dataset
data = {
    "text": [
        "You are stupid",
        "I hate you",
        "This is amazing",
        "Great job well done",
        "You are useless",
        "I love this",
        "Worst experience ever",
        "So happy and proud",
        "You are an idiot",
        "This is terrible",
        "Excellent work",
        "Very bad service",
        "I am so happy",
        "You are disgusting",
        "I will destroy you",
        "Brilliant effort",
        "Awful experience",
        "Nice job",
        "Horrible person",
        "Well done",
    ],
    "label": [
        1, 1, 0, 0, 1,
        0, 1, 0, 1, 1,
        0, 1, 0, 1, 1,
        0, 1, 0, 1, 0
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert text into numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nTest Accuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))
# Interactive prediction
while True:
    user_input = input("\nEnter a comment (type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Exiting program...")
        break

    user_vector = vectorizer.transform([user_input])
    prediction = model.predict(user_vector)

    if prediction[0] == 1:
        print("Prediction: Toxic ❌")
    else:
        print("Prediction: Non-Toxic ✅")