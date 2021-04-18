# Bulls and Cows

## Introduction
제목은 `숫자야구`로 하겠습니다.  
근데 이제 `class`를 곁들인...    
<br>



## What is the 숫자야구?
`숫자 야구` 게임은 숫자를 때려맞추는 게임이에요.  
숫자를 추측할 때마다 추측 결과를 알려주는 게 특징이죠.  
<br>



## Strike and Ball
그럼 추측 결과를 어떻게 알려주느냐?  
`S(strike)`와 `B(ball)`로 알려줍니다.  
`S`는 `숫자`랑 `자리`를 둘 다 맞춘 경우를 뜻하고,  
`B`는 `숫자`는 맞췄지만 `자리`는 틀린 경우를 뜻해요.  

<details><summary>EXAMPLE</summary>

`정답`: 486   
`추측`: 408   
첫번째 숫자인 `4`는 숫자도 맞고 자리도 맞으니까 `S`,  
두번째 숫자인 `0`은 숫자가 틀렸으니까 아무것도 아니고,  
세번째 숫자인 `8`은 숫자만 맞추고 자리는 틀렸으니까 `B`.  
결론적으로 `추측 결과`는 `1S1B`이 됩니다.  
</details>
<br>



## 함수로 구현
`클래스`로 구현하기 전에!  
일단 `함수`를 이용해서 한 번 구현해볼까요?  
skeleton code도 있다구요~  
코드는 [여기](https://github.com/happyhddey/pythonSimpleProject/blob/main/project/bullsAndCows/bullsAndCowsFunction.py)로~
```python
# 원하는 자리수를 입력하면 해당 자리수의 숫자를 랜덤하게 반환
def set_answer(size):

# 숫자 추리에 성공했는지 알려줌
def is_over(answer, guess):

# 제대로 된 입력이 들어왔는지 확인함
def is_right_input(size, my_answer):

# user에게서 입력을 받아옴
def set_guess(size):

# 추리 결과를 프린트 함
def print_score(answer, guess):

# main
size = 3
answer = set_answer(size)
attempt = 0
guess = ""

is_end = False
while not is_end:
    attempt += 1
    guess = set_guess(size)
    if is_over(answer, guess):
        print("NICE GUESS! THE ANSWER WAS %s" %answer)
        print("YOUR ATTEMPT: %d" %attempt)
        is_end = True
    else:
        print_score(answer, guess)
```
함수로 구현하는 건 어렵지 않죠?    
그런데 만약 `플레이어가 여러명`이 되면 어떻게 될까요?  
플레이어 수만큼 코드의 길이도 길어지겠죠?  
이럴 때 `클래스`를 사용한답니다.  
<br>

## 클래스로 구현
지금까지는 게임을 만들 때마다 필요한 변수를 모두 복붙해야 했죠?  
그런데 `클래스`를 사용하면 그럴 필요가 없어요.  
<br>

`클래스`는 `변수`랑 `함수`를 담고 있는 `패키지`라서,  
`클래스` 하나만 만들어도 그 안에 있는 `변수`랑 `함수`를 사용할 수 있어요.  
게임을 실행할 때 필요한 `변수`랑 `함수`를 `하나로 포장`해둔 거죠.  
무엇보다 박스 안에 있는 `변수`랑 `함수`를 필요할 때마다 꺼내쓸 수 있어서 편해요.  
박스 하나당 플레이어 한 명이니까 구분하기도 편하구요.  
코드는 [여기](https://github.com/happyhddey/pythonSimpleProject/blob/main/project/bullsAndCows/bullsAndCowsClass.py)로~
```python
class BaseballGame():

    # member variables
    def __init__(self, size):
        self.size = size
        self.answer = ""
        self.guess = ""
        self.attempt = 0

    # member methods
    def is_right_input(self, my_answer):

    def set_guess(self):

    def print_score(self):

    def is_over(self):

    def turn(self):
```
그럼 앞에서 만들었던 함수를 변형하여 이 skeleton code를 채워봅시다.  
보면 알 수 있듯, 클래스에는 `member variable`과 `member method`가 있어요.  
`variable`은 말그대로 `변수`이고,  
`method`는 클래스가 갖고 있는 `함수`예요.  
아, 클래스 안에 `변수`랑 `함수`를 사용할 때, `self`를 잊지 마세요!  
항상 사용할 때 `self.` 이걸 앞에 붙여줘야 해요.  

<br>
참고로 저 클래스는 이렇게 쓴답니다.  

```python
size = 3
game = BaseballGame(size)
while not game.is_over():
    game.turn()
```
<br>

## 클래스를 쓰면 너무 좋은 상황
클래스를 쓰면 `이럴 떄` 정말 좋아요.  
어떨 때냐구요?  
아래의 예시를 봅시다.  
```python
playerList = {}
defaultSize = 3

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
```
이 코드에선 먼저 플레이어 이름을 입력받아요.  
만약 `등록된 플레이어가 아니`라면, 플레이어를 등록하고 새로운 게임을 시작합니다.  
`등록된 플레이어`라면 기존 게임을 이어서 하구요.  
게임이 끝나면 해당 플레이어는 목록에서 삭제합니다.  
이렇게 하면 여러 플레이어가 동시에 게임을 할 수 있죠!  
다들 이래서 클래스를 쓰나봅니다ㅎㅎ  
<br>
<br>
<br>
