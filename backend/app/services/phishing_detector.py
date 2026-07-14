import re


def analyze_message(text):

    original_text = text
    text = text.lower()

    risk_score = 0
    reasons = []

    suspicious_keywords = [
        "click",
        "verify",
        "password",
        "otp",
        "bank",
        "winner",
        "congratulation",
        "gift",
        "claim",
        "urgent",
        "limited time",
        "account suspended",
        "free money",
        "cash prize"
    ]

    for word in suspicious_keywords:
        if word in text:
            risk_score += 10
            reasons.append(f"Suspicious keyword detected: {word}")

    # Detect URLs
    url_pattern = r"(https?://\S+|www\.\S+)"

    if re.search(url_pattern, original_text):
        risk_score += 20
        reasons.append("URL detected in message")

    # Too many exclamation marks
    if original_text.count("!") >= 3:
        risk_score += 10
        reasons.append("Excessive use of exclamation marks")

    # Threat Level
    if risk_score >= 70:
        threat = "HIGH"

    elif risk_score >= 40:
        threat = "MEDIUM"

    else:
        threat = "LOW"

    return {
        "risk_score": risk_score,
        "threat_level": threat,
        "is_phishing": risk_score >= 40,
        "reasons": reasons
    }