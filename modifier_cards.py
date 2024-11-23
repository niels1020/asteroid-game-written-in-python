import pygame
import main
import keybinds
import random
import graphics
import utils
import settings
import game

cards_for_choosing: dict
card_modifiers = ["kills_for_card","max_asteroids","asteroid_spawn_rate","kills_for_card"]

def onstart():
    cards_for_choosing = dict()
    for i in settings.cards_to_chose:
        pass


def update():
    pass

def onexit():
    pass

def on_event(event: pygame.event.Event):
    if event.type == pygame.QUIT:
        main.running = False