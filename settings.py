import pygame

debug_text_pos = (0,0)
debug_enabled = False
game_title = "asteroid clone"
despawn_distance = 1000
cards_to_chose = 3
kills_for_card = 5

#paths
game_icon_path = "assets/icon.png"
font_path = "assets/font.ttf"
game_mouse_path = "assets/cursor.png"

#text sizes
text_size = 26
title_size = 100
debug_text_size = 16

#collors
secondary_color = pygame.Color(0,0,0,225)
primary_color = pygame.Color(225,225,225,225)
debug_color = pygame.Color(255,255,0,255)
