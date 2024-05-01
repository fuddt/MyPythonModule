class DvdPlayer:
    def on(self):
        print("DVD Player turning on.")

    def play(self, movie):
        print(f"DVD Player playing {movie}.")

class Projector:
    def on(self):
        print("Projector turning on.")

    def setInput(self, input):
        print(f"Projector input set to {input}.")

class Lights:
    def dim(self, level):
        print(f"Lights dimming to {level}%.")

class HomeTheaterFacade:
    """ホームシアターシステムのファサードクラス"""
    
    def __init__(self):
        self.dvd = DvdPlayer()
        self.projector = Projector()
        self.lights = Lights()

    def watch_movie(self, movie):
        self.lights.dim(10)
        self.projector.on()
        self.projector.setInput("DVD")
        self.dvd.on()
        self.dvd.play(movie)

# クライアントコード
home_theater = HomeTheaterFacade()
home_theater.watch_movie("Inception")
