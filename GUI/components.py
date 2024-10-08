import pygame
import pygame_gui  # type: ignore


class Button(pygame.sprite.Sprite):
    """
    The Button class represents a button in the GUI.
    """
    def __init__(self, x, y, width, height, text):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.color = '#FDD726'
        self.hover_color = '#ECC615'
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.rendered_text = self.font.render(text, True, (0, 0, 0))
        self.text_rect = self.rendered_text.get_rect(center=self.rect.center)

    def update(self, surface, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surface.blit(self.rendered_text, self.text_rect)
    

class Label(pygame.sprite.Sprite):
    """
    The Label class represents a label in the GUI.
    """
    def __init__(self, x, y, text, font_size, color=(0, 0, 0)):
        super().__init__()
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.color = color
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def update(self, surface, mouse_pos):
        self.image = self.font.render(self.text, True, self.color)
        surface.blit(self.image, self.rect)


class DropDown(pygame_gui.elements.UIDropDownMenu):
    """
    The DropDown class represents a drop down menu for choices in the GUI.
    """
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
    """
    The TextBox class represents a text box for entering text in the GUI.
    """
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
    """
    The Label_UI class represents a label in the GUI.
    """
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

class ImcompatibleConfigError(Exception):
    """
    The ImcompatibleConfigError class represents an error when the configuration is incompatible.
    """
    def __init__(self, *args) -> None:
        super().__init__(*args)