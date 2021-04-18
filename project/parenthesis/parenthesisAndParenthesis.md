# (괄호)와 {괄호}와 [괄호]  
<br>

## Introduction
```
SyntaxError: invalid syntax
```
다들 익숙하시죠...? ㅎㅎ  
`SyntaxError`는 `괄호()`를 제대로 닫지 않거나, `세미콜론;`을 붙이지 않았을 때 경우에 만날 수 있는 에러예요.  
단어 그대로 `문법에 문제가 있다`는 뜻이죠.  
다행히 똑똑한 IDE는 안 닫힌 괄호가 있으면 알려줘요.  
그렇지만 IDE도 완벽하진 않아요.  

그래서 오늘은!  
`괄호 검사기`를 만들어서 직접 에러를 찾아볼 거예요.  
그럼 ㄱㄱ~
<br>
<br>

## Parenthesis Checker
`괄호 검사기`는 `()`와 `{}`, `[]`가 제대로 짝지어져 있는지 검사해요.  
검사는 주어진 파일에서 괄호만 순서대로 가져온 후 괄호를 검사하는 순서로 이루어지구요.  
괄호가 올바르게 짝지어져 있으면 `GOOD`을 프린트 해주지만,  
잘못 짝지어진 경우엔 `BAD`를 프린트 해줘요.  
예시를 살펴볼까요?  

1. 올바르게 짝지어진 괄호  
    `()`, `[]`, `{}`, `()[]`, `([])`, `({})[]`  
2. 잘못 짝지어진 괄호  
    `)`, `()[`, `(]`, `([]`, `(){})`

참고로 `테스트케이스`는 [여기](https://happyhddey.github.io/pythonSimpleProject/blob/main/project/parenthesis/index.html)에 있어요~
<br>
<br>

## Introduction to Stack
이 문제를 쉽게 푸는 방법이 있어요.  
바로 `Stack`이라는 자료구조를 활용하는 거예요.  

`Stack`은 list처럼 데이터를 저장할 수 있는 친구예요.  
데이터를 하나씩 넣고 꺼낼 수 있죠.  
그런데 데이터를 꺼낼 때는 가장 나중에 넣은 데이터를 먼저 꺼내야 해요.  
`LIFO(last in first out, 후입선출)`을 찾아보면 더 쉽게 이해가 될 거예요.  

쉽게 비유를 해볼까요?  
책상 위에 책을 쌓아두면 가장 나중에 올려둔 책이 가장 위에 있죠?  
가장 먼저 올려둔 책은 가장 아래에 있어서 위에 있는 책들을 다 치워야 볼 수 있구요.  
`Stack`이 이거랑 똑같은 경우에요.  
나중에 올려둔 책을 가장 먼저 볼 수 있는 거죠.  

여담이지만, `Stack`이라는 영어 단어가 '쌓는다'라는 뜻인 걸 생각해보면 참 잘 지은 이름인 것 같아요.  
<br>
<br>

## Implement Stack
그럼 `Stack`을 구현해서 사용해볼까요?  
기존 library가 있긴 하지만, 그래도 직접 구현해봐요.  
스켈레톤 코드는 [여기](https://github.com/happyhddey/pythonSimpleProject/blob/main/project/parenthesis/parenthesis.py)에~
```python
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
```
1. `isEmpty(self)`  
    list가 `비어있는지` 확인해요.  
    return은 boolean으로.  
2. `push(self, elem)`  
    list에 데이터를 `추가`해요.  
    `Stack`은 데이터를 하나씩 넣고 뺄 수 있다는 거 기억하죠?  
    return은 없습니다.  
3. `pop(self)`
    list에서 데이터를 빼요.  
    데이터를 `삭제`하는 거죠.  
    다시 한 번 말하지만, `Stack`은 데이터를 `하나씩만` 넣고 뺄 수 있어요.  
    당연히 여기서도 `하나만` 삭제해야 해요.  
4. `peek(self)`
    데이터 하나를 빼와요.  
    삭제하는 건 아니고, `가장 위에 있는 값`을 갖고 오는 거예요.  
    당연히 `하나만` 갖고 옵니다.  
<br>
<br>

## Level UP
지금 만든 `괄호 검사기`는 `잘못된 괄호`가 있을 때 단순하게 그걸 프린트 하죠?  
이번엔 좀 더 `user-friendly`한 괄호 검사기를 만들기 위해 `기능`을 하나 추가할 거예요.  
바로 `잘못된 괄호`의 `위치`까지 알려주는 거죠!  
한마디로 원래 코드에서 `잘못된 괄호`가 `몇번째 줄`의 `몇번째 문자`인지 알려주는 거예요.  
그럼 파이팅!^^
<br>
<br>
<br>
