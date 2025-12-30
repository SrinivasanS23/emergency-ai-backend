import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from nlp_engine.preprocessing import clean_text


def load_category_data(csv_path: str):
    df = pd.read_csv(csv_path)
    df = df[df["emergency"] == 1]

    df["clean_text"] = df["text"].apply(clean_text)

    X = df["clean_text"]
    y = df["category"]

    return X, y


def train_category_model(csv_path: str):
    X, y = load_category_data(csv_path)

    vectorizer = TfidfVectorizer(stop_words="english")
    X_vec = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.25, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Category Model Evaluation:")
    print(classification_report(y_test, y_pred))

    return model, vectorizer


def predict_category(text: str, model, vectorizer):
    clean = clean_text(text)
    vec = vectorizer.transform([clean])
    category = model.predict(vec)[0]
    confidence = model.predict_proba(vec).max()

    return category, confidence
