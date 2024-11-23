import pygame
import pygame.math as math
import settings

pygame.font.init()

surface: pygame.Surface

def clear(color: pygame.color):
    surface.fill(color)

def get_height():
    return surface.get_height()

def get_width():
    return surface.get_width()

def init(size: math.Vector2,flags: int = 0,depth: int = 0,display: int = 0,vsync: int = 0):
    global surface
    surface = pygame.display.set_mode(size,flags,depth,display,vsync)
    pygame.display.set_caption(settings.game_title)
    pygame.display.set_icon(pygame.image.load(settings.game_icon_path))
    pygame.mouse.set_cursor((5,5),pygame.image.load(settings.game_mouse_path))

def draw_line(color: pygame.color,start_pos: math.Vector2,end_pos: math.Vector2,width: int = 1):
    pygame.draw.line(surface,color,start_pos,end_pos,width)

def draw_rect(color: pygame.color,rect: pygame.rect.Rect):
    pygame.draw.rect(surface,color,rect)

def draw_polygon(color: pygame.color,points: list[math.Vector2] ,width: int = 1):
    pygame.draw.polygon(surface,color,points,width)

def outline_rect(color: pygame.color,rect: pygame.rect.Rect,width: int = 1):
    pygame.draw.lines(surface,color,True,[rect.topleft,rect.bottomleft,rect.bottomright,rect.topright],width)

def outline_polygon(color: pygame.Color, points: list[pygame.Vector2], width: int = 1):
    pygame.draw.lines(surface, color, True, points,width)

def flip():
    pygame.display.flip()

def draw_text(text: str,color: pygame.color.Color,pos: pygame.math.Vector2,size: int = 24):
    font = pygame.font.Font(settings.font_path,size)
    text = font.render(text,False,color)
    surface.blit(text,pos)

def text_size(text: str,pos: pygame.math.Vector2,size: int = 24) -> pygame.Rect:
    font = pygame.font.Font(settings.font_path,size)
    size = font.size(text)
    rect = pygame.Rect(pos[0],pos[1],size[0],size[1])
    return rect