class DialoguePlanner:
    """
    Determines who speaks in each scene (NO dialogue text)
    """

    def plan(self, scenes: list, characters: list) -> list:
        dialogue_map = []
        for scene in scenes:
            dialogue_map.append({
                "scene_id": scene["scene_id"],
                "speakers": [c["name"] for c in characters]
            })
        return dialogue_map
