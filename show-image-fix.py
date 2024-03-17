# The fix for showImage() is from Sean Lam, a student from D200.
from pygame.constants import K_ESCAPE, KEYDOWN, QUIT
import cmpt120imageHelper
import pygame

# img is the image represented in pixels
img = cmpt120imageHelper.getImage("week9-photo.jpg")
while True:
    cmpt120imageHelper.showImage(img)
    for event in pygame.event.get():
        # quit on alt f4 on pc or ⌘q on mac
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
        # quit when you press escape
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                exit()