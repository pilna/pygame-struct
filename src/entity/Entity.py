import pygame

class Entity:
    """
    image = {
        "run": ...img,
        "walk": ...img
    }
    """

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def animate(self, image):
        pass

"""
class Animation:

    def __init__(self, entity_directory: str):
        pass

class Metatruc(type):
    
    def __init__(cls, name, bases, dct):
        cls.value = "lala"
        def test(self):
            print("hello world")
        setattr(cls, "test", test)
        
class A(metaclass=Metatruc):
    pass

print(A().test())
"""