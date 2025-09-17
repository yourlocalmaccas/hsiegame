import pygame

pygame.display.init()
pygame.font.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("HSIE Game")
screen.fill((0, 0, 0))

# Start Button
start_button_rect = pygame.Rect(270, 150, 100, 60)
start_button_color = (255, 255, 255)
start_button_hover_color = (0, 150, 0)
font = pygame.font.Font(None, 38)
start_button_text = font.render("START", True, (0, 0, 0))

# Quit Button
quit_button_rect = pygame.Rect(270, 250, 100, 60)
quit_button_color = (255, 255, 255)
quit_button_hover_color = (150, 0, 0)
quit_button_text = font.render("QUIT", True, (0, 0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                print("Start button clicked!")
            elif quit_button_rect.collidepoint(event.pos):
                running = False

    mouse_pos = pygame.mouse.get_pos()

    # Start button hover color
    if start_button_rect.collidepoint(mouse_pos):
        start_color = start_button_hover_color
    else:
        start_color = start_button_color

    # Quit button hover color
    if quit_button_rect.collidepoint(mouse_pos):
        quit_color = quit_button_hover_color
    else:
        quit_color = quit_button_color
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, start_color, start_button_rect)
    start_text_rect = start_button_text.get_rect(center=start_button_rect.center)
    screen.blit(start_button_text, start_text_rect)


    pygame.draw.rect(screen, quit_color, quit_button_rect)
    quit_text_rect = quit_button_text.get_rect(center=quit_button_rect.center)
    screen.blit(quit_button_text, quit_text_rect)

    pygame.display.flip()

pygame.quit()
