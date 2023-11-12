import numpy as np

def rowInterchange(A, i, j):
    A[[i, j]] = A[[j, i]]

def rowScaling(A, k, i):
    A[i] = k*A[i]

def rowReplacement(A, k, i, j):
    A[j] += k*A[i]

def makeAllBelowPivotZero(A, ip, jp): #pivot == 1
    n, m = A.shape
    for i in range(ip + 1, n):
        rowReplacement(A, -A[i][jp], ip, i)

def makeAllAbovePivotZero(A, ip, jp): #pivot == 1
    n, m = A.shape
    for i in range(ip - 1, -1, -1):
        rowReplacement(A, -A[i][jp], ip, i)

def makeEchelonForm(A):
    n, m = A.shape
    npivot = 0
    for j in range(m):
        for i in range(npivot, n):
            if A[i][j] != 0:
                rowInterchange(A, npivot, i)
                rowScaling(A, 1/A[npivot][j], npivot)
                makeAllBelowPivotZero(A, npivot, j)
                npivot += 1
                break

def makeReducedEchelonForm(A):
    makeEchelonForm(A)
    n, m = A.shape
    for i in range(n - 1, -1, -1):
        for j in range(0, m):
            if A[i][j] != 0:
                makeAllAbovePivotZero(A, i, j)
                break

def showArray(A):
    n, m = A.shape
    for i in range(n):
        tmp = ""
        for j in range(m):
            tmp += str(A[i][j]) + " "
        print(tmp)

def showEquationResult(A):
    results = np.zeros((m,))
    isfree = np.ones((m,))
    for i in range(n):
        res = 0
        for j in range(m):
            if A[i][j] != 0:
                for k in range(j+1, m-1):
                    res += -A[i][k]*10
                res += A[i][m-1]
                results[j+1] = res
                isfree[j+1] = 0
                break
    for i in range(1, m):
        if isfree[i] == 1:
            print("X" + str(i) + " = 10")
        else:
            print("X" + str(i) + " = " + str(results[i]))

inp = input()
n = int(inp.split(' ')[0])
m = int(inp.split(' ')[1])
A = np.zeros((n, m))
for i in range(n):
    inp = input()
    A[i] = inp.split(' ')

makeReducedEchelonForm(A)
showArray(A)
showEquationResult(A)