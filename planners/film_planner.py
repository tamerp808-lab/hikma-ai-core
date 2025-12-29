class FilmPlanner:
    """
    Converts idea into a structured film plan
    """

    def plan(self, idea: str) -> dict:
        return {
            "idea": idea,
            "scenes": [
                {"id": 1, "type": "intro", "duration": 60},
                {"id": 2, "type": "conflict", "duration": 180},
                {"id": 3, "type": "resolution", "duration": 120}
            ],
            "total_duration": 360
        }
