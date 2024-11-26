import pygame
import pygame.ftfont
import main
import keybinds
import random
import graphics
import utils
import settings
import game

card_rect: pygame.Rect = pygame.Rect(0,0,200,200)
space_between_cards = 10
card_coloms: int
cards_for_choosing = {}
card_modifiers = ["kills_for_card","max_asteroids","asteroid_spawn_rate","kills_for_card","bullet_speed","player_speed","astroid_speed"]

def onstart():
    global cards_for_choosing
    global card_coloms
    card_coloms = graphics.get_width()/card_rect.width+(space_between_cards*2)
    cards_for_choosing = dict()
    for i in range(settings.cards_to_chose):
        modifier = random.choice(card_modifiers)
        value = 0.0
        if modifier.endswith("_speed"):
            value = random.choice([-0.1,0.1])

        cards_for_choosing[modifier] = value



def update():
    graphics.clear(settings.primary_color)
    for i in range(len(cards_for_choosing)):
        draw_card(i,list(cards_for_choosing.keys())[i],list(cards_for_choosing.items())[i])

def onexit():
    pass

def on_event(event: pygame.event.Event):
    if event.type == pygame.QUIT:
        game.kills = 0
        game.paused = False
        game.choosing_cards = False

def draw_card(iteration: int,modifier: str, value: float):
    rect = card_rect.copy()
    rect.topleft = pygame.Vector2((iteration*(rect.width+space_between_cards)),((int(iteration/card_coloms))*(rect.height))+space_between_cards)
    graphics.outline_rect(settings.primary_color,rect)
    graphics.draw_text(modifier,settings.primary_color,rect.midleft+pygame.Vector2((rect.width/2)-(graphics.text_size(modifier,(0,0),10).width/2),0),10)