from memory_engine.memory_engine import MemoryEngine

class DecisionEngineV2:
    """
    Advanced decision engine with intent, priority, and routing
    """

    def __init__(self, memory: MemoryEngine):
        self.memory = memory

    def decide(self, user_input: str) -> dict:
        text = user_input.lower()

        if any(w in text for w in ["حلل", "explain", "analyze"]):
            intent = "analysis"
            priority = 1
        elif any(w in text for w in ["اعمل", "اصنع", "build", "create"]):
            intent = "generation"
            priority = 2
        else:
            intent = "unknown"
            priority = 0

        if any(w in text for w in ["فيلم", "movie"]):
            domain = "film"
        elif any(w in text for w in ["تطبيق", "app"]):
            domain = "app"
        else:
            domain = "unknown"

        decision = {
            "intent": intent,
            "domain": domain,
            "priority": priority,
            "allowed": intent == "analysis",
            "next_engine": "architect_engine" if intent == "generation" else None
        }

        self.memory.remember_decision(decision)
        return decision
