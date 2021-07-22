#
#
##
##Problem 1: Write a program to compute the sum of the squares of the integers beginning with 5 and ending
##with 9. Use a while loop.

def sum_of_squares(n):
    mynum=0
    while n<9:
        n=n+1
        if n>4:
            mynum=mynum + n**2
        print(mynum)

##Problem 2: Write another program to repeat the task of Problem 1 but do it with a for loop using range(10).
##Use coditional execution within the loop to control which integers are used.

def range_func(n):
    mynum= 0
    for n in range(10):
        if n >=5:
            mynum= mynum + n **2
        print(mynum,n)

##Problem 3:Repeat the task using a for loop as in Problem 2, but instead of conditional execution within the
##loop, do a little research on range() and set the arguments to do what you want.

def range_func(n):
    mynum= 0
    for n in range(5,1,9):
        if n >=5:
            mynum= mynum**2
    print(mynum,n)

##Problem 4: Modify the code in Problem 3 to skip the integer 7 using continue.

def range_func(n):
    for n in range(5,1,9):
        mynum= n**2
        if n==7:
            continue
    print(mynum,n)

##Problem 5
##Modify the code from Problem 3 in two ways:
##1. Set the end argument of range to 100.
##2. Use break to avoid going beyond 9.

def range_func(n):
    for n in range(5,1,100):
        mynum= n**2
        if n==7:
            continue
    print(mynum,n)


def range_func2(n):
    for n in range(5,1,100):
        mynum= n**2
        if n>9:
            break
        print(mynum,n)