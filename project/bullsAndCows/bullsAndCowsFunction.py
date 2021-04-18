import random

def set_answer(size):
    answer = []
    for _ in range(size):
        random_number = random.randrange(1, 10)
        answer.append(str(random_number))
    return ''.join(answer)

def is_over(answer, guess):
    # IMPLEMENT YOUR CODE

def is_right_input(size, my_answer):
    right_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # IMPLEMENT YOUR CODE

def set_guess(size):
    # IMPLEMENT YOUR CODE
    # USE TRY, EXCEPT

def print_score(answer, guess):
    # IMPLEMENT YOUR CODE



size = 3
answer = set_answer(size)
guess = ""
attempt = 0

is_end = False
while not is_end:
    attempt += 1
    guess = set_guess(size)
    if is_over(answer, guess):
        print("NICE GUESS! THE ANSWER IS %s" %answer)
        print("YOUR ATTEMPT: %d" %attempt)
        is_end = True
    else:
        print_score(answer, guess)




    
    
    
