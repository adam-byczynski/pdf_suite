#Pdf suite which allows to manipulate pdfs in different ways

import os
from msvcrt import getch


#imports of own pdf scripts
import merge_pdfs
import split_pdf_at_page

ENTER_KEYCODE = 13
ESCAPE_KEYCODE = 27


def initial_setup():
      os.system('cls')
      print("\n") # for readability
      print("Welcome to the Rock, Paper, Scissors Game!")
      print("Two people are required to play, obviously.")
      print("Press Enter to start the game...")
      while(True):
            key_pressed = ord(getch())
            if key_pressed == ENTER_KEYCODE:
                  return
            elif key_pressed == ESCAPE_KEYCODE:
                  quit()
                  

def quit_or_play():
        print("Press Enter to play again, or Escape to quit...")
        while(True):
            play_again = ord(getch())
            if play_again == ESCAPE_KEYCODE:
                quit()
            elif play_again == ENTER_KEYCODE:
                break  
            
def main():
      while(True): 
            initial_setup()
            p1_choice, p2_choice = collect_input()
            evaluate_input(p1_choice,p2_choice)
            quit_or_play()

main()