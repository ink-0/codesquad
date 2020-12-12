#U,B,R,F 함수 정의
def U(cube,type):
    if type=='left':
        cube[0].append(cube[0].pop(0))
    elif type=='right':
        cube[0].insert(0,cube[0].pop())
    return cube

def B(cube,type):
    if type=='left':
        cube[2].append(cube[2].pop(0))
    elif type=='right':
        cube[2].insert(0,cube[2].pop())
    return cube
def R(cube,type):
    if type=='up':
        temp=cube[0][2]
        cube[0][2]=cube[1][2]
        cube[1][2]=cube[2][2]
        cube[2][2]=temp
    elif type=='down':
        temp=cube[2][2]
        cube[2][2]=cube[1][2]
        cube[1][2]=cube[0][2]
        cube[0][2]=temp
    return cube
def L(cube,type):
    if type=='up':
        temp=cube[0][0]
        cube[0][0]=cube[1][0]
        cube[1][0]=cube[2][0]
        cube[2][0]=temp
    elif type=='down':
        temp=cube[2][2]
        cube[2][0]=cube[1][0]
        cube[1][0]=cube[0][0]
        cube[0][0]=temp
    return cube


#CUBE 입력
cube=[list(map(str,input('cube를 한줄씩 입력하시오(3x3):').split()))for i in range(3)]
inp=0


#'Q'입력 전까지 계속 명령어 입력
while inp != 'Q':
    cmd=list(map(str,input('CUBE>'))) #CUBE 입력받음
    #cmd(명령어)상의 '처리
    while "'" in cmd:
        if "'" in cmd:
            cmd[cmd.index("'") - 1] += "'"
            cmd.pop(cmd.index("'"))

    #명령어 하나씩 처리
    for i in range(len(cmd)):
        inp=cmd.pop(0)
        if inp=="U":
            cube = U(cube, 'left')
        elif inp == "U'":
            cube = U(cube, 'right')

        elif inp == "B":
            cube = B(cube, 'right')
        elif inp == "B'":
            cube = B(cube, 'left')

        elif inp == "R":
            cube = R(cube, 'up')
        elif inp == "R'":
            cube = R(cube, 'down')

        elif inp == "L":
            cube = L(cube, 'down')
        elif inp == "L'":
            cube = L(cube, 'up')

        elif inp == "Q":
            print('Bye~')
            exit()

        print(inp)
        for i in cube:
            print(*i)
        print()

