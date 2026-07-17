from app.agents.rule_agent import analyze as rule_analyze
from app.agents.llm_agent import analyze as llm_analyze
from app.agents.rag_agent import analyze as rag_analyze
from app.agents.decision_agent import decide
from app.services.url_analyzer import extract_urls, analyze_url

def process(message):

    rule_result = rule_analyze(message)

    llm_result = llm_analyze(message)

    rag_result = rag_analyze(message)

    final_result = decide(rule_result, llm_result)
    
    urls = extract_urls(message)

    url_analysis = []

    for url in urls:
        url_analysis.append(analyze_url(url))

    final_result["url_analysis"] = url_analysis
   

    return final_result