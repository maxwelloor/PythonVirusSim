import pygame

class HUD:

    pygame.font.init()

    screen_w = 1920

    border = 5
    middle_gap = 10
    white = (255, 255, 255)
    black = (0, 0, 0)
    font = pygame.font.SysFont('arial', 16)
    b_font = pygame.font.SysFont('arial', 16, True)

    def __init__(self, num_houses, num_stores, virus):
        self.current_infections = 0
        self.total_infections = 0
        self.total_deaths = 0
        self.total_recoveries = 0
        self.people_alive = 0

        # Top left
        self.simulation_settings_render = HUD.b_font.render('Simulation Settings:', 1, HUD.black)
        self.num_houses_render = HUD.font.render('Number of Houses: ' + str(num_houses), 1, HUD.black)
        self.num_stores_render = HUD.font.render('Number of Stores: ' + str(num_stores), 1, HUD.black)
        self.total_people_render = HUD.font.render('Starting People: ' + str(num_houses * 4), 1, HUD.black)

        # Middle
        self.live_stats_render = HUD.b_font.render('Live Simulation Stats:', 1, HUD.black)
        self.current_infections_render = HUD.font.render('Current Infections: ' + str(self.current_infections), 1, HUD.black)
        self.total_infections_render = HUD.font.render('Total Infections: ' + str(self.total_infections), 1, HUD.black)
        self.total_deaths_render = HUD.font.render('Total Deaths: ' + str(self.total_deaths), 1, HUD.black)
        self.total_recoveries_render = HUD.font.render('Total Recoveries: ' + str(self.total_recoveries), 1, HUD.black)
        self.people_alive_render = HUD.font.render('People Alive: ' + str(self.people_alive), 1, HUD.black)

    def update(self, ci, ti, td, tr, pa, virus):
        self.current_infections = ci
        self.current_infections_render = HUD.font.render('Current Infections: ' + str(self.current_infections), 1, HUD.black)

        self.total_infections = ti
        self.total_infections_render = HUD.font.render('Total Infections: ' + str(self.total_infections), 1, HUD.black)

        self.total_deaths = td
        self.total_deaths_render = HUD.font.render('Total Deaths: ' + str(self.total_deaths), 1, HUD.black)

        self.total_recoveries = tr
        self.total_recoveries_render = HUD.font.render('Total Recoveries: ' + str(self.total_recoveries), 1, HUD.black)

        self.people_alive = pa
        self.people_alive_render = HUD.font.render('People Alive: ' + str(self.people_alive), 1, HUD.black)

        if virus.noticed:
            self.virus_discovered_render = HUD.font.render('Virus Noticed: Yes', 1, HUD.black)
        else:
            self.virus_discovered_render = HUD.font.render('Virus Noticed: No', 1, HUD.black)

    def render(self, display):
        pygame.draw.rect(display, HUD.white, (0, 0, HUD.screen_w, 100))

        # left side of top hud will have the current simulation settings
        display.blit(self.simulation_settings_render, (HUD.border, HUD.border))
        display.blit(self.num_houses_render, (HUD.border, HUD.border + 17))
        display.blit(self.num_stores_render, (HUD.border, HUD.border + 17 * 2))
        display.blit(self.total_people_render, (HUD.border, HUD.border + 17 * 3))

        # middle top of hud  will have the current stats of the simulation
        display.blit(self.live_stats_render, (HUD.screen_w / 2 - self.live_stats_render.get_width() / 2, HUD.border))
        display.blit(self.current_infections_render, (HUD.screen_w / 2 - self.current_infections_render.get_width() - HUD.middle_gap, HUD.border + 17))
        display.blit(self.total_infections_render, (HUD.screen_w / 2 + HUD.middle_gap, HUD.border + 17))
        display.blit(self.total_deaths_render, (HUD.screen_w / 2 - self.total_deaths_render.get_width() - HUD.middle_gap, HUD.border + 17 * 2))
        display.blit(self.total_recoveries_render, (HUD.screen_w / 2 + HUD.middle_gap, HUD.border + 17 * 2))
        display.blit(self.people_alive_render, (HUD.screen_w / 2 - self.people_alive_render.get_width() - HUD.middle_gap, HUD.border + 17 * 3))
        display.blit(self.virus_discovered_render, (HUD.screen_w / 2 + HUD.middle_gap, HUD.border + 17 * 3))

        # right side of top hud will have virus settings

        