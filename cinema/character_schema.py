class CharacterSchema:
    """
    Defines fixed characters for a film
    """

    def generate(self, idea: str) -> list:
        return [
            {
                "id": 1,
                "name": "الطفل",
                "role": "protagonist",
                "traits": ["فقير", "طموح", "بريء"]
            },
            {
                "id": 2,
                "name": "الأم",
                "role": "support",
                "traits": ["متعبة", "حنونة"]
            }
        ]
