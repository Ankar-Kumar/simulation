# import pygame
import pygame

# initializing pygame
pygame.font.init()

# check whether font is initialized
# or not
pygame.font.get_init()

# create the display surface
display_surface = pygame.display.set_mode((500, 500))

# change the window screen title
pygame.display.set_caption('Our Text')

# Create a font file by passing font file
# and size of the font
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
# font2 = pygame.font.SysFont('chalkduster.ttf', 40)

# Render the texts that you want to display
text1 = font1.render('GeeksForGeeks', True, (0, 255, 0))
# text2 = font2.render('GeeksForGeeks', True, (0, 255, 0))

# create a rectangular object for the
# text surface object
textRect1 = text1.get_rect()


# setting center for the first text
textRect1.center = (350, 250)


while True:

	# add background color using RGB values
	display_surface.fill((255, 0, 0))

	display_surface.blit(text1, textRect1)
	
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
		
			# deactivating the pygame library
			pygame.quit()

			# quitting the program.
			quit()

		# update the display
		pygame.display.update()
