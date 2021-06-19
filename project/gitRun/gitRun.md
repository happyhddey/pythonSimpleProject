# Git Run

## Introduction
Github을 온라인 백업 서비스로만 알고 있는 당신!  
사실 Github은 `version 관리 사이트` 중 하나입니다.  
<br>
정확히는 `git`이 `version 관리 프로그램`이고,  
Github은 `git`을 이용해서 코드를 올릴 수 있는 사이트죠!  
<br>
아무튼 `git`을 사용하면

1. 코드를 `추가`하거나
2. 코드를 `변경`하거나
3. 코드를 `삭제`했을 때  

어떤 부분이 어떻게 변했는지 쉽게 눈으로 확인할 수 있어요.  
<br>
<br>

## Git 설치
그럼 먼저 `git`을 설치해야겠죠?  
설치법은 아래를 참고합니다.  

<details><summary>설치법</summary>
"git 설치" 를 구글링ㅎㅎ
</details>  

<br>

그럼 다들 `git` 설치하셨죠?  
이제 `branch`에 대해 알아봅시다.  
<br>
<br>

## Git Branch
`git`을 사용할 땐 `branch`라는 개념이 중요해요.  
기존 코드를 수정하고 싶을 때 새로운 branch를 만들면 알아서 원래 코드가 복사돼요.  
그 후에 원래 코드에 수정한 걸 합칠 수도 있구요.  
말 그래도 `가지치기`라고 생각하면 됩니다.  
자세한 건 직접 해보면서 알아봅시다~  
<br>
<br>

## Git Commands

### 초기 설정
`git`은 코드를 `폴더` 단위로 관리합니다.  
그래서 `git`에 올리고 싶은 폴더가 있다면,

1. 해당 폴더에서 `git` 초기 설정
    ```
    $ git init
    ```
2. 사용자 정보 입력
    ```
    $ git config --global user.name "happyhddey"
    & git config --global user.email "hyejinkim99@unist.ac.kr"
    ```
    이렇게 입력해두면(`--global`을 사용하면) 이후에 `config`를 설정해주지 않아도 돼요.  
    만약 특정 폴더에서만 사용자 정보를 다르게 하고 싶다면 `--global`을 빼고 똑같이 입력합니다.  

이렇게 초기 설정을 해둔 후엔 폴더 내의 파일을 수정할 경우 `수정 사항`이 모두 추적(!)됩니다.  

### Remote에서 파일 받아오고 수정
그럼 이제 `git`에서 파일을 들고 옵시다.  
1. 폴더 받아오기
    ```
    & git clone https://github.com/username/repo.git
    ```
    이때 기본적으로 `main` 브랜치를 받아옵니다.  
2. 업데이트 받아오기
    ```
    & git pull origin main
    ```
    만약 `main` 말고 다른 브랜치에서 받아온다면?
    ```
    & git pull origin branchName
    ```
    
### 코드 수정하고 올리기
1. 수정 사항 확인
    ```
    & git status
    ```
2. `git`에 올릴 파일 선택
    ```
    & git add fileName
    ```
    만약 폴더를 올리고 싶다면?
    ```
    & git add directoryName
    ```
    만약 수정한 걸 모두 올리고 싶다면?
    ```
    & git add .
    ```
3. 수정 사항 올리기 전에 설명(`commit message`) 쓰기
    ```
    & git commit -m "message"
    ```
4. 올리기...!  
    주의해야 할 점은 `push`하기 전에 항상 `pull`을 먼저 해야한다는 것!!!
    ```
    & git push origin main
    ```
    다른 브랜치에 올리고 싶다면?  
    ```
    & git push origin branchName
    ```

### 심화편: branch 사용하기
`branch`를 만드는 건 복사본을 만드는 거랑 같다고 했죠?  
그래서 branch를 옮기는 건 복사본에서 작업하겠단 얘기입니다~  
그럼 `branch`를 사용해봅시다!  
1. 브랜치 만들기.. 전에 목록 확인
    ```
    & git branch
    ```
2. 만들기
    ```
    & git branch branchName
    ```
    다만 여기서 만든 `branch`는 Github에 만들어지는 게 아니라 `local(개인 컴퓨터)`에서만 만들어집니다.  
    알아서 동기화가 안 돼요.  
3. 다른 브랜치로 이동하고 싶다면  
    ```
    & git checkout branchName
    ```
4. 만들면서 이동하고 싶다면
    ```
    & git checkout -b branchName
    ```

그 외에는 다 동일해요.  
추가적으로

5. 만약 branch 내용을 Github에 올리고 싶다면,
    ```
    $ git push --set-upstream origin localBranchName
    ```
6. Github에서 `main`말고 다른 `branch`만 들고오고 싶다면?  
    ```
    & git clone -b branchName --single-branch http://github.com/userName/directory.git
    ```

<br>
<br>

## Pull Request
`풀리퀘`라고 불리는 `Pull Request`는 `branch`를 합치는 작업이랍니다.  
알아서 어떤 부분이 바뀌었는지 알려줘서 엄청 편하죠.  
그리고 `풀리퀘`는 Github 페이지에서 합시다!  

<br>
<br>

## 그럼 연습해봅시다
간단하게 연습해볼까요?  
1. [여기](https://github.com/happyhddey/starPattern)로 가서 repository를 받아오고
2. 새로운 branch를 만듭니다.
3. 그 후에 백준 별찍기 1번 파일을 추가하고  
4. README.md의 `contributor`에 이름을 추가합니다.  
5. 만든 branch를 repository에 올리고  
6. 풀리퀘까지~  
