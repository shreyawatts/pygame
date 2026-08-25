import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 700,700

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

background_image = pygame.transform.scale(
    pygame.image.load('background.webp').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = pygame.transform.scale(
    pygame.image.load('penguin.jpg').convert_alpha(), (200,200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH//2,
    SCREEN_HEIGHT // 2-30))

text = pygame.font.Font(None, 36).render("Hello World", True,
    pygame.Color("black"))
text_rect = text.get_rect(center=(SCREEN_WIDTH//2,
    SCREEN_HEIGHT // 2+110))

def game_loop():
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.qiut()

if __name__ == '__main__':
    game_loop()