def decide(rule_result, llm_result):

    return {
        **rule_result,
        "llm_analysis": llm_result
    }
