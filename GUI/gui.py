import pygame
import sys

sys.path.append('.')
from data_processing.database import Card, CardDatabase
from operations.config import Config

class GUI():
    def __init__(self):
        """ 
        There are 3 stages of the GUI:
            1. title page
            2. configuration page
            3. game page
        """
        self.stage = 0
        
        pygame.init()
        self.width, self.height = 600, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pygame Template")
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.button = Button(50, 50, 200, 50, "Click Me")
        self.all_sprites.add(self.button)
    
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.rect.collidepoint(event.pos):
                    print("Button Clicked!")
        return True

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def openning(self):
        """
        Display the GUI for the game at the initial state. (title, start a new game, play an old game, quit...)
        """
        pass

    def setting(self)->dict:
        """ 
        Take the user input and set up the game configuration.
        At the page of starting a new game, users have the option to save this configuration and start playing. 
        Return: 
            config (dict): all configurations for the game. (Detail in config/config.py)
        """
        config={}
        return config

    def update_stage(self, stage: int):
        """
        Update the stage of the gui. 
        """
        self.stage = stage
        pass
    
    def display_stage(self):
        """
        Display the current stage of the game.
        """
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        self.button.draw_text(self.screen)
        self.all_sprites.update()
        pygame.display.flip()

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.rendered_text = self.font.render(text, True, (0, 0, 0))
        self.text_rect = self.rendered_text.get_rect(center=self.rect.center)

    def draw_text(self, surface):
        surface.blit(self.rendered_text, self.text_rect)

if __name__ == '__main__':
    gui = GUI()
    while True:
        gui.clock.tick(60)
        if not gui.events(): break
        gui.display_stage()