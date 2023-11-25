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
        self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Card Game Designer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.quit=Button(370, 530, 260, 60, "Quit")
        self.all_sprites.add(self.quit)
    
    
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.display_stage()
        pygame.quit()
        sys.exit()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit.rect.collidepoint(event.pos):
                    print("Quit Clicked!")
                    self.running = False
        return True
    
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def openning(self):
        """
        Display the GUI for the game at the initial state. (Stage 0)
        It will display 3 buttons: create new templates, load templates, quit.
        Create new templates: users can create new templates for the game.
        Load templates: users can load the templates they have created before.
        """
        self.create_new = Button(370, 350, 260, 60, "Create new templates")
        self.load = Button(370, 440, 260, 60, "Load templates")
        self.all_sprites.add(self.create_new)
        self.all_sprites.add(self.load)
        self.create_new.draw_text(self.screen)
        self.load.draw_text(self.screen)
        self.quit.draw_text(self.screen)
        return True

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
        stage = self.stage
        if stage == 0:
            self.screen.fill((255, 255, 255))
            self.all_sprites.draw(self.screen)
            self.all_sprites.update()
            self.openning()
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
    gui.run()