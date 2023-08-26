from array import *

num = int( input( "Enter a positive number: " ) )
arr = []
def displaytbl(num, arr): 
    x = 1   
    for r in range(num):
        row = []
        for c in range(num):
            row.append(x)
            x += 1 
        arr.append(row)
    
    for r in range(num):
        for c in range(num):
            print( arr[r][c], end = " ")
        print()

def sumrow(num, arr):
    print("Sum of row: ")
    for r in range(num):
        sum = 0
        for c in range(num):
            sum += arr[r][c]
        print(sum, end = " ")
    print()     

def sumcol(num, arr):
    print("Sum of col: ")
    for r in range(num):
        sum = 0
        for c in range(num):
            sum += arr[c][r]
        print(sum, end = " ")
    print()

def sumdia(num, arr):
    print("Sum of dia: ")
    for r in range(num):
        x = r
        sum = 0
        for c in range(num):
            sum += arr[x][c]
            x += 1
            if (x == num ):
                x = 0
        print(sum, end = " ")
    print()

displaytbl(num, arr)
sumrow(num, arr)
sumcol(num, arr)
sumdia(num, arr)