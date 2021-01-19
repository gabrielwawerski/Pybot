from time import time


class Chatbot:
    def __init__(self, username, password, thread_id):
        self.username = username
        self.password = password
        self.thread_id = thread_id

        self._running = True
        self._version = "v0.1"
        self._modules = list(range(10))
        self._message_log = list(range(100))
        self.refresh_rate = 0.1
        self._startup_time = time()
        print(time())

    def get_regexes(self):
        pass

    def run(self):
        while self._running:
            try:
                pass
            finally:
                pass


