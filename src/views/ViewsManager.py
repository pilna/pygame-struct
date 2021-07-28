from src.views.View import View
from src.views.Menu import Menu

class ViewsManager:

    def __init__(self, starting_view: View = None) -> None:
        self.current_view = starting_view(self) if starting_view is not None else Menu(self)
    
    def switch_to(self, view: View) -> None:
        self.current_view = view(self)