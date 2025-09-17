import pygame
pygame.display.init()
pygame.font.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("HSIE Game")
screen.fill((0, 0, 0))

start_button_rect = pygame.Rect(270, 150, 100, 60)
start_button_color = (255, 255, 255)
start_button_hover_color = (200, 200, 200)
font = pygame.font.Font(None, 38)
start_button_text = font.render("START", True, (0, 0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_pos = pygame.mouse.get_pos()
    if start_button_rect.collidepoint(mouse_pos):
        color = start_button_hover_color
    else:
        color = start_button_color
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, start_button_rect)
    text_rect = start_button_text.get_rect(center=start_button_rect.center)
    screen.blit(start_button_text, text_rect)

    pygame.display.flip()

pygame.quit()