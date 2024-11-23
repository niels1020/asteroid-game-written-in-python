import pygame
import utils
import player
import random
import math
import graphics
import settings
import main

min_asteroid_spawn_distance = 10
max_asteroid_spawn_distance = 100


min_asteroid_vertices = 5
max_asteroid_vertices = 8

class Asteroid:
    def __init__(self):
        self.position = pygame.Vector2(0, 0)
        self.direction = pygame.Vector2(0, 0)
        self.num_vertices = 0
        self.size = 0
        self.vertices = []
        self.speed = 10
    
    def update(self):
        self.position += self.direction * main.delta * self.speed

def generate_asteroid():
    screen_width, screen_height = graphics.get_width(), graphics.get_height()

    asteroid = Asteroid()
    
    
    side = random.choice(["top", "bottom", "left", "right"])
    
    if side == "top":
        y = 0
        x = random.randint(0,screen_width)
    elif side == "bottom":
        x = random.randint(0,screen_width)
        y = screen_height
    elif side == "left":
        x = 0
        y = random.randint(0,screen_height)
    else:  # "right"
        x = screen_width
        y = random.randint(0,screen_height)
    asteroid.position = pygame.Vector2(x, y)-utils.get_screen_midle()
    
    asteroid.direction = (player.position - asteroid.position).normalize()

    asteroid.num_vertices = random.randint(min_asteroid_vertices, max_asteroid_vertices)

    angle_step = (2 * math.pi) / asteroid.num_vertices
    for i in range(asteroid.num_vertices):
        angle = i * angle_step
        radius = 30 + random.random() * 20
        vertice = pygame.Vector2(radius * math.cos(angle), radius * math.sin(angle))
        asteroid.vertices.append(vertice)
        if vertice.distance_to((0,0)) > asteroid.size:
            asteroid.size = vertice.distance_to((0,0))


    
    return asteroid

def draw_asteroid(asteroid: Asteroid):
    screen_mid = utils.get_screen_midle()
    
    processed_model = [
        pygame.Vector2(point) + asteroid.position - player.position + screen_mid
        for point in asteroid.vertices
    ]
    
    graphics.outline_polygon(settings.primary_color, processed_model)

    if settings.debug_enabled:
        graphics.draw_line(settings.debug_color, asteroid.position - player.position + utils.get_screen_midle(),(asteroid.position + asteroid.direction * asteroid.speed) - player.position + utils.get_screen_midle())
