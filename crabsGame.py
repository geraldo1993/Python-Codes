from random import randint
# is the variable that says the point is set or not
pointOn=False
point=0
roundOver=False
def roll():
    global pointOn,point,roundOver
    dice1=randint(1,6)
    dice2=randint(1,6)
    value=dice1+dice2

    print "The Player rolls a " + str (value)
    if not pointOn:
        if value==2 or value==3 or value==12:
            print"The house Wins"
            roundOver=True
        elif value ==7 or  value==11:
            print"The Player wins"
            roundOver=True
        else:
            point=value
            pointOn=True
            print " The point has been set to " +str(point)
    else:
        if value ==point:
            print "The player wins"
            roundOver=True
        elif value==7:
            print"The house win"
            roundOver=True


while not roundOver:
    roll()
print"Game Over"
