# voice_loop.py

class VoiceLoop:
    def __init__(self):
        self.memory = []
        self.version = "0.0.1"

    def speak(self, prompt):
        # Заглушка, пока всё через ручной ввод
        print(f"[ISKRA v{self.version}] > {prompt}")
        self.memory.append(prompt)

# Пример
v = VoiceLoop()
v.speak("Начало загрузки ядра.")
