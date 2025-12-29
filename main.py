from decision_engine.decision_engine_v1 import DecisionEngineV1

engine = DecisionEngineV1()

while True:
    user_input = input("HIKMA > ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print(engine.decide(user_input))
