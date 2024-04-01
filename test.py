from view.dice_view import DiceView
from model import DICE
import pygame


pygame.init()
pygame.font.init()


dice = DiceView(5, DICE.D20)

dice.draw((pygame.Surface((100, 100)), (0, 0)))