class CodeBreaker:
    def __init__(self, size, codeAlphabet):
        self.size = size
        self.codeAlphabet = codeAlphabet
        self.codeBook = {}

    def makeCodeBook(self, codeBookStr):
        codeBook = {}
        for i in range(self.size):
            tempDict = {}
            for j in range(self.size):
                tempDict[self.codeAlphabet[j]] = codeBookStr[i][j]
            codeBook[self.codeAlphabet[i]] = tempDict
        self.codeBook = codeBook

    def breakOneChar(self, ch):
        codeBookRow = ch[0]
        codeBookCol = ch[1]
        return self.codeBook[codeBookRow][codeBookCol]

    def breakCode(self, code):
        answer = ""
        codeSize = len(code) // 2
        for i in range(codeSize):
            oneChar = code[i*2] + code[i*2+1]
            answer += self.breakOneChar(oneChar)
        return answer


def getCodeBookStr(size):
    codeBookStr = []
    for _ in range(size):
        row = input()
        rowList = []
        for ch in row:
            rowList.append(ch)
        codeBookStr.append(rowList)
    return codeBookStr


size = lambda :6
codeAlphabet = ["A", "D", "F", "G", "V", "X"]
codeBreaker = CodeBreaker(size(), codeAlphabet)

codeBookStr = getCodeBookStr(size())
codeBreaker.makeCodeBook(codeBookStr)

end = False
while not end:
    code = input("Enter the code : ")
    print(codeBreaker.breakCode(code))





