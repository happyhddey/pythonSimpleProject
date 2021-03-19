# 구현해야 하는 함수들

def initializeBoard():
    gameBoard = []
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE
    return gameBoard


def printBoard(gameBoard):
    print("\n====== BOARD ======\n")
    print("      ", end="")
    for i in range(3):
        print("B=%d " % (i+1), end="")
    print("\n")
    for i in range(3):
        print(" A=%d   " % (i+1), end="")
        ithLine = gameBoard[i]
        for i in range(3):
            print(ithLine[i], "  ", end="")
        print("\n")
    print("===================\n")


def inputAB(currentPlayer):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE


def isRightRange(A, B):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE


def getABonBoard(A, B):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE


def isEmptyCell(gameBoard, A, B):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE


def updateBoard(gameBoard, A, B, mark):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE


def getNextPlayer(player):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE


def isBingoInA(gameBoard):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE


def isBingoInB(gameBoard):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE


def isBingoInDiagonal(gameBoard):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE


def isBingo(gameBoard):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE


def isFull(gameBoard):
    # IMPLEMENT
    # YOUR
    # CODE
    # HERE





# MAIN

startPlayer = 'x'

isEndOfGame = False
gameBoard = initializeBoard()
player = startPlayer

while not isEndOfGame:
    printBoard(gameBoard)
    inputA, inputB = inputAB(player)
    
    if isRightRange(inputA, inputB):
        A, B = getABonBoard(inputA, inputB)
        
        if isEmptyCell(gameBoard, A, B):
            updateBoard(gameBoard, A, B, player)
            
            if isBingo(gameBoard):
                printBoard(gameBoard)
                print("축하합니다!!! 승자는: %s 입니다." % player)
                isEndOfGame = True
            elif isFull(gameBoard):
                printBoard(gameBoard)
                print("보드판이 다 찼습니다. 숫자를 다시 입력해주세요.")
                isEndOfGame = True
            else:
                player = getNextPlayer(player)
        
        else:
            print("이미 채워진 칸입니다. 숫자를 다시 입력해주세요.")
    
    else:
        print("범위를 벗어난 숫자를 선택하였습니다. 숫자를 다시 입력해주세요.")