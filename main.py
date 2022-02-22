
"""
a function returns True/False based on 
if cor1, cor2, and cor3 are the same value or not.
assume cor1, cor2 and cor3 are all integers
"""
def myFunc(cor1, cor2, cor3):
    result = False

    if (cor1 == cor2 and cor2 == cor3):
         result = True

    return result


def mySimpleFunc(cor1, cor2, cor3):
    return cor1 == cor2 and cor2 == cor3


cor1 = 2
cor2 = 4
cor3 = 2


if myFunc(cor1, cor2, cor3):
    print("YEAH, They are all equal to each other!  World is all the same!!!")

else:
    print("NAHH, Some one is different.  Let's united them!") 


if mySimpleFunc(cor1, cor2, cor3):
    print("YEAH, They are all equal to each other!  World is all the same!!!")

else:
    print("NAHH, Some one is different.  Let's united them!") 


c1 = 0
c2 = 1
c3 = 2
r1 = 0
r2 = 1
r3 = 2
v1 = -1
v2 = -1
v3 = -1


BS = 0
Board = [[BS, BS, BS], [BS, BS, BS], [BS, BS, BS]]
#       BS BS BS
#       BS BS BS
#       BS BS BS


# given 3 points, tells if the points form a line and have the same value. 
def boardFunction(c1,c2,c3,r1,r2,r3,v1,v2,v3):
    # test if repeat points
    if ((r1 == r2 and c1 == c2) or (r2 == r3 and c2 == c3) or (r1 == r3 and c1 == c3)):
        print("duplicate found.")
        return False 

    #test if form a straight line

    isSameRow = (r1 == r2 and r2== r3)
    isSameCol = (c1 == c2 and c2 == c3)
    isDiag1 = (r1 == c1 and r2 == c2 and r3 == c3)
    isDiag2 = (r1 + c1 == 2 and r2 + c2 == 2 and r3 + c3 == 2)

    isSameVal = (v1 == v2 and v2== v3)


    return (isSameRow or isSameCol or isDiag1 or isDiag2) and isSameVal

# given a board, tells if a player wins, and if so, which player wins.
#if boardFunction(c1, c2, c3, r1, r2, r3, v1, v2, v3, Board):
  #  ""for loop
   # all possible combinations of three connected points
  #  save into   variable
   # ru nthough board funciotn
  if boardfunction is true:
      if v1 == -1:
        xWinner == True
    else:
        Owinner == True

    

  #  else, nobody won yet. 
 ##  if boardFunction ""

for loop
 boardFunction(combo1, othercombo1)

def combo1 ():
    c1 = 0
    c2 = 1
    c3 = 2
    r1 = 0
    r2 = 1
    r3 = 2

def combo2 ():
    c1 = 1
    c2 = 2
    c3 = 0
    r1 = 1
    r2 = 2
    r3 = 0

def combo3():
    c1 = 2
    c2 = 0
    c3 = 1
    r1 = 2
    r2 = 0
    r3 = 1

def othercombo1():
v1 = -1
v2 = -1
v3 = -1

def othercombo2():
v1 = 1
v2 = 1
v3 = 1