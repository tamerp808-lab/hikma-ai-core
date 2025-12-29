class MemoryEngine:
    """
    Stores rules and past decisions (NO raw content)
    """

    def __init__(self):
        self.rules = []
        self.decisions = []

    def add_rule(self, rule: str):
        self.rules.append(rule)

    def remember_decision(self, decision: dict):
        self.decisions.append(decision)

    def get_rules(self):
        return self.rules
