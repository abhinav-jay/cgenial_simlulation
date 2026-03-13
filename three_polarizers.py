import math
import pygame, sys
from pygame.locals import *
from pygame_widgets.slider import Slider
import pygame_widgets

theta1 = 0
theta2 = math.radians(44)
theta3 = math.radians(abs(theta2 - 90))
t = 30

def calculate_intensity(theta2, theta3):
    i1 = 1 / 2
    i2 = i1 * (math.cos(theta2))**2
    i3 = i2 * (math.cos(theta3))**2
    return [i2, i3]

# color calculation
def get_color(i):
    return [math.floor(255 * i), math.floor(255 * i), math.floor(255 * i)]
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('trois polariseurs')
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

fontObj = pygame.font.Font(None, 30)
slider = Slider(screen, 100, 600, 900, 40, min=0, max=90, step=1, color=(100,100,100))
value = theta2


while running:
    dt = clock.tick(20) / 1000  # delta time, limited to 200 FPS

    theta3 = math.radians(abs(math.degrees(theta2) - 90))

    i2 = calculate_intensity(theta2, theta3)[0]
    i3 = calculate_intensity(theta2, theta3)[1]

    # color calculation
    color0 = get_color(1)
    color1 = get_color(1/2)
    color2 = get_color(i2)
    color3 = get_color(i3)

    text1 = fontObj.render(f"θ = {math.degrees(theta2) % 91}°", True, (0, 0, 255))
    text2 = fontObj.render(f"I2 = {i2 * 100}%", True, (0, 0, 255))
    text3 = fontObj.render(f"I3 = {i3 * 100}%", True, (0, 0, 255))
    text4 = fontObj.render(f"0°", True, (0, 0, 255))
    text5 = fontObj.render(f"θ = {math.degrees(theta2) % 91}°", True, (0, 0, 255))
    text6 = fontObj.render(f"90°", True, (0, 0, 255))

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    theta2 = math.radians(slider.getValue())

    value = slider.getValue()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_h]:
        value -= 1
        value = value % 91
    if keys[pygame.K_l]:
        value += 1
        value = value % 91

    slider.setValue(value)

    # write text
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 30))
    screen.blit(text3, (10, 50))
    screen.blit(text4, (460, 410))
    screen.blit(text5, (940, 410))
    screen.blit(text6, (1420, 410))
    screen.blit(text5, (1050, 610))

    # draw color rectangles
    pygame.draw.rect(screen, color0, [0, 100, 480, 300])
    pygame.draw.rect(screen, color1, [480, 100, 480, 300])
    pygame.draw.rect(screen, color2, [960, 100, 480, 300])
    pygame.draw.rect(screen, color3, [1440, 100, 480, 300])

    # draw arrow
    if t in range(480):
        pygame.draw.polygon(screen, (200, 200, 100), (((t-30), 220), ((t-30), 270), ((110+t), 270), ((110+t), 320), ((210+t), 255), ((110+t), 170), ((110+t), 220)))
    if t in range(480,960):
        pygame.draw.polygon(screen, (100, 100, 50), (((t-30), 220), ((t-30), 270), ((110+t), 270), ((110+t), 320), ((210+t), 255), ((110+t), 170), ((110+t), 220)))
    if t in range(960,1440):
        pygame.draw.polygon(screen, (math.floor(200*i2), math.floor(i2*200), math.floor(i2*100)), (((t-30), 220), ((t-30), 270), ((110+t), 270), ((110+t), 320), ((210+t), 255), ((110+t), 170), ((110+t), 220)))
    if t > 1440:
        pygame.draw.polygon(screen, (math.floor(200*i3), math.floor(i3*200), math.floor(i3*100)), (((t-30), 220), ((t-30), 270), ((110+t), 270), ((110+t), 320), ((210+t), 255), ((110+t), 170), ((110+t), 220)))


    # update
    pygame_widgets.update(events)
    pygame.display.update()
    t += 30

    if t > 2000:
        t = 30

pygame.quit()
