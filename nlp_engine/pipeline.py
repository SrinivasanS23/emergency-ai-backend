from nlp_engine.classifier import train_model, predict_message
from nlp_engine.category_classifier import train_category_model, predict_category
from nlp_engine.severity import predict_severity


class EmergencyAIPipeline:
    def __init__(self, csv_path: str):
        # Train models once
        self.emergency_model, self.emergency_vectorizer = train_model(csv_path)
        self.category_model, self.category_vectorizer = train_category_model(csv_path)

    def analyze_message(self, text: str) -> dict:
        # Stage 1: Emergency detection
        emergency, emergency_conf = predict_message(
            text, self.emergency_model, self.emergency_vectorizer
        )

        if emergency == 0:
            return {
                "text": text,
                "is_emergency": False,
                "confidence": round(emergency_conf, 2),
            }

        # Stage 2: Category prediction
        category, category_conf = predict_category(
            text, self.category_model, self.category_vectorizer
        )

        # Stage 3: Severity scoring
        severity = predict_severity(text, category)

        return {
            "text": text,
            "is_emergency": True,
            "category": category,
            "severity": severity,
            "confidence": round(max(emergency_conf, category_conf), 2),
        }
