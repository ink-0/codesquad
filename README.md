# codesquad 2021 마스터즈 코스 테스트
## [STEP-1] 단어 밀어내기
### 문제 설명
1. 입력: 사용자로부터 단어 하나, 정수 숫자 하나( -100 <= N < 100) , L 또는 R을 입력받는다. L 또는 R은 대소문자 모두 입력 가능하다.
2. 주어진 단어를 L이면 주어진 숫자 갯수만큼 왼쪽으로, R이면 오른쪽으로 밀어낸다.
3. 밀려나간 단어는 반대쪽으로 채워진다.

### 코드풀이
* 단어, 정수, 방향을 구분하여 입력
``` python
word,cnt,type=map(str,input("영단어,정수,방향 공백 구분하여 입력:").split())
```

* 문장 길이로 나눠 최소 연산 구현
``` python
wordlen=len(word)
turn=abs(cnt)%wordlen
``` 

* 오른쪽,왼쪽 밀어내기 구현
``` python
word.append(word.pop()) #오른쪽
word.append(word.pop(0)) #왼쪽
``` 

## [STEP-2] 평면 큐브 구현하기
### 문제설명
* 3 X 3의 2차원 배열에 사용자의 입력을 받아 동작하는 프로그램 구현
 ```python
R R W  
G C W  
G B B  
 ```

- U  가장 윗줄을 왼쪽으로 한 칸 밀기 RRW -> RWR
- U' 가장 윗줄을 오른쪽으로 한 칸 밀기 RRW -> WRR
- R  가장 오른쪽 줄을 위로 한 칸 밀기 WWB -> WBW
- R' 가장 오른쪽 줄을 아래로 한 칸 밀기 WWB -> BWW
- L  가장 왼쪽 줄을 아래로 한 칸 밀기 RGG -> GRG (L의 경우 R과 방향이 반대임을 주의한다.)
- L' 가장 왼쪽 줄을 위로 한 칸 밀기 RGG -> GGR
- B  가장 아랫줄을 오른쪽으로 한 칸 밀기 GBB -> BGB (B의 경우도 U와 방향이 반대임을 주의한다.)
- B' 가장 아랫줄을 왼쪽으로 한 칸 밀기 GBB -> BBG
- Q  Bye~를 출력하고 프로그램을 종료한다.
 
 ### 코드 풀이
 * 각 기능별 함수 구현  (U,R,L,B)
 ``` python
 def U(cube,type):
    if type=='left':
        cube[0].append(cube[0].pop(0))
    elif type=='right':
        cube[0].insert(0,cube[0].pop())
    return cube
 ```
* CUBE 사용자로부터 입력
 ``` python
cube=[list(map(str,input('cube를 한줄씩 입력하시오(3x3):').split()))for i in range(3)]
inp=0
#초기 CUBE 출력
for i in cube:
    print(*i)
print()
 ```
* type을 생성하여 기본 & ' 구분
(left,right/up,down)
 ``` python
 if inp=="U":
    cube = U(cube, 'left')
 elif inp == "U'":
    cube = U(cube, 'right')

 elif inp == "R":
    cube = R(cube, 'up')
 elif inp == "R'":
    cube = R(cube, 'down')
 ```
* 명령어 & 결과 CUBE 출력
``` python
print(inp)
for i in cube:
  print(*i)
 ```

## [STEP-3] 루빅스 큐브 구현하기
### 문제 설명
+ 큐브는 W, B, G, Y, O, R의 6가지 색깔
+ 입력: 각 조작법을 한 줄로 입력받는다.
+ 출력: 큐브의 6면을 펼친 상태로 출력한다.
+ Q를 입력받으면 프로그램을 종료하고, 조작 받은 명령의 갯수를 출력시킨다.

* 큐브의 초기 상태 
``` python 
                B B B  
                B B B
                B B B

 W W W     O O O     G G G     Y Y Y 
 W W W     O O O     G G G     Y Y Y 
 W W W     O O O     G G G     Y Y Y 
 
                R R R 
                R R R 
                R R R 
 ```
### 코드풀이
* CUBE 출력함수  
tab으로 구분하여 출력
``` python 
def prt():
    for i in U:
        print("\t\t\t ",end="")
        print(*i)
    print()
    print(*L[0],"\t\t",*F[0],"\t\t",*R[0],"\t\t",*B[0])
    print(*L[1], "\t\t", *F[1], "\t\t", *R[1], "\t\t", *B[1])
    print(*L[2], "\t\t", *F[2], "\t\t", *R[2], "\t\t", *B[2])
    print()
    for i in D:
        print("\t\t\t ",end="")
        print(*i)
 ```

* rot(회전함수) 안에 각 기능 구현
``` python 
if t=="F":
#ULDR 자리 바꿈
   temp1,temp2,temp3= U[2][0],U[2][1],U[2][2]
   U[2][0], U[2][1], U[2][2]=L[2][2], L[1][2], L[0][2]
   L[0][2], L[1][2], L[2][2]=D[0][0], D[0][1], D[0][2]
   D[0][0], D[0][1], D[0][2]=R[2][0], R[1][0], R[0][0]
   R[0][0], R[1][0], R[2][0]=temp1,temp2,temp3
#F 자리 바꿈
   temp1 = F[0][0]
   F[0][0],F[2][0],F[2][2],F[0][2]=F[2][0],F[2][2],F[0][2],temp1
   temp2 = F[0][1]
   F[0][1],F[1][0],F[2][1],F[1][2] = F[1][0],F[2][1],F[1][2],temp2
 ```
* 종료 기능 구현
경과시간 / 조작갯수/ 안내멘트 출력
``` python 
def q():
    print('---------CUBE 맞추기 종료---------')
    end = time.time()
    start_end = time.ctime(end - start)
    print('경과시간:', str(start_end)[14:19])
    print("조작갯수:", cnt)
    print('이용해주셔서 감사합니다. 뚜뚜뚜.')
    exit()
 ```

* [추가기능] -CUBE 셔플
'S'입력시 CUBE 셔플 및 작동 시간 초기화
``` python 
if inp == 'S':
    #조작개수 초기화
    cnt=0

    #컬러 리스트를 shuffle통해 섞어줌.
    color = ["O", "G", "R", "B", "W", "Y"]
    random.shuffle(color)

    c = color.pop()
    F = [[c] * 3 for _ in range(3)] 
    #... 중략 R,U,D,L,B 동일
 ```
  CUBE의 모든 동작 구현 RANDOM으로 24번 시행
``` python 
r = ["F", "F'", "B", "B'", "R", "R'", "L", "L'", "U", "U'", "D", "D'"]
            for _ in range(24):
                a = random.choice(r)
 ```
* rot(회전)함수 구현
각 회전 별 F,F',F2,F'2 구현
``` python
        if inp == 'F':
            rot('F')
            prt()
        if inp == 'F2':
            rot('F')
            rot('F')
            cnt+=1
            prt()

        if inp == "F'":
            rot("F'")
            prt()
        if inp == "F'2":
            rot("F'")
            rot("F'")
            cnt+=1
            prt()
 ```
* [추가기능] - CUBE 맞춤 시 자동 시행
``` python
        answer=True
        for k in [F,B,R,L,U,D]:
            for i in range(3):
                for j in range(3):
                    if k[i][j] != k[1][1]:
                        answer=False
                        break
        if answer==True:
            print("축하합니다! 모든 면을 다 맞추셨습니다.")
            q()
 ```