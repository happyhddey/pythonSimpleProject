### Initialize exercises

REGNUM = 20
PRINTSTEP = 5
register = []
for i in range(REGNUM):
    register.append(0)

def initializeRegister():
    for i in range(REGNUM):
        register[i] = 0

def printRegister():
    iteration = int(REGNUM/PRINTSTEP)
    print("\n==== REGISTER =============================================================")
    for i in range(PRINTSTEP):
        for j in range(iteration):
            index = i + PRINTSTEP * j
            print("  REG[%2d] %7d" %(index, register[index]), end="  ")
        print("\n", end="")
    print("============================================================================\n")

def printExerciseFormatStart(exerciseNum):
    print("\n#### EXERCISE %1d ############################################################" % exerciseNum)

def printExerciseFormatEnd():
    print("#############################################################################\n\n\n")

def exerciseRoutine(exerciseFun, exerciseNum):
    initializeRegister()
    printExerciseFormatStart(exerciseNum)
    exerciseFun()
    printRegister()
    printExerciseFormatEnd()



### Here are MIPS instructions

def add(rd, rs, rt):
    register[rd] = register[rs] + register[rt]

def sub(rd, rs, rt):
    register[rd] = register[rs] - register[rt]

def mult(rd, rs, rt):
    register[rd] = register[rs] * register[rt]

def addi(rd, rs, imm):
    register[rd] = register[rs] + imm

def subi(rd, rs, imm):
    register[rd] = register[rs] - imm

def sll(rd, rt, sa):
    register[rd] = register[rt] << sa

def srl(rd, rt, sa):
    register[rd] = register[rt] >> sa




### EXERCISE 0: Implement code you want

def exercise0():
    pass

exerciseRoutine(exercise0, 0)



### EXERCISE 1: result in REG[10]

def exercise1():
    addi(9, 0, 9)
    sll(10, 9, 2)
    add(10, 10, 9)

exerciseRoutine(exercise1, 1)



### EXERCISE 2: result in REG[6]

def exercise2():
    addi(6, 0, 6)
    addi(5, 0, 9)
    add(6, 6, 5)
    add(6, 6, 5)
    add(6, 6, 5)
    add(6, 6, 5)
    add(6, 6, 5)
    add(6, 6, 5)

exerciseRoutine(exercise2, 2)



### EXERCISE 3: result in REG[6]

def exercise3():
    addi(5, 5, 1)
    add(6, 6, 5)
    addi(5, 5, 1)
    add(6, 6, 5)
    addi(5, 5, 1)
    add(6, 6, 5)
    addi(5, 5, 1)
    add(6, 6, 5)
    addi(5, 5, 1)
    add(6, 6, 5)
    addi(5, 5, 1)
    add(6, 6, 5)
    addi(5, 5, 1)
    add(6, 6, 5)
    addi(5, 5, 1)
    add(6, 6, 5)
    addi(5, 5, 1)
    add(6, 6, 5)
    addi(5, 5, 1)
    add(6, 6, 5)

exerciseRoutine(exercise3, 3)



### EXERCISE 4: result in REG[6]

def exercise4():
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)
    addi(5, 5, 1)
    mult(6, 5, 5)

exerciseRoutine(exercise4, 4)



### EXERCISE 5: Implement code to calculate Fibonacci number, result in REG[3]

def exercise5():
    pass

exerciseRoutine(exercise5, 5)



### EXERCISE 6: Implement what you want for teacher to solve

def exercise6():
    pass

exerciseRoutine(exercise6, 6)
