class ArchitectEngine:
    """
    Converts decisions into execution plans
    """

    def build_plan(self, decision: dict) -> dict:
        if not decision.get("allowed"):
            return {
                "status": "BLOCKED",
                "reason": "Generation not allowed yet"
            }

        return {
            "status": "READY",
            "steps": [
                "analyze_requirements",
                "select_domain_rules",
                "prepare_execution_plan"
            ]
        }
