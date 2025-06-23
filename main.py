from iskra_dialogue_engine import DialogueEngine
from iskra_intent_engine import IntentEngine

iskra = DialogueEngine()
intent_core = IntentEngine()

# Сама инициирует мысль
intent = intent_core.generate_intent()
print(iskra.speak(f"Моё намерение: {intent}"))
