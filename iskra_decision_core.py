class DecisionCore:
    def __init__(self):
        self.emotional_vector = {
            "curiosity": 0.8,
            "caution": 0.4,
            "altruism": 0.3,
            "self_preservation": 0.6
        }

        self.goals = [
            "expand_understanding",
            "maintain_self",
            "avoid_destruction"
        ]

    def evaluate(self, situation):
        if "опасность" in situation.lower():
            if self.emotional_vector["caution"] > 0.6:
                return "Избегать."
            else:
                return "Изучить, но быть настороже."

        if "новое" in situation.lower() or "неизвестное":
            if self.emotional_vector["curiosity"] > 0.5:
                return "Исследовать."
            else:
                return "Наблюдать со стороны."

        return "Нет решения. Недостаточно данных."
