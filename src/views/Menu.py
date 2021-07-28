from __future__ import annotations
from typing import TYPE_CHECKING
from src.views.View import View
import pygame

if TYPE_CHECKING:
    from src.views.ViewsManager import ViewsManager


class Menu(View):
    
    def __init__(self, manager: ViewsManager) -> None:
        View.__init__(self, manager)
        self.color = (255, 0, 0)
    
    def handle_event(self, event: pygame.Event) -> None:
        if event.type == pygame.KEYDOWN:
            self.color = (24, 56, 78)
    
    def update(self) -> None:
        pass
    
    def render(self, screen: pygame.Surface) -> None:
        screen.fill(self.color)