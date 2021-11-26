


class EngineLoop:

    def __init__(self):
        self.counter = 0

    def main_game_loop(self):
        while self.counter <= 20:
            print("Piengine")
            self.counter = self.counter + 1

    def run(self):
        self.main_game_loop()
