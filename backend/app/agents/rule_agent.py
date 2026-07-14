from app.services.phishing_detector import analyze_message


def analyze(message):
    return analyze_message(message)