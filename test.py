
# playing with array
# Array is a data structure that holds a list of values with similar data type
# Array can have higher dimentions


# 1-d array

def printMyFruits(fruits):
    a = 1
    #print("There are", len(fruits), "fruits in my list.")

    #for fruit in fruits:
        #print(fruit.capitalize())


fruits = ["apple", "watermelon", "pear", "orange", "banana", "mango", "kiwi"]
printMyFruits(fruits)

fruits.append("honeydew")
printMyFruits(fruits)

badFruit = "pears"

if badFruit in fruits:
    fruits.remove("pears")
else:
    print("Lucky day!!! ", badFruit, "not in my list!")

printMyFruits(fruits)


# 2-d array

def printMyDishes(meals):
    print(len(meals))

    for meal in meals:
        for dish in meal:
            print(dish)


"""meals = []

breakfast = ["oatmeal", "pancake", "waffle", "sandwich", "milk"]
lunch = ["pasta", "rice", "leftovers", "noodles", "dumplings"]
dinner = ["pizza", "cake", "icecream", "junkfood", "hamburgers"]

meals.append(breakfast)
meals.append(lunch)
meals.append(dinner)
"""

meals = [["oatmeal", "pancake", "waffle", "sandwich", "milk"],  ["pasta", "rice", "leftovers", "noodles", "dumplings"], ["pizza", "cake", "icecream", "junkfood", "hamburgers"]]

#printMyDishes(meals)

#print(meals[2][1])


def isValidBoard(board):
    if len(board) != 3:  # 1st dimension
        print("how dare u call me with that!!!")
        return False
    
    if len(board[0]) != 3 or len(board[1]) != 3 or len(board[2]) != 3: # 2nd dimensoin
        print("how dare u call me with that second!!!")
        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if (board[r][c] == -1 or board[r][c] == 0 or board[r][c] == 1):
                continue
            else:
                print("How dare u call me with wrong values! Are u out of ur mind!!!")
                return False
    
    return True


# given 3 points, tells if the points form a line and have the same value. 
def isAWinningLine(r1, c1, v1, r2, c2, v2, r3, c3, v3):
    # test if repeat points
    if ((r1 == r2 and c1 == c2) or (r2 == r3 and c2 == c3) or (r1 == r3 and c1 == c3)):
        print("duplicate found.")
        return False 

    # make sure no zero values
    if v1 == 0 or v2 == 0 or v3 == 0:
        return False

    #test if form a straight line

    isSameRow = (r1 == r2 and r2== r3)
    isSameCol = (c1 == c2 and c2 == c3)
    isDiag1 = (r1 == c1 and r2 == c2 and r3 == c3)
    isDiag2 = (r1 + c1 == 2 and r2 + c2 == 2 and r3 + c3 == 2)

    isSameVal = (v1 == v2 and v2== v3)


    return (isSameRow or isSameCol or isDiag1 or isDiag2) and isSameVal


#given three values that form a line, find out who won
def whoWon(val1, val2, val3):
    if (val1 and val2 and val3) == 1:
        return "O wins!"

    if (val1 and val2 and val3) == -1:
        return "X wins!"
    
    return "Does not have the same value"


print(whoWon(-1,-1,-1))


def didAnyoneWin(v1, v2, v3):
    if (v1 or v2 or v3) == 0:
        return False

    return v1 == v2 and v2 == v3
    

# given a 2-d (3 * 3) board, return if a player won or nobody won
# board values should only be -1 (O), 0, 1 (X)
def didIWin(board):
    if not isValidBoard(board):
        return "What did u say?"

    # check rows
    for r in range(len(board)):
        player = "X" if board[r][0] == 1 else "O"

        #if isAWinningLine(r, 0, board[r][0], r, 1, board[r][1], r, 2, board[r][2]):
        if didAnyoneWin(board[r][0], board[r][1], board[r][2]):
            return player + " Won!!!"

    #check columns
    for c in range(len(board[0])):
        player = "X" if board[0][c] == 1 else "O" 

        #if isAWinningLine(0, c, board[0][c], 1, c, board[1][c], 2, c, board[2][c]):
        if didAnyoneWin(board[0][c], board[1][c], board[2][c]):
            return player + " Won!!!"

    #check diagonal 1
    player = "X" if board[0][0] == 1 else "O"

    #if isAWinningLine(0, 0, board[0][0], 1, 1, board[1][1], 2, 2, board[2][2]):
    if didAnyoneWin(board[0][0], board[1][1], board[2][2]):
        return player + " Won!!!"

    #check diagonal 2
    player = "X" if board[0][2] == 1 else "O"

    #if isAWinningLine(0, 2, board[0][2], 1, 1, board[1][1], 2, 0, board[2][0]):
    if didAnyoneWin(board[0][2], board[1][1], board[2][0]):
        return player + " Won!!!"

    return 'dummy'



b = [[-1, 0, 1], 
     [1, -1, 1], 
     [1, 1, 1]]

print(didIWin(b))

#make sure x and o cannot win at the same time
# make sure that the difference of number of -1 and 1 has to be by a difference of 1 bc o and x hsould have the same nubmer of turns,s of course differnecce of one depending on who starts first.

"""from tkinter import *
import tkinter
tkinter.dnd 

def create_widgets(self):


import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
    """

print ()