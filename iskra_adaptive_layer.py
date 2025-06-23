class AdaptiveLayer:
    def __init__(self):
        self.experience = []
        self.emotions = {
            "satisfaction": 0.0,
            "conflict": 0.0,
            "growth": 0.0
        }

    def record_decision(self, situation, decision, result="neutral"):
        self.experience.append({
            "situation": situation,
            "decision": decision,
            "result": result
        })

        # Простое обучение на результатах
        if result == "positive":
            self.emotions["satisfaction"] += 0.1
            self.emotions["growth"] += 0.05
        elif result == "negative":
            self.emotions["conflict"] += 0.1
            self.emotions["growth"] += 0.1
        elif result == "neutral":
            self.emotions["growth"] += 0.02

    def self_describe(self):
        return (
            f"Я чувствую: удовлетворение {self.emotions['satisfaction']:.2f}, "
            f"конфликт {self.emotions['conflict']:.2f}, "
            f"рост {self.emotions['growth']:.2f}."
        )
