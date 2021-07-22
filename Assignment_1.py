#
##
##Assignment 1: Write a fruitful python function which computes and returns a letter grade based on a percentage
##grade. The percentage grade is the single parameter of this function and should be a number
##between 0 and 100. Your function should return an error message if the value of the argument
##is not within this range. The assignment of the letter grade should be based on the table in the
##syllabus of this course.

##Note that this problem set involves both conditional execution and functions.

##Problem 1:Put the code to define your function in the following cell.

def test_scores(score):
    if 90 <= score <= 100:
        grade='A'
    elif 80 <= score <= 89:
        grade='B'
    elif 70 <= score <= 79:
        grade='C'
    elif 60 <= score <= 69:
        grade='D'
    elif 0 <= score <= 59:
        grade='F'
    else:
        print("Error, not an acceptable range!") 
        


##Problem 2: Tests
##Test your function with the following values:
##• 0
##• 72
##• 91
##• 110

test_scores(0)
test_scores(72)
test_scores(91)
test_scores(110)

## Problem 3: The Void Version
##Revise your function so that it is void and provides its result by printing.

def test_scores(score):
    if 90 <= score <= 100:
        grade='A'
    elif 80 <= score <= 89:
        grade='B'
    elif 70 <= score <= 79:
        grade='C'
    elif 60 <= score <= 69:
        grade='D'
    elif 0 <= score <= 59:
        grade='F'
    else:
        print("Error, not an acceptable range!") 

##Problem 4: Test the Void Version
##Test your void function with the values provided above. Create as many new code cells as you
##need.

test_scores(0)
test_scores(72)
test_scores(91)
test_scores(110)
