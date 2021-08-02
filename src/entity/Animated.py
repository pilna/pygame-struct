from os import listdir, path
import pygame

class Animated(type):

    def __init__(cls, name, attrs, dct):
        super(Animated, cls).__init__(name, attrs, dct)
        path_entity_animation = f"assets/img/{cls.__name__}"
        animations_img = {}

        for file_name in listdir(path_entity_animation):
            if path.isdir(path.join(path_entity_animation, file_name)):
                animations_img[file_name] = [
                    pygame.image.load(path.join(path_entity_animation, file_name, img)) 
                    for img in listdir(path.join(path_entity_animation, file_name)) 
                    if path.isfile(path.join(path_entity_animation, file_name, img))
                ]
            else:
                animations_img["default"] = [pygame.image.load(path.join(path_entity_animation, file_name))]
        
        cls.animations = animations_img
        cls.get_image = Animated.get_image


    def get_image(self, animation_name, animation_speed=1):
        if not hasattr(self, "animation_index"):
            self.animation_index = 0

        self.animation_index += animation_speed
        
        return type(self).animations[animation_name][int(self.animation_index) % len(type(self).animations[animation_name])]

            

class Player(metaclass=Animated):
    pass