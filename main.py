import pygame
import pygame.freetype
from backgrounds import Background
from player import Player, Santa, Grinch
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()
pygame.font.init()
# FONT = pygame.font.SysFont('Comic Sans MS', 30)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
screen = width, height = 800, 800
disp = pygame.display.set_mode(screen)

player_list = pygame.sprite.Group()
santa_list = pygame.sprite.Group()
grinch_list = pygame.sprite.Group()
win_zone_group = pygame.sprite.GroupSingle()
all_sprites = pygame.sprite.Group()

background = Background()
player = Player()
player_list.add(player)
all_sprites.add(player)
    
ADDSANTA = pygame.USEREVENT + 1
pygame.time.set_timer(ADDSANTA, 1, 8)
santa_count: int = 8
ADDGRINCH = pygame.USEREVENT + 2
pygame.time.set_timer(ADDGRINCH, 1, 8)
grinch_count: int = 3

clock = pygame.time.Clock()


def main() -> None:
    global santa_count
    global grinch_count
    running = True
    # h1 = FONT.render(f"Points: {player.points}", True, BLACK, WHITE)
    # textRect = h1.get_rect()
    # textRect.center = (40, 40)
    # disp.blit(h1, textRect)
    while running:
        # disp.blit(h1, textRect)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == ADDSANTA:
                new_santa = Santa()
                santa_list.add(new_santa)
                all_sprites.add(new_santa)
            elif event.type == ADDGRINCH:
                new_grinch = Grinch()
                grinch_list.add(new_grinch)
                all_sprites.add(new_grinch)

        pressed_keys = pygame.key.get_pressed()
        player.move(pressed_keys)

        disp.fill((250,235,215))
        background.update()
        background.render(disp)
        
        for santa in santa_list:
            if player.rect.colliderect(santa.rect):
                santa.kill()
                player.points += 5
                santa_count -= 1
        for grinch in grinch_list:
            if player.rect.colliderect(grinch.rect):
                grinch.kill()
                player.points -= 10
                grinch_count -= 1
        
        if santa_count == 0 or grinch_count == 0:
            running = False
        
        for entity in all_sprites:
            disp.blit(entity.surf, entity.rect)
        
        pygame.display.flip()
        clock.tick(60)
        

if __name__ == "__main__":
    main()