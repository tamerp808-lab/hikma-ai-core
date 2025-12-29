class DecisionEngineV1:
    """
    HIKMA AI Core
    Decision Engine v1
    Phase 1 – Core Intelligence
    """

    def decide(self, user_input: str) -> dict:
        text = user_input.lower().strip()

        if any(w in text for w in ["تطبيق", "app"]):
            domain = "app"
        elif any(w in text for w in ["فيلم", "movie"]):
            domain = "film"
        elif any(w in text for w in ["لعبة", "game"]):
            domain = "game"
        else:
            domain = "unknown"

        return {
            "decision": "BLOCK_GENERATION",
            "domain": domain,
            "allowed_to_generate": False,
            "reason": "AI Core not completed yet"
        }
