# initialising pygame
import pygame
pygame.init()

#setting the dimensions of the screen
screen_width = 900
screen_height = 900

#setting the surface and colour that the landscape will be drawn on
surface = pygame.display.set_mode((screen_width, screen_height))
colour = (250, 250, 250)
surface.fill(colour)

#setting the speed that objects will be moving at
clock = pygame.time.Clock()

#setting the background, which is a nature landscape, making it cover the entire display area
background = pygame.image.load("grass.jpg")
background = pygame.transform.scale(background, (900, 900))
background_x = 0
background_y = 0

#Importing the samurai character to the landscape, and setting its size and location
character_1 = pygame.image.load("sam.png")
character_1 = pygame.transform.scale(character_1, (300,300))
character_1_x = 600
character_1_y = 500

#setting the original location of the bird
bird_x = 0
bird_y = 70

#Importing the moon image and setting its size and location
moon = pygame.image.load("moon.png")
moon = pygame.transform.scale(moon, (100, 100))
moon_x = 0
moon_y = 350


#Importing the tree image and setting its size and location
tree = pygame.image.load("treee.png")
tree = pygame.transform.scale(tree, (700, 700))
tree_x = 200
tree_y = 50


#Updating the display, as well as displaying the images, and adding a function to stop the display
running = True
count = 0

# Lines 53 to 60 are code I got from ChatGPT
# Animating the bird by using 4 images, then displaying the 4 images
bird_frames = []
for i in range(4):
    animation = f"Egle{i}.png"
    frame = pygame.image.load(animation)
    frame = pygame.transform.scale(frame, (160,160))
    bird_frames.append(frame)
frame_index = 0
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    surface.fill(colour)
#displaying the images
    surface.blit(background, (background_x, background_y))
    surface.blit(character_1, (character_1_x, character_1_y))
    surface.blit(moon, (moon_x, moon_y))
    surface.blit(tree, (tree_x, tree_y))
 #Making the moon move   
    moon_x += 8
    moon_y -= 4
    if moon_x == 400:
        moon_x += 8
        moon_y += 4
    if moon_x == 800:
        moon_x = 0
        moon_y = 350

   
  #Making the bird move  
    bird_x += 8
    if bird_x >= 800:
        bird_x = 0
#Creating a frame count speed for the bird animation to move at
    frame_count += 1
    if frame_count > 5:
        frame_count = 0
    frame_index += 1
    if frame_index > 3:
        frame_index = 0


    bird = bird_frames[frame_index]
    surface.blit(bird, (bird_x, bird_y))

    

    
    
    
#Updating the display, as well as setting a speed for everything to move at
    pygame.display.update()
    clock.tick(12)

pygame.quit()