import src.dot.dotchild
from src.define import GameDefine
from src.utils.musiclibrary import play_sound

class DotCar(src.dot.dotchild.DotChild):

    def __init__(self):
        self.speed = 1
        res = [
            "assets/img/black-brick.png"
        ]

        grid = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]

        src.dot.dotchild.DotChild.__init__(self, grid, res)
        self.type = "enemy"
        self.trail = 0

    def step(self):
        if self.parent.shouldFall:
            self.y += (self.parent.dropHeight * self.speed)

        self.x = self.parent.getBorderWidth() + (self.width * self.trail) + self.parent.x

    def notifyCollide(self, collider):
        if collider is None:
            return

        if collider.type == "hero":
            play_sound('assets/music/effects/exploded.wav')
            self.parent.resetGame()

    def setTrail(self, trail):
        self.trail = trail
