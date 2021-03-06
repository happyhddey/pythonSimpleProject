# 업다운 숫자게임
## Introduction
<br>

업다운 숫자게임은 컴퓨터가 고른 숫자를 맞추는 `숫자 추리 게임`입니다.  
설명하기 전에 예시부터 보고 갈까요?  
<br>
<br>
숫자 범위: 1~1000  
정답: 37  
<br>
첫번째 시도: 50  
`다운!`  
두번째 시도: 17  
`업!`  
세번째 시도: 37  
`정답!`
<br>
<br>
<br>
혹시 컴퓨터가 언제 `업!` `다운!` `정답` 을 외치는지 감이 오셨나요?  
<br>
깔끔하게 정리해보면,  
`업!` 은 정답보다 높은 숫자를 추리한 경우  
`다운!` 은 정답보다 낮은 숫자를 추리한 경우  
`정답!` 은 정답을 맞춘 경우  
를 말합니다.  
<br>
<br>
그럼 이제 업다운 숫자게임을 만들어 볼까요?  
<br>
<br>
<br>

## Description

### Level 1
1. `숫자 범위` 지정  
업다운 숫자게임에서 지원하는 숫자 범위는 1~1000 입니다.  
**"숫자를 추리하세요: "**  
범위를 벗어난 숫자를 입력한 경우,  
**"범위를 벗어난 숫자를 입력하였습니다. 다시 입력하세요: "**  
라는 메시지를 띄우고, 입력을 다시 받습니다.

2. `카운트다운` 모드 / `무제한` 모드 선택  
`카운트다운` 모드는 추리 가능 횟수에 제한이 있습니다.  
`무제한` 모드는 추리 가능 횟수에 제한이 없습니다.  

3. `카운트다운` 모드 구현  
총 15번의 추리가 가능합니다.  
추리할 때마다 추리 결과와 남은 추리 가능 횟수를 알려줍니다.  
**"업! 앞으로 3번 남았습니다."**  
**"다운! 앞으로 1번 남았습니다."**  
**"정답! 답은 37이었습니다."**  

4. `무제한` 모드 구현  
추리 횟수에 제한이 없습니다.  
추리할 때마다 추리 결과와 현재 추리 횟수를 알려줍니다.  
**"업! 현재 5번째 시도입니다."**  
**"다운! 현재 8번째 시도입니다."**  
**"정답! 답은 37이었습니다."**  

5. `결과 기록`  
게임 결과가 지금까지 플레이한 기록 중 5위 안에 드는 경우,  
게임 결과를 기록할지 물어봅니다.  
**"3위를 달성했습니다! 결과를 기록할까요? Y/N: "**  
결과를 기록할 땐 오늘의 연도, 월, 일, 시간과 player의 이름을 입력받아 기록합니다.  
**"Player 이름을 입력하세요: "**  
**"2021년도 3월 6일 16시 28분, taeGo 3위 달성!"**  
<details><summary>HINT</summary>
"txt 파일 입출력" 을 참고합시다
</details>
<br>

6. `게임 종료`  
게임을 다시 한 번 더 진행할 건지, 게임을 종료할 건지 물어봅니다.  
**"게임을 다시 하시겠습니까? Y/N: "**
<br>

### Level 2

1. `1P`, `2P` 옵션 선택  
`1P`와 `2P` 중 하나를 선택합니다.  
1인용 게임을 원하는 경우 `1P`를, 2인용 게임을 원하는 경우 `2P` 를 선택하면 됩니다.  
**"1P와 2P 중 선택하세요. 1P/2P: "**  
입력이 잘못된 경우, 입력을 다시 받습니다.  

2. `1P` 모드 구현  
level 1의 구현과 같습니다.  

3. `2P` 모드 구현  
2명이 플레이가 가능합니다.  
`무제한 모드`로 진행됩니다.  
player 1 부터 먼저 시작하며, player 두 명이 번갈아가며 게임을 진행합니다.  
**"player 1 차례입니다. 숫자를 추리하세요: "**  
**"업! 다음 플레이어에게 턴이 넘어갑니다."**  
**"player 2 차례입니다. 숫자를 추리하세요: "**  
**"정답! The winner is player 2! 축하합니다!"**

4. `게임 종료`  
다시 한 번 게임을 플레이하는 경우, `1P`, `2P` 옵션 선택으로 넘어갑니다.  
<br>
<br>
<br>
