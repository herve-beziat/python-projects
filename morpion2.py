
currentPlayer = "X"
winner = None
gameRunning = True

board = [ 
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]

# affichage du tableau de jeu vide
def printBoard(board):
    print(board[0][0] + " " + board[0][1] + " " + board[0][2])
    print(board[1][0] + " " + board[1][1] + " " + board[1][2])
    print(board[2][0] + " " + board[2][1] + " " + board[2][2])

printBoard(board)

bienvenue = input("Bonjour, souhaites tu jouer ou voir les scores?" )


if bienvenue  == "s":
    print("Scores")
elif bienvenue == "j":
    user1 = input("Nom du joueur 1: ")
    user2 = input("Nom du joueur 2: ")

