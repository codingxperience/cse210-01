'''
Author: Fred Okorio
Assignment: tic-tac-toe_game
'''

'''
Tic-Tac-Toe is a game in which two players seek in 
alternate turns to complete a row, a column, 
or a diagonal with either three x's or three o's
drawn in the spaces of a grid of nine squares.
'''
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9

# These global variables define specific positions of each number
first_number = one.grid(row=0, column=0)
second_number = two.grid(row=0, column=1)
third_number = three.grid(row=0, column=2)
fourth_number = four.grid(row=1, column=0)
fifth_number = five.grid(row=0, column=3)
sixth_number = six.grid(row=0, column=4)
seventh_number = seven.grid(row=2, column=0)
eigth_number = eight.grid(row=0, column=5)
nineth_number = nine.grid(row=0, column=6)

print('''
         1|2|3
        *******
         4|5|6
        *******
         7|8|9
      '''
      )

player = 'x', 'y'

def main():
  while True:

    choice = int(input(player, 'take your pick(1-9): '))

def substitute_number_for_letter_o(choice):
  '''
  This is function replaces a number chosen by player o
  with a letter o
  '''
  if choice == (1, 2, 3, 4, 5, 6, 7, 8, 9):
    return 'o'


def substitute_number_for_letter_x(choice):
  '''
  This is function replaces a number chosen by player ox
  with a letter x
  '''
  if choice == (1, 2, 3, 4, 5, 6, 7, 8, 9):
    return 'x'
  
   
