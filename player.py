import math
from random import randint
import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, RLEACCEL

class Player(pygame.sprite.Sprite):
    x: int = 50
    y: int = 780
    points: int = 0

    def __init__(self):
        super(Player, self).__init__()

        self.surf = pygame.image.load("images/c.png").convert()
        self.surf = pygame.transform.scale(self.surf, (35, 35))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.speed = 3
        self.rect = self.surf.get_rect(center = (self.x, self.y))

    def move(self, pressed_keys) -> None:
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 800:
            self.rect.bottom = 800


class Santa(pygame.sprite.Sprite):
    x: int
    y: int

    def __init__(self):
        super(Santa, self).__init__()

        self.surf = pygame.image.load("images/s.png").convert()
        self.surf = pygame.transform.scale(self.surf, (60, 60))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.x = randint(50, 750)
        self.y = randint(50, 750)
        spawn_santas = (self.x, self.y)
        self.rect = self.surf.get_rect(center = spawn_santas)

    def distance(self, player: Player) -> float:
        dist: float = math.sqrt((self.x - player.rect.x) ** 2 + (self.y - player.rect.y) ** 2)
        return dist

    def collision(self, player: Player) -> bool:
        if self.distance(player) <= 20:
            return True
        return False


class Grinch(pygame.sprite.Sprite):
    x: int
    y: int

    def __init__(self):
        super(Grinch, self).__init__()

        self.surf = pygame.image.load("images/g.png").convert()
        self.surf = pygame.transform.scale(self.surf, (60, 60))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.x = randint(50, 750)
        self.y = randint(50, 750)
        spawn_grinch = (self.x, self.y)
        self.rect = self.surf.get_rect(center = spawn_grinch)

    def distance(self, player: Player) -> float:
        dist: float = math.sqrt((self.x - player.rect.x) ** 2 + (self.y - player.rect.y) ** 2)
        return dist

    def collision(self, player: Player) -> bool:
        if self.distance(player) <= 20:
            return True
        return False