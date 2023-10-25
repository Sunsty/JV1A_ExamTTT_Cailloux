# Import



# Fonctions

def display(x):
    line1 = [x[0],x[1],x[2]]
    line2 = [x[3],x[4],x[5]]
    line3 = [x[6],x[7],x[8]]
    print("",line1,"\n",line2,"\n",line3,"\n")

def play(x,y):
    if( y == 0):
        move = int(input("\nJoueur 1 : Case à jouer ?\n")) - 1
        x[move] = "X"
    if( y == 1):
        move = int(input("\nJoueur 2 : Case à jouer ?\n")) - 1
        x[move] = "O"

def checkWin(x):

    win = False

    if(x[0] == x[1] == x[2] and x[0] != " " and x[1] != " " and x[2] != " "):
        win = True
        return(win)
    if(x[3] == x[4] == x[5] and x[3] != " " and x[4] != " " and x[5] != " "):
        win = True
        return(win)
    if(x[6] == x[7] == x[8] and x[6] != " " and x[7] != " " and x[8] != " "):
        win = True
        return(win)
    if(x[0] == x[3] == x[6] and x[0] != " " and x[3] != " " and x[6] != " "):
        win = True
        return(win)
    if(x[1] == x[4] == x[7] and x[1] != " " and x[4] != " " and x[7] != " "):
        win = True
        return(win)
    if(x[2] == x[5] == x[8] and x[2] != " " and x[5] != " " and x[8] != " "):
        win = True
        return(win)
    if(x[0] == x[4] == x[8] and x[0] != " " and x[4] != " " and x[8] != " "):
        win = True
        return(win)
    if(x[2] == x[4] == x[6] and x[2] != " " and x[4] != " " and x[6] != " "):
        win = True
        return(win)
    else:
        win = False
        return(win)
    
def checkFull(x):
    full = True
    i = 0
    while(full and i < len(x)):
        if( x[i] == " " ):
            full = False
            return(full)
        i += 1
    return(full)

# Variables

win = False
full = False
j = 0

# Code

tab = [" "] * 9
display(tab)
while(not win and not full):
    play(tab,j%2)
    display(tab)
    win = checkWin(tab)
    full = checkFull(tab)
    j += 1
if(win):
    print(f"\nBien joué !! Joueur {(j-1)%2 + 1} à gagné la partie")
if(full):
    print("La partie est terminée !! Il n'y a aucun vainqueur")





# Question 6

# Il nous faut definir un tableau plus grand, l'option de choisir une case va devenir choisir une colonne
# Trouver une meilleur manière de vérifier la condition de victoire car il y aura beaucoup plus de combinaisons
# de victoire