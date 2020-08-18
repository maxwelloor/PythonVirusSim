import pygame

class Button:

    pygame.init()

    list = []
    font = pygame.font.SysFont('comicsans', 32)
    black = (0, 0, 0)
    gray = (128, 128, 128)
    dark_gray = (100, 100, 100)

    def __init__(self, t, number_picker_parent, x, y):
        # type is 0, 1 or 2. 0 for the > button that adds 1, 1 is for the >> button that adds 10, 2 is for the >>> button that adds 100.
        
        self.type = t
        self.parent = number_picker_parent
        self.scrolled_over = False
        self.offset = 7
        self.x = x
        self.y = y
        self.w = 50
        self.h = 40

        if self.type == 0:
            self.arrow_render = Button.font.render('>', 1, Button.black)
        elif self.type == 1:
            self.arrow_render = Button.font.render('>>', 1, Button.black)
        elif self.type == 2:
            self.arrow_render = Button.font.render('>>>', 1, Button.black)
        elif self.type == 3:
            self.arrow_render = Button.font.render('<', 1, Button.black)
        elif self.type == 4:
            self.arrow_render = Button.font.render('<<', 1, Button.black)
        elif self.type == 5:
            self.arrow_render = Button.font.render('<<<', 1, Button.black)

        Button.list.append(self)

    def clicked(self):
        if self.type == 0:
            self.parent.value += 1
            if self.parent.value > self.parent.max:
                self.parent.value = self.parent.max
        elif self.type == 1:
            self.parent.value += 10
            if self.parent.value > self.parent.max:
                self.parent.value = self.parent.max
        elif self.type == 2:
            self.parent.value += 100
            if self.parent.value > self.parent.max:
                self.parent.value = self.parent.max
        elif self.type == 3:
            self.parent.value -= 1
            if self.parent.value < self.parent.min:
                self.parent.value = self.parent.min
        elif self.type == 4:
            self.parent.value -= 10
            if self.parent.value < self.parent.min:
                self.parent.value = self.parent.min
        elif self.type == 5:
            self.parent.value -= 100
            if self.parent.value < self.parent.min:
                self.parent.value = self.parent.min

    def render(self, display):
        if not self.scrolled_over:
            pygame.draw.rect(display, Button.gray, (self.x, self.y, self.w, self.h))
        else:
            pygame.draw.rect(display, Button.dark_gray, (self.x, self.y, self.w, self.h))
        
        if self.type == 0:
            display.blit(self.arrow_render, (self.x + 20, self.y + self.offset))
        elif self.type == 1:
            display.blit(self.arrow_render, (self.x + 12, self.y + self.offset))
        elif self.type == 2:
            display.blit(self.arrow_render, (self.x + 6, self.y + self.offset))
        elif self.type == 3:
            display.blit(self.arrow_render, (self.x + 17, self.y + self.offset))
        elif self.type == 4:
            display.blit(self.arrow_render, (self.x + 11, self.y + self.offset))
        elif self.type == 5:
            display.blit(self.arrow_render, (self.x + 5, self.y + self.offset))

class NumberPicker:

    list = []
    font = pygame.font.SysFont('arial', 32)
    white = (255, 255, 255)

    def __init__(self, display, lbl, default_value, min_value, max_value, pos):
        self.display = display
        self.label = lbl
        self.value = default_value
        self.min = min_value
        self.max = max_value
        self.x, self.y = pos
        self.w = 200
        self.h = 40

        self.label_render = NumberPicker.font.render(self.label, 1, Button.black)

        self.buttons = [
        Button(0, self, self.x + 200, self.y),
        Button(1, self, self.x + 255, self.y),
        Button(2, self, self.x + 310, self.y),
        Button(3, self, self.x - 50, self.y),
        Button(4, self, self.x - 105, self.y),
        Button(5, self, self.x - 160, self.y)
        ]

        NumberPicker.list.append(self)

    def render(self):
        
        self.display.blit(self.label_render, (self.x + self.w / 2 - self.label_render.get_width() / 2, self.y - self.label_render.get_height()))
        pygame.draw.rect(self.display, NumberPicker.white, (self.x, self.y, self.w, self.h))
        np_value_render = NumberPicker.font.render(str(self.value), 1, Button.black)
        self.display.blit(np_value_render, ((self.x + self.w / 2) - np_value_render.get_width() / 2, self.y))

        for b in self.buttons:
            b.render(self.display)


class SimulationSetup:

    background = (50, 50, 50)
    font = pygame.font.SysFont('arial', 48)

    def __init__(self, display):
        self.number_pickers = [
        NumberPicker(display, 'Homes', 100, 1, 2000, (200, 100)),
        NumberPicker(display, 'Stores', 100, 1, 2000, (200, 200)),
        NumberPicker(display, 'Starting Infections', 2, 1, 100, (200, 300)),
        NumberPicker(display, 'Average Persons IQ', 50, 1, 100, (200, 400)),
        NumberPicker(display, 'Persons IQ Range', 50, 1, 100, (200, 500)),
        NumberPicker(display, 'Spread Chance', 10, 1, 1000, (855, 100)),
        NumberPicker(display, 'Lethality', 30, 1, 1000, (855, 200)),
        NumberPicker(display, 'Noticibility', 3, 1, 1000, (855, 300)),
        NumberPicker(display, 'Recovery Time', 10, 1, 200, (855, 400)),
        NumberPicker(display, 'Recovery Chance', 50, 1, 1000, (855, 500))
        ]

        self.press_enter_render = SimulationSetup.font.render('Press Enter to Start...', 1, Button.black)
        self.simulation_settings_render = SimulationSetup.font.render('Simulation Settings:', 1, Button.black)
        self.virus_settings_render = SimulationSetup.font.render('Virus Settings:', 1, Button.black)

        self.display = display
        self.run = True
        self.menu_loop()

    def end_setup(self):
       self.setup_dic = {}

       for np in self.number_pickers:
           self.setup_dic[np.label] = np.value
       
       self.run = False

    def menu_loop(self):
        while self.run:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    for button in Button.list:
                        if pygame.Rect(button.x, button.y, button.w, button.h).collidepoint(pos):
                            button.clicked()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.end_setup()

            m_pos = pygame.mouse.get_pos()

            for button in Button.list:
                if pygame.Rect(button.x, button.y, button.w, button.h).collidepoint(m_pos):
                    button.scrolled_over = True
                else:
                    button.scrolled_over = False

            self.display.fill(SimulationSetup.background)

            self.display.blit(self.simulation_settings_render, (100, 0))
            self.display.blit(self.virus_settings_render, (1920 / 2 - self.virus_settings_render.get_width() / 2, 0))

            for np in self.number_pickers:
                np.render()

            self.display.blit(self.press_enter_render, (1920 / 2 - self.press_enter_render.get_width() / 2, 800))

            pygame.display.update()
            pygame.event.pump()

    def get_setup_dic(self):
        return self.setup_dic

