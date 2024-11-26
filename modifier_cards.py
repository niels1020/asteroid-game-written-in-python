import pygame
import main
import keybinds
import random
import graphics
import utils
import settings
import game

card_rect: pygame.Rect = pygame.Rect(0,0,100,100)
space_between_cards = 10
card_coloms: int
cards_for_choosing: dict
card_modifiers = ["kills_for_card","max_asteroids","asteroid_spawn_rate","kills_for_card","bullet_speed","player_speed","astroid_speed"]

def onstart():
    card_coloms = graphics.get_width()/card_rect.width+(space_between_cards*2)
    cards_for_choosing = dict()
    for i in range(settings.cards_to_chose):
        modifier = random.choice(card_modifiers)
        value = 0.0
        if modifier.endswith("_speed"):
            value = random.choice([-0.1,0.1])

        cards_for_choosing[modifier] = value



def update():
    global cards_for_choosing
    draw_card(0,cards_for_choosing.keys()[0],cards_for_choosing.items()[0])

def onexit():
    pass

def on_event(event: pygame.event.Event):
    if event.type == pygame.QUIT:
        game.paused = False
        game.choosing_cards = False

def draw_card(iteration: int,modifier: str, value: float):
    rect = card_rect.copy()
    rect.left = (iteration*(rect.width))+space_between_cards
    graphics.draw_rect(settings.primary_color,rect)