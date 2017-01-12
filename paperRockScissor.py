import random
def game(first,second):

    if first==second:
        print"You choose:",first
        print"Computer Choose:",second
        print"It is a tie"
    elif first=="rock":
        if second=="scissors":
          print"You choose:",first
          print"Computer Choose:",second
          print"You win"
        else:
            print"You choose:",first
            print"Computer Choose:",second
            print"You lose!"
    elif first =="paper":
        if second=="rock":
          print"You choose:",first
          print"Computer Choose:",second
          print"You Win!"
        else:
            print"You choose",first
            print"Computer Choose:",second
            print"You lose!"
    elif first =="scissors":
        if second=="paper":
          print"You choose:",first
          print"Computer Choose:",second
          print"You Win!"
        else:
            print"You choose:",first
            print"Computer Choose:",second
            print"You lose!"

userHand=raw_input("What will you choose ? , paper,rock,or scissors:")
computerHand= random.random()

if computerHand <=.33:
    computerHand="paper"
elif computerHand <=.66:
    computerHand="rock"
else:
    computerHand="scissors"

game(userHand,computerHand)
