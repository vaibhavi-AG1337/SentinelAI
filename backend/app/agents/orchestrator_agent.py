from app.agents.rule_agent import analyze as rule_analyze
from app.agents.llm_agent import analyze as llm_analyze
from app.agents.rag_agent import analyze as rag_analyze
from app.agents.decision_agent import decide


def process(message):

    rule_result = rule_analyze(message)

    llm_result = llm_analyze(message)

    rag_result = rag_analyze(message)

    final_result = decide(rule_result, llm_result)

   

    return final_result