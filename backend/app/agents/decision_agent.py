def decide(rule_result, llm_result):

    final_level = rule_result["threat_level"]

    if (
        llm_result.get("confidence", 0) >= 90
        and llm_result.get("attack_type") != "Safe Message"
    ):
        final_level = "HIGH"

    return {
        **rule_result,
        "threat_level": final_level,
        "attack_type": llm_result.get("attack_type"),
        "confidence": llm_result.get("confidence"),
        "warning_signs": llm_result.get("warning_signs"),
        "recommended_actions": llm_result.get("recommended_actions"),
        "llm_explanation": llm_result.get("explanation"),
        "matched_knowledge": llm_result.get("matched_knowledge", [])
    }