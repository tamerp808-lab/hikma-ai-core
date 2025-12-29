from memory_engine.memory_engine import MemoryEngine
from decision_engine.decision_engine_v2 import DecisionEngineV2
from architect_engine.architect_engine import ArchitectEngine

class HikmaCore:
    def __init__(self):
        self.memory = MemoryEngine()
        self.decision_engine = DecisionEngineV2(self.memory)
        self.architect = ArchitectEngine()

    def process(self, user_input: str):
        decision = self.decision_engine.decide(user_input)
        plan = self.architect.build_plan(decision)
        return {
            "decision": decision,
            "plan": plan
        }
