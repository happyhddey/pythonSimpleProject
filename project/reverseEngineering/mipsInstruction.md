# REVERSE ENGINEERING

## Introduction
`PYTHON`이나 `c++` 코드는 어떻게 실행될까요?  
이런 언어들은 먼저 `assembly(어셈블리)` 코드로 번연된 이후,  
`compile`이라는 단계를 거쳐서 `기계어(binary) 코드`로 번역됩니다.  
그러면 컴퓨터는 그 `기계어 코드`를 실행하는 거죠!  
`assembly` 언어는 `Reverse Engineering`에 필수적이예요.  
그럼 이번 시간엔 python으로 흉내낸 `MIPS Insturction` 어셈블리 명령어를 살펴봅시다!  
<br>
<br>
<br>

## MIPS INSTRUCTION
`assembly` 언어는 `register(레지스터)`라는 저장 공간을 활용해요.  
`register`는 `CPU`가 사용하는 저장 공간이에요.  
누구보다 빠르게 접근할 수 있는 저장 공간인 거죠.  
여기서 꼭 알아야 할 점은, `register 하나`에 `변수 하나`가 저장된다는 거예요.  
참고로 `register`는 `0~19`번까지 총 20개가 있어요.  

```python
# ADD : 레지스터 값끼리 덧셈
# rd번째 register에
# rs번째 register의 값에 rt번째 register 값을 더한 값을 저장
def add(rd, rs, rt):
    register[rd] = register[rs] + register[rt]

# SUB : 레지스터 값끼리 뺄셈
# rd번째 register에
# rs번째 register의 값에 rt번째 register 값을 뺀 값을 저장
def sub(rd, rs, rt):
    register[rd] = register[rs] - register[rt]

# MULT : 레지스터 값끼리 곱셈
# rd번째 register에
# rs번째 register의 값에 rt번째 register 값을 곱한 값을 저장
def mult(rd, rs, rt):
    register[rd] = register[rs] * register[rt]

# ADDI : 레지스터 값에 상수 덧셈
# rd번째 register에
# rs번째 register의 값과 imm라는 상수를 더한 값을 저장
def addi(rd, rs, imm):
    register[rd] = register[rs] + imm

# SUBI : 레지스터 값에 상수 뺄셈
# rd번째 register에
# rs번째 register의 값과 imm라는 상수를 뺀 값을 더한 값을 저장
def subi(rd, rs, imm):
    register[rd] = register[rs] - imm

# SLL : 레지스터 값을 shift left logical
# rd번째 register에
# rs번째 register의 값에 2^sa를 곱한 값을 저장
def sll(rd, rt, sa):
    register[rd] = register[rt] << sa

# SRL : 레지스터 값을 shift right logical
# rd번째 register에
# rs번째 register의 값에 2^sa를 나눈 값을 저장
def srl(rd, rt, sa):
    register[rd] = register[rt] >> sa
```
<br>
<br>
<br>

## EXERCISE SUMMARY  
<br>

- EXERCISE 0  
    `MIPS Instruction`을 이용해서 간단한 코드를 짜봅시다!  
<br>

- EXERCISE 1  
    ```python
    addi(9, 0, 9)
    sll(10, 9, 2)
    add(10, 10, 9)
    ```
    `곱셈`과 `덧셈`이 섞여 있어요.  
    간단하게 식으로 나타내볼까요?  
<br>

- EXERCISE 2  
    간단한 `수열`이에요.  
    아마 `등차수열`?  
<br>

- EXERCISE 3  
    얘도 간단한 `수열`이에요.  
    `규칙`을 찾아볼까요?  
<br>

- EXERCISE 4  
    얘도.. 간단한 `수열`이에요.  
    `규칙`을 찾아봅시다.  
<br>

- EXERCISE 5  
    `Fibonacci 수열`을 계산하는 코드를 써봅시다.  
    생각보다 간단해요.  
<br>

- EXERCISE 6  
    수열을 코딩해서 선생님께 보여줍시다.  
    선생님을 `시험`해보세요!    
<br>
<br>
<br>
