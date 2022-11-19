import pygame

class Background():
    
    def __init__(self):
        super(Background, self).__init__()

        surface = pygame.image.load("images/white.jpg").convert()
        self.surf = pygame.transform.scale(surface, (800, 800))
        
        self.x = 0
        self.y = 0
        self.speed = 0
        
    def update(self):
        self.x -= self.speed

    def render(self, display):
        display.blit(self.surf, (self.x, self.y))