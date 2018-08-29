rad1 = ["", "", ""]
rad2 = ["", "", ""]
rad3 = ["", "", ""]

print ("PlayerX choose a name")
playerX =raw_input()
print("Your name is now " + playerX)
print("PlayerO choose a name")
playerO = raw_input()
print("Your name is now " + playerO)

def gamearea():

    print(rad1[0], rad1[1], rad1[2])
    print(rad2[0], rad2[1], rad2[2])
    print(rad3[0], rad3[1], rad3[2])

def choosexplacement():

    print("Place an X by choosing a number between 1-9")
    x = input()
    if x == 1:
        if rad1[0] == "":
            rad1[0]="X"
        else:
            print("Position taken")
            choosexplacement()
    elif x == 2:
        if rad1[1] == "":
            rad1[1]="X"
        else:
            print("Position taken")
            choosexplacement()
    elif x == 3:
        if rad1[2] == "":
            rad1[2]="X"
        else:
            print("Position taken")
            choosexplacement()
    elif x == 4:
        if rad2[0] == "":
            rad2[0]="X"
        else:
            print("Position taken")
            choosexplacement()
    elif x == 5:
        if rad2[1] == "":
            rad2[1]="X"
        else:
            print("Position taken")
            choosexplacement()
    elif x == 6:
        if rad2[2] == "":
            rad2[2]="X"
        else:
            print("Position taken")
            choosexplacement()
    elif x == 7:
        if rad3[0] == "":
            rad3[0]="X"
        else:
            print("Position taken")
            choosexplacement()
    elif x == 8:
        if rad3[1] == "":
            rad3[1]="X"
        else:
            print("Position taken")
            choosexplacement()
    elif x == 9:
        if rad3[2] == "":
            rad3[2]="X"
        else:
            print("Position taken")
            choosexplacement()
    elif x < 1:
        print("Try again..... pick 1-9.")
        chooseoplacement()
    elif x > 9:
        print("Try again..... pick 1-9.")
        choosexplacement()


def chooseoplacement():

    print("Place an O by choosing a number between 1-9")
    o = input()
    if o==1:
        if rad1[0] == "":
            rad1[0]="O"
        else:
            print("Position taken")
            chooseoplacement()
    elif o == 2:
        if rad1[1] == "":
            rad1[1]="O"
        else:
            print("Position taken")
            chooseoplacement()
    elif o == 3:
        if rad1[2] == "":
           rad1[2]="O"
        else:
           print("Position taken")
           chooseoplacement()
    elif o == 4:
        if rad2[0] == "":
            rad2[0]="O"
        else:
            print("Position taken")
            chooseoplacement()
    elif o == 5:
        if rad2[1] == "":
            rad2[1]="O"
        else:
            print("Position taken")
            chooseoplacement()
    elif o == 6:
        if rad2[2] == "":
            rad2[2]="O"
        else:
            print("Position taken")
            chooseoplacement()
    elif o == 7:
        if rad3[0] == "":
            rad3[0]="O"
        else:
            print("Position taken")
            chooseoplacement()
    elif o == 8:
        if rad3[1] == "":
            rad3[1]="O"
        else:
            print("Position taken")
            chooseoplacement()
    elif o == 9:
        if rad3[2] == "":
            rad3[2]="O"
        else:
            print("Position taken")
            chooseoplacement()
    elif o<1:
        print("Try again..... pick 1-9.")
        chooseoplacement()
    elif o>9:
        print("Try again..... next time pick 1-9.")
        chooseoplacement()


radO=["O","O","O"]
radX = ["X","X","X"]








i = 0

def win():
    raddr= [rad1[0],rad2[1],rad3[2]]
    raddl= [rad1[2],rad2[1],rad3[0]]
    radleft = [rad1[0],rad2[0],rad3[0]]
    radmid =  [rad1[1],rad2[1],rad3[1]]
    radright = [rad1[2],rad2[2],rad3[2]]
    rad_win = [raddr,raddl,radleft,radmid,radright,rad1,rad2,rad3]

    if radO in rad_win:
        print(playerO + " you won!")
        return False
    elif radX in rad_win:
        print(playerX + " you won!")
        return False
    elif i==9:
        print("Tie.....")
        return False

    return True

gamearea()

even = [2,4,6,8]
odd = [1,3,5,7,9]
while i <=9 and win():
    if i in odd:
        choosexplacement()
        gamearea()
        i += 1
    else:
        chooseoplacement()
        gamearea()
        i += 1
