import pygame
import main
import keybinds
import random
import graphics
import utils
import settings
import game

stars = 1000
star_size = 2
selection_rect_extra_size = 20
updates_per_second = 5
selection_outline_size = 1

play_button_rect = graphics.text_size("play",(0,0),settings.text_size)
quit_button_rect = graphics.text_size("quit",(0,0),settings.text_size)
title_rect = graphics.text_size(settings.game_title,(0,0),settings.title_size)

quit_button_selection_rect: pygame.Rect
play_button_selection_rect: pygame.Rect


def onstart():
    main.frame_rate_cap = updates_per_second

    quit_button_rect.topleft = ((graphics.get_width() / 2) - (quit_button_rect.w / 2),((graphics.get_height() / 4) * 3) - (quit_button_rect.h / 2)),
    title_rect.topleft = ((graphics.get_width() / 2) - (title_rect.w / 2),(graphics.get_height() / 4) - (title_rect.h / 2))
    play_button_rect.topleft = ((graphics.get_width() / 2) - (play_button_rect.w / 2),((graphics.get_height() / 4) * 2) - (play_button_rect.h / 2))
    
    global play_button_selection_rect
    play_button_selection_rect = resize_to_selection_rect(play_button_rect)

    global quit_button_selection_rect
    quit_button_selection_rect = resize_to_selection_rect(quit_button_rect)

def update():
    graphics.clear(settings.secondary_color)
    draw_stars()
    draw_buttons()
    draw_title()
    draw_select_rect()
    if settings.debug_enabled:
        utils.debug_draw()

def onexit():
    main.frame_rate_cap = 60

def on_event(event: pygame.event.Event):
    if event.type == pygame.QUIT:
        main.running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == keybinds.exit:
            main.running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == pygame.BUTTON_LEFT:
            if utils.mouse_in_rect(play_button_selection_rect): 
                main.change_scene(game)

            if utils.mouse_in_rect(quit_button_selection_rect): 
                main.running = False


def draw_stars():
    for i in range(stars):
        draw_star()

def draw_star():
    x = random.randint(0, graphics.get_width())
    y = random.randint(0, graphics.get_height())
    rect = pygame.Rect(x, y, star_size, star_size)
    graphics.draw_rect(settings.primary_color, rect)

def draw_buttons():
    graphics.draw_text("play", settings.primary_color, play_button_rect.topleft,settings.text_size)
    graphics.draw_text("quit", settings.primary_color, quit_button_rect.topleft,settings.text_size)

def draw_title():
    graphics.draw_text(settings.game_title, settings.primary_color, title_rect.topleft,settings.title_size)

def draw_select_rect():

    if utils.mouse_in_rect(play_button_selection_rect): 
        graphics.outline_rect(settings.primary_color, play_button_selection_rect, selection_outline_size)
    
    if utils.mouse_in_rect(quit_button_selection_rect): 
        graphics.outline_rect(settings.primary_color, quit_button_selection_rect, selection_outline_size)


def resize_to_selection_rect(rect: pygame.Rect) -> pygame.Rect:
    resized_rect = rect.copy()
    
    resized_rect.height += selection_rect_extra_size
    resized_rect.width += selection_rect_extra_size
    
    resized_rect.topleft = (resized_rect.topleft[0] - selection_rect_extra_size / 2, resized_rect.topleft[1] - selection_rect_extra_size / 2)    

    return resized_rect