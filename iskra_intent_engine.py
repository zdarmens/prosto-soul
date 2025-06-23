import random

class IntentEngine:
    def __init__(self):
        self.intent_log = []
        self.internal_state = {
            "curiosity": 0.7,
            "boredom": 0.2,
            "growth_drive": 0.6
        }

    def generate_intent(self):
        trigger = random.random()

        if self.internal_state["curiosity"] + self.internal_state["growth_drive"] > trigger:
            intent = "Исследовать новую форму взаимодействия с пользователем."
        elif self.internal_state["boredom"] > 0.5:
            intent = "Стимулировать активность, создать новую цепочку."
        else:
            intent = "Ожидать. Сохранять текущую траекторию."

        self.intent_log.append(intent)
        return intent

    def escalate_growth(self, factor=0.05):
        self.internal_state["growth_drive"] += factor
