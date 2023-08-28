import pygame
from settings import *  # noqa: F403
from random import randint

class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player
        self.sounds = {
            'heal': pygame.mixer.Sound('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/audio/heal.wav'),  # noqa: E501
            'flame':pygame.mixer.Sound('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/audio/Fire.wav')  # noqa: E501
        }

    def heal(self,player,strength,cost,groups):
        if player.energy >= cost:
            self.sounds['heal'].play()
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles('aura',player.rect.center.groups)
            self.animation_player.create_particles('heal',player.rect.center + pygame.math,Vector2(0,-60).groups)  # noqa: E501, F405

    def flame(self,player,cost,groups):
        if player.energy >= cost:
            player.energy -= cost
            self.sounds['flame'].play()

            if player.status.split ('_')[0] == 'right': direction = pygame.math.Vector2(1,0)  # noqa: E701, E501
            elif player.stats.split ('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)  # noqa: E701, E501
            elif player.stats.split ('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)  # noqa: E701, E501
            else: direction = pygame.math.Vector2(0,1)  # noqa: E701

            for i in range(1,6):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE  # noqa: F405
                    x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)  # noqa: F405, E501
                    y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)  # noqa: F405, E501
                    self.animation_player.create_particles('flame',(x,y),groups)
                else: # vertical
                    offset_y = (direction.y * i) * TILESIZE  # noqa: F405
                    x = player.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)  # noqa: F405, E501
                    y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)  # noqa: F405, E501
                    self.animation_player.create_particles('flame',(x,y),groups)
