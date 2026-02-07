import math
import pygame, sys
from pygame.locals import *
from pygame_widgets.slider import Slider
import pygame_widgets

theta1 = 0
theta2 = math.radians(int(input("Enter the angle of the second polarizer in degrees: ")))
theta3 = math.radians(abs(theta2 - 90))

def calculate_intensity(theta2, theta3):
    i1 = 1 / 2
    i2 = i1 * (math.cos(theta2))**2
    i3 = i2 * (math.cos(theta3))**2
    return [i2, i3]

# color calculation
def get_color(i):
    return [math.floor(255 * i), math.floor(255 * i), math.floor(255 * i)]
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

fontObj = pygame.font.Font(None, 25)

while running:
    dt = clock.tick(60) / 1000  # delta time, limited to 60 FPS

    # Update theta3 based on theta2 (second polarizer angle)
    theta3 = math.radians(abs(math.degrees(theta2) - 90))

    # Calculate intensity using Malus's Law
    i2 = calculate_intensity(theta2, theta3)[0]
    i3 = calculate_intensity(theta2, theta3)[1]

    # color calculation
    color0 = get_color(1)
    color1 = get_color(1/2)
    color2 = get_color(i2)
    color3 = get_color(i3)

    # Render text for angle and intensity
    text1 = fontObj.render(f"θ = {math.degrees(theta2) % 90}°", True, (0, 0, 255))
    text2 = fontObj.render(f"I2 = {i2 * 100}%", True, (0, 0, 255))
    text3 = fontObj.render(f"I3 = {i3 * 100}%", True, (0, 0, 255))

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_h]:
        theta2 -= math.radians(1)
    if keys[pygame.K_l]:
        theta2 += math.radians(1)

    screen.fill((0,0,0))

    slider = Slider(screen, 100, 600, 800, 40, min=0, max=90, step=0.1)
    theta2 = slider.getValue()
    # write text
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 30))
    screen.blit(text3, (10, 50))

    # draw color rectangles
    pygame.draw.rect(screen, color0, [0, 100, 320, 100])
    pygame.draw.rect(screen, color1, [320, 100, 320, 100])
    pygame.draw.rect(screen, color2, [640, 100, 320, 100])
    pygame.draw.rect(screen, color3, [960, 100, 320, 100])

    # Update the display
    pygame.display.flip()
    pygame_widgets.update(events)
    pygame.display.update()

pygame.quit()
