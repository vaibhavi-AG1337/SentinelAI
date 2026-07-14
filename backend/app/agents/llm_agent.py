from app.services.llm_service import analyze_with_llm


def analyze(message):
    return analyze_with_llm(message)