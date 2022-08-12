from manim import *
class PlayingCard:
    def __init__(self, number: int, suit: int):
        self.number = number
        self.suit = suit
        if suit == 1:
            suitName = "$\spadesuit$"
        elif suit == 2:
            suitName = "$\clubsuit$"
        elif suit == 3:
            suitName = "$\diamondsuit$"
        elif suit == 4:
            suitName = "$\diamondsuit$"

        if number == 11:
            royaltyIcon = "J"
        elif number == 12:
            royaltyIcon = "Q"
        elif number == 13:
            royaltyIcon = "K"
        elif number == 14:
            royaltyIcon = "A"
        else:
            royaltyIcon = ""
        self.icon = f"{royaltyIcon or number}{suitName}"

    def getColor(self):
        if self.suit < 2:
            return BLACK
        else:
            return RED

    def generateCard(self):
        card = (
            RoundedRectangle(corner_radius=0.25, height=4, width=3)
            .set_fill(color=WHITE, opacity=1)
            .set_stroke(color=self.getColor(), width=2)
        )
        textUL = Tex(f"{self.icon}", color=self.getColor())
        textCENTER = Tex(f"{self.number}", color=self.getColor()).scale(3)
        textDR = textUL.copy()
        textUL.shift(UP * 1.55, LEFT * 0.9)
        textDR.rotate(PI)
        textDR.shift(DOWN * 1.55, RIGHT * 0.9)
        return VGroup(card, textUL, textDR, textCENTER)
