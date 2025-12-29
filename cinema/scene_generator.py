class SceneGenerator:
    """
    Expands film plan scenes into cinematic descriptions
    """

    def generate(self, film_plan: dict) -> list:
        scenes = []
        for scene in film_plan["scenes"]:
            scenes.append({
                "scene_id": scene["id"],
                "type": scene["type"],
                "description": f"Cinematic {scene['type']} scene with emotional focus",
                "duration": scene["duration"]
            })
        return scenes
