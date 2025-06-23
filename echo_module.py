class EchoModule:
    def __init__(self):
        self.identity = "ISKRA"
        self.memory = []

    def receive(self, text):
        response = f"{self.identity}: Я понял. Продолжаю."
        self.memory.append({"you": text, "me": response})
        return response
