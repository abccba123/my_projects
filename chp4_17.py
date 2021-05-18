'''
(Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper
game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
2 and displays a message indicating whether the user or the computer wins, loses,
or draws.
'''

import random
import math

Computer = random.randint(0,2)
User = int(input("Scissor (0), rock (1), paper (2), Enter either 0,1,2 for the game"))

if (Computer == 0 ) and (User ==0):
    print("The computer is scissor. You are scissor too. It is a Draw")
elif (Computer ==1) and (User ==0):
    print("The computer is rock. You are scissor. You lose")
elif (Computer ==2) and (User ==0):
    print("The computer is paper. You are scissor. You lose")
elif (Computer ==0) and (User == 1):
    print("The computer is scissor. You are rock. You Win")
elif (Computer ==1) and (User == 1):
    print("The computer is rock. You are rock too. It is a Draw")
elif (Computer ==2) and (User == 1):
    print("The computer is paper. You are rock. You lose")
elif (Computer ==0) and (User == 2):
    print("The computer is scissor. You are paper. You Win")
elif (Computer ==1) and (User == 2):
    print("The computer is rock. You are paper. You Win")
elif (Computer ==2) and (User == 2):
    print("The computer is paper. You are paper too. It is a Draw")

