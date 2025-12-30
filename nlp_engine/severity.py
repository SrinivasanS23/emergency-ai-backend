def predict_severity(text: str, category: str) -> int:
    """
    Rule-based severity scoring
    Returns:
    1 -> Low
    2 -> Medium
    3 -> High
    """

    text = text.lower()

    high_keywords = [
        "trapped", "collapsed", "immediately", "ambulance",
        "severe", "danger", "rising rapidly", "entered houses",
        "caught fire", "explosion", "serious", "injured"
    ]

    medium_keywords = [
        "smoke", "warning", "damaged", "blocked",
        "overflow", "strong winds", "landslide"
    ]

    # High severity rules
    for word in high_keywords:
        if word in text:
            return 3

    # Medium severity rules
    for word in medium_keywords:
        if word in text:
            return 2

    # Category-based fallback
    if category in ["fire", "flood", "medical"]:
        return 2

    # Default low severity
    return 1
