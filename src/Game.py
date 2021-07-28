from src.views.ViewsManager import ViewsManager
from os import getenv
import pygame

class Game:

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((int(getenv("SCREEN_WIDTH")), int(getenv("SCREEN_HEIGHT"))))
        self.clock = pygame.time.Clock()
        self.views_manager = ViewsManager()
        self.is_running = True

    def run(self) -> None:
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                self.views_manager.current_view.handle_event(event)
            
            self.views_manager.current_view.update()
            self.views_manager.current_view.render(self.screen)
            pygame.display.flip()