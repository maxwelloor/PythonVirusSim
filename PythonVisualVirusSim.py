import pygame
import lib
import sys

white = (255, 255, 255)

SCREEN_W = 1920
SCREEN_H = 1080

pygame.init()

display = pygame.display.set_mode((SCREEN_W, SCREEN_H))

FPS = 30
fps_clock = pygame.time.Clock()

simulator = lib.TimeManager()
virus = lib.Virus(1, 1, 0)

lib.Building.generate_buildings(50, 100)
lib.Person.generate_people(lib.Building.get_homes(), 2)

print(f'Starting sim with {str(len(lib.Person.people))} people ({lib.Person.infection_count} starting infections), {str(len(lib.Building.homes))} homes and {str(len(lib.Building.stores))} stores.')

frame_count = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Keeps the time moving and if theres been 24 hours then it moves the day foreward.
    if frame_count >= 10:
        if simulator.time >= 25:
            simulator.day_change(lib.Person.people, virus, lib.Person.infection_count, lib.Person.death_count, lib.Person.recoveries)
        else:
            simulator.time_change(lib.Person.people, virus, lib.Building.stores)
        frame_count = 0

        print('Time: ' + str(simulator.time))
        print('Day: ' + str(simulator.day))

    display.fill(white)

    frame_count += 1
    pygame.display.update()
