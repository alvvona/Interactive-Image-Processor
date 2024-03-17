##############################
###
# CMPT120 D200
# [CODING EXERCISE] WK9
# INTERACTIVE IMAGE PROCESSOR
#
# AUTHOR: ALINA
# DATE: NOVEMBER 16, 2021


####### imports
import cmpt120imageHelper as helper


####### get image
# images are lists of lists of lists
# lists are mutable
img = helper.getImage('week9-photo.jpg')
final = helper.getImage('week9-photo.jpg')


####### get width and height
height = len(img)
# print('height >>', height)
width = len(img[0])
# print('width >>', width)


####### defining functions
# option 1
def coverRightHalf(pixels):
  for row in range(height):
    for col in range(width):
      if col > int(width/2):
        pixels[row][col] = [0,0,0]
  return pixels

# option 2
def swapRedWithBlue(pixels):
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      pixels[row][col] = [b,g,r]
  return pixels

# option 3
def flipVertical(pixels, p_copy):
  for row in range(height):
    for col in range(width):
        pixels[row][col] = p_copy[height-1-row][col]
  return pixels

# option 4
def invert(pixels):
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      r_inv = 255-r
      g_inv = 255-g
      b_inv = 255-b
      pixels[row][col] = [r_inv,g_inv,b_inv]
  return pixels

# option 5
def grayscale(pixels):
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      gray_img = (r+g+b)/3
      pixels[row][col] = [gray_img,gray_img,gray_img]
  return pixels

