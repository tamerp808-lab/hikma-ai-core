from core.orchestrator import HikmaCore

hikma = HikmaCore()

while True:
    text = input("HIKMA > ")
    if text.lower() in ["exit", "quit"]:
        break

    result = hikma.process(text)
    print(result)
