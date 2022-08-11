from manim import *
class PlayingCard():
    def __init__(self, number, suit, icon):
        self.number = number
        self.suit = suit
        self.icon = icon
    
    def getColor(self):
        if self.suit < 2:
            return BLACK
        else: 
            return RED

    def generateCard(self):
        card = RoundedRectangle(corner_radius = 0.25,height = 4, width=3).set_fill(color = WHITE, opacity = 1).set_stroke(color=self.getColor(), width=2)
        textUL = Tex(f"{self.icon}", color=self.getColor())
        textCENTER = Tex(f"{self.number}", color=self.getColor()).scale(3)
        textDR = textUL.copy()
        textUL.shift(UP*1.55, LEFT*0.9)
        textDR.rotate(PI)
        textDR.shift(DOWN*1.55, RIGHT*0.9)
        return VGroup(card, textUL, textDR, textCENTER)


class Example(Scene):
    def construct(self):
        
        self.camera.background_color = DARKER_GRAY
        
        KingOfSpades = PlayingCard(13, 1, "K$\spadesuit$")
        KingOfSpades = KingOfSpades.generateCard()

        ThreeOfDiamonds = PlayingCard(3, 3, "3$\diamondsuit$")
        ThreeOfDiamonds = ThreeOfDiamonds.generateCard()

        ThreeOfDiamonds.next_to(KingOfSpades, RIGHT)

        VGroup(KingOfSpades, ThreeOfDiamonds).center()

        self.play(FadeIn(KingOfSpades, shift=RIGHT*1.5, scale=0.25), FadeIn(ThreeOfDiamonds, shift=LEFT*1.5, scale=0.25))
        self.wait()