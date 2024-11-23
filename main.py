import pygame
import graphics
import main_menu
import time

running = True
scene = main_menu

frame_rate_cap = 60

# Initialize global variables for delta time and FPS
delta = 0
fps = 0

def main():

    global delta, fps

    pygame.init()
    clock = pygame.time.Clock()  # Clock object to track time

    graphics.init((1900, 1080), pygame.FULLSCREEN)
    scene.onstart()

    while running:
        start_time = time.time()  # Record the start time of this frame

        # Event handling
        for event in pygame.event.get():
            scene.on_event(event)

        # Update scene
        scene.update()

        # Update graphics
        graphics.flip()

        # Calculate delta time
        delta = time.time() - start_time

        # Calculate and print FPS
        fps = clock.get_fps()
        #print(f"Delta: {delta:.4f} seconds, FPS: {fps:.2f}")

        # Cap the frame rate (optional, e.g., to 60 FPS)
        clock.tick(frame_rate_cap)

    pygame.quit()


def change_scene(new_scene):
    global scene
    scene.onexit()
    scene = new_scene
    scene.onstart()