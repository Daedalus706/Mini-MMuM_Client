import pygame
from view.colors import Color


def write_at(surf:pygame.Surface, font:pygame.font.Font, pos:tuple[int,int], text:str, text_color:int=0, background_color:int=Color.GOLD, align='left') -> pygame.Rect:
    """Writes thext with provided font to provided surface. align = 'left' | 'center' | 'right'"""

    text_surf:pygame.Surface = font.render(text, True, text_color, Color.to_tuple(background_color))
    text_surf.set_colorkey(Color.to_tuple(background_color))

    match align:
            case 'left':
                pass
            case 'center':
                pos = (pos[0]-text_surf.get_width()//2, pos[1])
            case 'right':
                pos = (pos[0]-text_surf.get_width(), pos[1])

    surf.blit(text_surf, pos)
    return pygame.Rect(pos[0], pos[1], text_surf.get_width(), text_surf.get_height())