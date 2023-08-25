import pygame
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic
            'flame': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/flame/frames'),  # noqa: E501
            'aura': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/aura'),  # noqa: E501
            'heal': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/heal/frames'),  # noqa: E501
            
            # attacks 
            'claw': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/claw'),  # noqa: E501
            'slash': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/slash'),  # noqa: E501
            'sparkle': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/sparkle'),  # noqa: E501
            'leaf_attack': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf_attack'),  # noqa: E501
            'thunder': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/thunder'),  # noqa: E501
 
            # monster deaths
            'squid': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/smoke_orange'),  # noqa: E501
            'raccoon': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/raccoon'),  # noqa: E501
            'spirit': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/nova'),  # noqa: E501
            'bamboo': import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/bamboo'),  # noqa: E501
            
            # leafs 
            'leaf': (
                import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf1'),  # noqa: E501
                import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf2'),  # noqa: E501
                import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf3'),  # noqa: E501
                import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf4'),  # noqa: E501
                import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf5'),  # noqa: E501
                import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf6'),  # noqa: E501
                self.reflect_images(import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf1')),  # noqa: E501
                self.reflect_images(import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf2')),  # noqa: E501
                self.reflect_images(import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf3')),  # noqa: E501
                self.reflect_images(import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf4')),  # noqa: E501
                self.reflect_images(import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf5')),  # noqa: E501
                self.reflect_images(import_folder('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/graphics/particles/leaf6'))  # noqa: E501
                )
            }

    def reflect_images(self,frames):
        new_frames = []
        
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame,True,False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self,pos,groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos,animation_frames,groups)

    def create_particles(self,animation_type,pos,groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos,animation_frames,groups)

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames,groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()