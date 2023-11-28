import pygame
import pygame_gui  # type: ignore


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.rendered_text = self.font.render(text, True, (0, 0, 0))
        self.text_rect = self.rendered_text.get_rect(center=self.rect.center)

    def update(self, surface, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.image.fill((0, 235, 0))
        else:
            self.image.fill((0, 255, 0))
        surface.blit(self.rendered_text, self.text_rect)
    


class Label(pygame.sprite.Sprite):
    def __init__(self, x, y, text, font_size, color=(0, 0, 0)):
        super().__init__()
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.color = color
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)



class DropDown(pygame_gui.elements.UIDropDownMenu):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        dropdown_options: list[str],
        ui_manager: pygame_gui.UIManager,
        uid: str,
    ) -> None:
        dropdown_rect = pygame.Rect(x, y, width, height)
        super().__init__(
            options_list=dropdown_options,
            starting_option=dropdown_options[0],
            relative_rect=dropdown_rect,
            manager=ui_manager,
            object_id=uid,
        )

class TextBox(pygame_gui.elements.UITextEntryLine):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        ui_manager: pygame_gui.UIManager,
        uid: str,
    ) -> None:
        text_box_rect = pygame.Rect(x, y, width, height)
        super().__init__(
            relative_rect=text_box_rect,
            manager=ui_manager,
            object_id=uid,
        )
        
class Label_UI(pygame_gui.elements.UILabel):
    def __init__(self, 
                 x: int, 
                 y: int, 
                 width: int, 
                 height: int,
                 text: str, 
                 ui_manager: pygame_gui.UIManager, 
                 uid: str
                 ) -> None:
        label_rect = pygame.Rect(x, y, width, height)
        super(). __init__(relative_rect=label_rect, 
                          text=text, 
                          manager=ui_manager, 
                          object_id=uid
                          )