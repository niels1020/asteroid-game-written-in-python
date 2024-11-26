import pygame
import main
import main_menu
import graphics
import settings
import utils
import keybinds
import player
import modifier_cards
import asteroids
import bullet

asteroid: list[asteroids.Asteroid] = list()
bullets: list[bullet.bullet] = list()
kills: int = 0
paused = False
choosing_cards = False

astroid_spawn_timer:float = 0.0
max_asteroids = 25
time_between_asteroid_spawns = 0.5

def onstart():
    global asteroid
    asteroid.append(asteroids.generate_asteroid())

def update():
    global choosing_cards
    global paused
    if not paused:

        if kills >= settings.kills_for_card:
            paused = True
            choosing_cards = True
            modifier_cards.onstart()

        global astroid_spawn_timer
        graphics.clear(settings.secondary_color)

        player.draw()

        player.angle = utils.get_angle_between(utils.get_screen_midle(),pygame.mouse.get_pos())
        
        if pygame.mouse.get_pos() - utils.get_screen_midle() != pygame.Vector2(0,0):
            player.position += (pygame.mouse.get_pos() - utils.get_screen_midle()).normalize() * main.delta * player.speed * (player.position.distance_to(utils.get_screen_midle())/10)
        
        bullet.bullet_stuf()

        to_remove = list()
        for i in asteroid:
            if i.position.distance_to(player.position) > settings.despawn_distance:
                to_remove.append(i)
            else:
                i.update()
                asteroids.draw_asteroid(i)
        
        for i in to_remove:
            asteroid.remove(i)

        if asteroid.__len__() < max_asteroids and astroid_spawn_timer < 0.0:
            asteroid.append(asteroids.generate_asteroid())
            astroid_spawn_timer = time_between_asteroid_spawns

        if settings.debug_enabled:
            utils.debug_draw()
        
        astroid_spawn_timer -= main.delta
    elif choosing_cards:
        modifier_cards.update()

def onexit():
    pass

def on_event(event: pygame.event.Event):
    global paused
    global choosing_cards
    if not paused:
        if event.type == pygame.QUIT:
            main.change_scene(main_menu)
        elif event.type == pygame.KEYDOWN:
            if event.key == keybinds.exit:
                main.change_scene(main_menu)
            elif event.key == keybinds.shoot:
                bullet.shoot()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == keybinds.shoot:
                bullet.shoot()
    elif choosing_cards:
        modifier_cards.on_event(event)