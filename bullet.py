import pygame
import pygame.locals
import graphics
import settings
import main
import game
import utils
import player

class bullet:
    def __init__(self, position, direction):
        self.position = pygame.Vector2(position)
        self.direction = pygame.Vector2(direction).normalize()
        self.speed = 1000
        self.length = 10
    
    def draw(self):
        graphics.draw_line(settings.primary_color, self.position - player.position + utils.get_screen_midle(), (self.position - (self.direction * self.length)) - player.position + utils.get_screen_midle(), 1)
    
    def advance(self):
        self.position += self.direction * self.speed * main.delta

def bullet_stuf():
    bullets_to_remove = []
    asteroids_to_remove = []

    for bullet in game.bullets:
        
        if bullet.position.distance_to(player.position) > settings.despawn_distance:
            bullets_to_remove.append(bullet)
        else:
            for asteroid in game.asteroid:
                if bullet.position.distance_to(asteroid.position) <= asteroid.size:
                    game.kills += 1
                    print(game.kills)
                    bullets_to_remove.append(bullet)
                    asteroids_to_remove.append(asteroid)
                    break

        bullet.advance()
        bullet.draw()

    for bullet in bullets_to_remove:
        game.bullets.remove(bullet)
    for asteroid in asteroids_to_remove:
        game.asteroid.remove(asteroid)

def shoot():
    direction = (pygame.mouse.get_pos()-utils.get_screen_midle()).normalize()
    bullet_position = player.position
    new_bullet = bullet(bullet_position, direction)
    game.bullets.append(new_bullet)
