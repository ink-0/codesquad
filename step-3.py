#링크 참조
# https://cube3x3.com/%ED%81%90%EB%B8%8C%EB%A5%BC-%EB%A7%9E%EC%B6%94%EB%8A%94-%EB%B0%A9/#notation
# https://rubiks-cube-solver.com/



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
def rot(t):
    #F회전
    if t=="F":
       temp1,temp2,temp3= U[2][0],U[2][1],U[2][2]
       U[2][0], U[2][1], U[2][2]=L[0][2], L[1][2], L[2][2]
       L[0][2], L[1][2], L[2][2]=D[0][0], D[0][1], D[0][2]
       D[0][0], D[0][1], D[0][2]=R[0][0], R[1][0], R[2][0]
       R[0][0], R[1][0], R[2][0]=temp1,temp2,temp3

       temp1 = F[0][0]
       F[0][0],F[2][0],F[2][2],F[0][2]=F[2][0],F[2][2],F[0][2],temp1

       temp2 = F[0][1]
       F[0][1],F[1][0],F[2][1],F[1][2] = F[1][0],F[2][1],F[1][2],temp2
    elif t=="F'":
        temp1,temp2,temp3= U[2][0],U[2][1],U[2][2]
        U[2][0], U[2][1], U[2][2]=R[0][0], R[1][0], R[2][0]
        R[0][0], R[1][0], R[2][0]=D[0][2], D[0][1], D[0][0]
        D[0][2], D[0][1], D[0][0]=L[0][2], L[1][2], L[2][2]
        L[0][2], L[1][2], L[2][2]=temp3,temp2,temp1

        temp1 = F[0][0]
        F[0][0] = F[0][2]
        F[0][2] = F[2][2]
        F[2][2] = F[2][0]
        F[2][0] = temp1
        temp1 = F[0][1]
        F[0][1] = F[1][2]
        F[1][2] = F[2][1]
        F[2][1] = F[1][0]
        F[1][0] = temp1

