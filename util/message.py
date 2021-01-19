class Message:
    def __init__(self, message):
        if len(message) == 0:
            self.message = ""
        else:
            self.message = message
        print(f"Hi!: {self.message}")
