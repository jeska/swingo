from sys import argv
from os import path, listdir
from Image import open
import random

# fillin
# input: card (image)
# output: none
# fills in the blank card with swingo spaces
def fillin(card):
   spaces_dir = "swingo_spaces"
   spaces = getfiles(spaces_dir)
   for x in range(5):
      for y in range(5):
         index = 5*x+y
         if index != 12: # ignores the middle square
            space = open(path.join(spaces_dir, spaces[index]))
            card.paste(space, (10 + 210*x, 232 + 210*y))

# getfiles
# input: dirname (string)
# output: list of image file names (strings)
# pass in a directory name with desired swingo spaces
# randomizes the file names and returns a list of the first 25
def getfiles(dirname):
   images = listdir(dirname)[1:] # ignores '.'
   random.shuffle(images)
   return images[:25]

def main(num_cards):
   for card_num in range(1, num_cards + 1):
      card = open("full_blank.png")
      fillin(card)
      card.save("dancecard" + str(card_num) + ".png")

if __name__ == '__main__':
   if len(argv)!=2:
      print "usage: python swingo.py [num_cards]"
      exit(0)
   else:
      main(int(argv[1]))
