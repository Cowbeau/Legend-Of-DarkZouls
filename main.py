import pygame, sys  # noqa: E401
from settings import *  # noqa: F403
from level import Level


class Game:
    def __init__(self):
          
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))  # noqa: F405
        pygame.display.set_caption('Souls of Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('/home/beaum/Documents/Coding Projects/Python Projects/Legend Of DarkZouls/audio/main.ogg')  # noqa: E501
        main_sound.set_volume(0.5)
        main_sound.play(loops = -1)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

                    
            self.screen.fill(WATER_COLOR)  # noqa: F405
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)  # noqa: F405
            
if __name__ == '__main__':
    game = Game()
    game.run()
