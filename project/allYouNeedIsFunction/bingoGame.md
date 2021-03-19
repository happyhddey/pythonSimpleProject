# All you need is FUNCTION

## Introduction
이번 프로젝트에서는 `3x3 빙고 게임`을 구현할 거예요~  
`빙고 게임` 규칙은 다들 아시죠?  
다행히 이번에는 `skeleton code`가 있어요!  
`skeleton code`는 '뼈대 코드'라고도 하는데,  
말 그대로 뼈대만 있기 때문에 빈 부분을 코딩해서 채워줘야 하죠ㅎㅎ  
다행히 이 `skeleton code` 자체는 건드릴 게 없어요.  
그럼 뭘 채워야 한다는 걸까요?  
일단 `skeleton code`를 봅시다.  
<br>
<br>
<br>

## Skeleton Code
이게 `빙고 게임`의 `skeleton code`예요.  
근데 `코드`라기 보다 `영어 문장` 같지 않나요?  
```PYTHON
# MAIN

startPlayer = 'x'

gameBoard = initializeBoard()
player = startPlayer
isEndOfGame = False

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
```
<br>
<br>
<br>

## Skeleton Code with Comments
잘 이해가 안 된다면, `주석`이 달린 코드를 한 번 읽어볼게요.  
```PYTHON
# MAIN

startPlayer = 'x'               # 선 플레이어를 지정합니다.

gameBoard = initializeBoard()   # 보드판을 초기화합니다.
player = startPlayer            # 플레이어 정보를 초기화합니다.
isEndOfGame = False             # '게임 종료 flag'를 초기화합니다.

while not isEndOfGame:                          # 게임이 끝날 때까지 루프를 반복합니다.
    printBoard(gameBoard)
    inputA, inputB = inputAB(player)            # 플레이어가 선택한 칸 정보(A, B)를 입력받습니다.
    
    if isRightRange(inputA, inputB):            # 제대로 된 A, B 값을 입력했는지 체크합니다.
        A, B = getABonBoard(inputA, inputB)     # 입력받은 A, B 값을 보드판 리스트의 인덱스로 바꿔줍니다.
        
        if isEmptyCell(gameBoard, A, B):        # 플레이어가 선택한 칸이 빈 칸인지 체크합니다.
            updateBoard(gameBoard, A, B, player)  # 플레이어가 선택한 칸을 채웁니다.
            
            if isBingo(gameBoard):              # 빙고가 있는지 체크합니다.
                printBoard(gameBoard)
                print("축하합니다!!! 승자는: %s 입니다." % player)
                isEndOfGame = True              # 게임을 끝내기 위해 '게임 종료 flag'를 바꿔줍니다.
            elif isFull(gameBoard):             # 보드판이 다 찼는지 체크합니다.
                printBoard(gameBoard)
                print("There is no empty cell. Please restart the game")
                isEndOfGame = True              # 게임을 끝내기 위해 '게임 종료 flag'를 바꿔줍니다.
            else:
                player = getNextPlayer(player)  # 플레이어를 바꿉니다.
        
        else:
            print("이미 채워진 칸입니다. 숫자를 다시 입력해주세요.")
    
    else:
        print("범위를 벗어난 숫자를 선택하였습니다. 숫자를 다시 입력해주세요.")
```
이제 게임이 어떻게 돌아가는지 알겠죠?  
이해가 되었다면 손을 들어서 선생님을 부를 것!!!  
잘 모르는 부분이 있어도 손을 들어서 선생님을 부를 것!!!  
<br>
<br>
<br>

