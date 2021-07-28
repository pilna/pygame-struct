from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from src.views.ViewsManager import ViewsManager


class View(metaclass=ABCMeta):

    def __init__(self, manager: ViewsManager) -> None:
        self.manager = manager

    @abstractmethod
    def handle_event(self, event: pygame.Event) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        raise NotImplementedError
