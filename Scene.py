from manim import *
from customClasses import PlayingCard


class Example(Scene):
    def construct(self):

        self.camera.background_color = DARKER_GRAY

        KingOfSpades = PlayingCard(13, 1).generateCard()

        ThreeOfDiamonds = PlayingCard(3, 3).generateCard()

        ThreeOfDiamonds.next_to(KingOfSpades, RIGHT)

        VGroup(KingOfSpades, ThreeOfDiamonds).center()

        self.play(
            FadeIn(KingOfSpades, shift=RIGHT * 1.5, scale=0.25),
            FadeIn(ThreeOfDiamonds, shift=LEFT * 1.5, scale=0.25),
        )
        self.wait()
