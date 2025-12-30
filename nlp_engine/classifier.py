import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from nlp_engine.preprocessing import clean_text


def load_data(csv_path: str):
    """Load and preprocess dataset for emergency detection"""
    df = pd.read_csv(csv_path)

    df["clean_text"] = df["text"].apply(clean_text)

    X = df["clean_text"]
    y = df["emergency"]

    return X, y


def train_model(csv_path: str):
    """Train emergency vs non-emergency classifier"""

    X, y = load_data(csv_path)

    vectorizer = TfidfVectorizer(stop_words="english")
    X_vec = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Emergency Model Evaluation:")
    print(classification_report(y_test, y_pred))

    return model, vectorizer


def predict_message(text: str, model, vectorizer):
    """Predict if a message is an emergency"""
    clean = clean_text(text)
    vec = vectorizer.transform([clean])
    prediction = model.predict(vec)[0]
    probability = model.predict_proba(vec).max()

    return prediction, probability
