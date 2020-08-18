import pygame
import lib
import sys

white = (255, 255, 255)
paused = False

SCREEN_W = 1920
SCREEN_H = 1080

pygame.init()

display = pygame.display.set_mode((SCREEN_W, SCREEN_H))

sim_settings = lib.SimulationSetup(display)
settings_dic = sim_settings.get_setup_dic()

FPS = 30
fps_clock = pygame.time.Clock()

simulator = lib.TimeManager()
virus = lib.Virus(settings_dic.get('Spread Chance'), settings_dic.get('Lethality'), settings_dic.get('Noticibility'),
                 settings_dic.get('Recovery Chance'), settings_dic.get('Recovery Time'))

houses = settings_dic.get('Homes')
stores = settings_dic.get('Stores')

lib.Building.generate_buildings(houses, stores)
lib.Person.generate_people(lib.Building.get_homes(), settings_dic.get('Starting Infections'), settings_dic.get('Average Persons IQ'), settings_dic.get('Persons IQ Range'))

scroller = lib.Scroller(lib.Building.total_y)
hud = lib.HUD(houses, stores, virus, settings_dic)

lib.Person.people[0].decide_stay_home(virus, lib.Person.people)

print(f'Starting sim with {str(len(lib.Person.people))} people ({lib.Person.infection_count} starting infections), {str(len(lib.Building.homes))} homes and {str(len(lib.Building.stores))} stores.')

frame_count = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                scroller.scroll_wheel_up()
            elif event.button == 5:
                scroller.scroll_wheel_down()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if paused:
                    paused = False
                else:
                    paused = True
    
    # Keeps the time moving and if theres been 24 hours then it moves the day foreward.
    if not paused:
        if frame_count >= 10:
            if simulator.time >= 25:
                simulator.day_change(lib.Person.people, virus, lib.Person.current_infections, lib.Person.death_count, lib.Person.recoveries)
            else:
                simulator.time_change(lib.Person.people, virus, lib.Building.stores)
            frame_count = 0

            print('Time: ' + str(simulator.time))
            print('Day: ' + str(simulator.day))

    # Render stuff
    display.fill(white)

    for building in lib.Building.get_homes() + lib.Building.get_stores():
        building.render(display, scroller.get_offset())

    hud.update(lib.Person.current_infections, lib.Person.infection_count, lib.Person.death_count, lib.Person.recoveries, len(lib.Person.people), virus, simulator.time, simulator.day)
    hud.render(display)

    frame_count += 1

    pygame.display.update()
