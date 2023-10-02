import pygame
import matplotlib.pyplot as plt
# Initialize Pygame
pygame.init()

# Create a Pygame window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Legend Example")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw shapes and labels for the legend
    pygame.draw.rect(screen, red, (50, 50, 20, 20))
    pygame.draw.rect(screen, blue, (50, 80, 20, 20))
    font = pygame.font.Font(None, 36)
    text_red = font.render("Red", True, black)
    text_blue = font.render("Blue", True, black)
    screen.blit(text_red, (80, 50))
    screen.blit(text_blue, (80, 80))
	

    # Update the display
    pygame.display.flip()
plt.legend()
# Quit Pygame
pygame.quit()
