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
