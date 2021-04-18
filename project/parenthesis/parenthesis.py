# list로 구현한 stack
class Stack:

    # Constructor(생성자), 데이터를 저장할 list를 초기화
    def __init__(self):
        self.stack = []
        self.length = 0

    # list가 비어있는지 확인
    def isEmpty(self):

    # list에 데이터(elem) 추가        
    def push(self, elem):

    # list에서 데이터 삭제
    def pop(self):

    # list에서 데이터 반환
    def peek(self):




# 입력을 받아오는 부분
num_line = int(input())
parsed_code = []

for i in range(num_line):
    code = input()
    str_len = len(code)
    for j in range(str_len):
        ch = code[j]    # i번째 줄의 j번째 문자
        # 여기서부터는 직접 코딩