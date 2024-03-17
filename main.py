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
import cmpt120imageManip as manip


####### interactive program
####### greet user
print("---------------")
print("Welcome to Interactive Image Processor!\n")
contd = True
while contd:
  img = helper.getImage('week9-photo.jpg')
  final = helper.getImage('week9-photo.jpg')
  print("-------")
  print("Here are your options >>>")
  print("0: Quit")
  print("1: Cover the right half with black color")
  print("2: Swap all the red components with the blue components")
  print("3: Flip the image vertically")
  print("4: Invert the color of the image")
  print("5: Convert the color of the image into grayscale")
  print('')

  ####### ask for user input
  option = input("Enter your choice (0/1/2/3/4/5): ")

  ####### calling functions
  # chose option 0
  if option == '0':
    print("Quitting program...")
    contd = False
  # chose option 1
  elif option == '1':
    print("Chose option 1")
    final = manip.coverRightHalf(final)
    helper.saveImage(final, 'result-option1.jpg')
  # chose option 2
  elif option == '2':
    print("Chose option 2")
    final = manip.swapRedWithBlue(final)
    helper.saveImage(final, 'result-option2.jpg')
  # chose option 3
  elif option == '3':
    print("Chose option 3")
    final = manip.flipVertical(final,img)
    helper.saveImage(final, 'result-option3.jpg')
  # chose option 4
  elif option == '4':
    print("Chose option 4")
    final = manip.invert(final)
    helper.saveImage(final, 'result-option4.jpg')
  # chose option 5
  elif option == '5':
    print("Chose option 5")
    final = manip.grayscale(final)
    helper.saveImage(final, 'result-option5.jpg')
  # invalid option
  else:
    print("Sorry, I don't understand", option)
    print('\n')


    