## 그래서 오늘은...
사실 이 코드 자체는 건드릴 게 없답니다.  
아직 `구현되지 않은 함수`를 쓰고 있다는 게 문제일 뿐이에요.  
이 말은???  
`skeleton code`에 사용된 `함수`만 코딩해주면 된다는 것!!ㅎㅎ  
`skeleton code`는 [여기(https://github.com/happyhddey/pythonSimpleProject/blob/main/project/allYouNeedIsFunction/bingoGame.py)]에 있어요!  
<br>
<br>
<br>
<br>
<br>

# 구현할 함수 목록

## initializeBoard()
보드판을 초기화하는 함수입니다.  
`.`으로 채워진 이중 리스트 `gameBoard`를 return합니다.  
크기는 `3x3`입니다.  
<br>
<br>
<br>

## printBoard(gameBoard)
보드판을 출력합니다.  
이미 구현되어 있습니다!!!  
<br>
<br>
<br>

## inputAB(currentPlayer)
플레이어에게 `A`, `B` 두 개의 숫자를 입력받는 함수입니다.  
누구의 차례인지도 알려주세요.  
입력받은 숫자를 `int`로 바꾸어 return합니다.  
갑을 어떻게 return해야 할지 모르겠다면 `skeleton code`를 살펴보아요ㅎㅎ  
<br>
<br>
<br>

## isRightRange(A, B)
플레이어에게 입력받은 `A`와 `B`가 범위 내의 숫자인지 확인하는 함수입니다.   
어떤 값을 return해야 할까요?  
그리고 숫자 범위는 어떻게 되어야 할까요?  
<br>
<br>
<br>

## getABonBoard(A, B)
플레이어에게 입력받은 `A`, `B`를 보드판의 `index`로 바꾸어주는 함수입니다.  
변환된 `index`를 출력합니다.  
<br>
<br>
<br>

## isEmptyCell(gameBoard, A, B)
플레이어가 선택한 칸이 `비어있는지` 확인하는 함수입니다.  
어떤 값을 return해야 할까요?  
<br>
<br>
<br>

## updateBoard(gameBoard, A, B, mark) 
보드판을 `업데이트`하는 함수입니다.  
플레이어가 칸을 선택했으니 보드판을 `업데이트` 해주는 거죠.    
`mark`는 칸에 표시할 기호를 뜻합니다.  
`mark`가 어떤 건지 잘 모르겠다면, `skeleton code`를 살펴봐요.  
어떤 값을 `인자`로 넘겨주고 있나요?  
한 가지 더.  
이 함수에서는 어떤 값을 return해야 할까요?  
<br>
<br>
<br>

## getNextPlayer(player)
`다음 플레이어`를 함수입니다.  
어떤 값을 return해야 할까요?  
<br>
<br>
<br>

## isBingoInA(gameBoard)
`A` 줄에 `빙고`가 있는지 확인하는 함수입니다.  
어떤 값을 return해야 할까요?  
<br>
<br>
<br>

## isBingoInB(gameBoard)
`B` 줄에 `빙고`가 있는지 확인하는 함수입니다.  
어떤 값을 return해야 할까요?  
<br>
<br>
<br>

## isBingoInDiagonal(gameBoard)
`대각선`에 `빙고`가 있는지 확인하는 함수입니다.  
어떤 값을 return해야 할까요?  
<br>
<br>
<br>

## isBingo(gameBoard)
`보드판 전체`에 `빙고`가 있는지 확인하는 함수입니다.  
어떤 값을 return해야 할까요?  
아 참, `isBingoInA`, `isBingoInB`, `isBingoInDiagonal` 함수를 구현한 이유가 뭘까요?^^  
<br>
<br>
<br>


## isFull(gameBoard)
보드판이 `꽉 찼는지` 확인하는 함수입니다.  
보드판이 다 찬 경우에는 더 이상 게임을 진행할 수 없으니까요.  
어떤 값을 return해야 할까요?  
<br>
<br>
<br>
<br>
<br>


# Finally...
모든 함수를 구현했나요?  
이제 코드를 실행해봅시다.  
아마 문제없이 코드가 돌아갈 거예요.  
그렇지만 아직 하나가 남았어요.  
`모듈`을 배울 차례 거든요ㅎㅎㅎㅎ  
