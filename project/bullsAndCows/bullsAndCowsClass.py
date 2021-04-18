import random

class BaseballGame():
    def __init__(self, size):
        self.size = size
        # set answer
        answer = []
        for _ in range(self.size):
            random_number = random.randrange(1, 10)
            answer.append(str(random_number))
        self.answer = ''.join(answer)
        self.guess = ""
        self.attempt = 0

    def is_right_input(self, my_answer):
        right_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # IMPLEMENT YOUR CODE

    def set_guess(self):
        # IMPLEMENT YOUR CODE
        # USE TRY, EXCEPT

    def print_score(self):
        # IMPLEMENT YOUR CODE

    def is_over(self):
        # IMPLEMENT YOUR CODE
        print("NICE GUESS! THE ANSWER IS %s" %self.answer)
        print("YOUR ATTEMPT: %d" %self.attempt)

    def turn(self):
        self.attempt += 1
        self.set_guess()
        if self.is_over():
            return True
        else:    
            self.print_score()
            return False
        

# ONE PLAYER
size = 3
game = BaseballGame(size)
while not game.is_over():
    game.turn()


# VARIOUS PLAYER
playerList = {}
defaultSize = 3
player = None

while True:
    playerName = input("ENTER PLAYER NAME: ")
    if playerName in playerList:
        player = playerList[playerName]
    else:
        print("START NEW GAME")
        playerList[playerName] = BaseballGame(defaultSize)
        player = playerList[playerName]
    is_end = player.turn()
    if is_end:
        playerList.pop(playerName)
