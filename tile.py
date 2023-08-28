import pygame
from settings import *  # noqa: F403

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):  # noqa: F405, E501
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]  # noqa: F405
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))  # noqa: F405, E501
        else: 
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,y_offset)