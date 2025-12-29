from memory_engine.memory_engine import MemoryEngine
from decision_engine.decision_engine_v2 import DecisionEngineV2
from architect_engine.architect_engine import ArchitectEngine
from domain_rules.film_rules import FilmRules
from planners.film_planner import FilmPlanner
from cinema.character_schema import CharacterSchema
from cinema.scene_generator import SceneGenerator
from cinema.dialogue_planner import DialoguePlanner

class HikmaCore:
    def __init__(self):
        self.memory = MemoryEngine()
        self.decision_engine = DecisionEngineV2(self.memory)
        self.architect = ArchitectEngine()

        self.film_rules = FilmRules()
        self.film_planner = FilmPlanner()
        self.character_schema = CharacterSchema()
        self.scene_generator = SceneGenerator()
        self.dialogue_planner = DialoguePlanner()

    def process(self, user_input: str):
        decision = self.decision_engine.decide(user_input)

        if decision.get("domain") == "film" and decision.get("intent") == "analysis":
            rules = self.film_rules.validate(user_input)
            film_plan = self.film_planner.plan(user_input)
            characters = self.character_schema.generate(user_input)
            scenes = self.scene_generator.generate(film_plan)
            dialogue_map = self.dialogue_planner.plan(scenes, characters)

            return {
                "decision": decision,
                "rules": rules,
                "film_plan": film_plan,
                "characters": characters,
                "scenes": scenes,
                "dialogue_plan": dialogue_map
            }

        plan = self.architect.build_plan(decision)
        return {
            "decision": decision,
            "plan": plan
        }
