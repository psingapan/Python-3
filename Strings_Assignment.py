##Problem 1:Assume that name is a variable of type String that has been assigned a value. Write an expression
##whose value is the first character of the value of name. So if the value of name were “Jones” the
##expression’s value would be ‘J’.
myname="Pirin"
my_name=myname[0]
print(my_name)

##Problem 2: Write an expression whose value is the last character in the string associated with name. Remember
##how to index a string from the right instead of the left.
myname="Pirin"
print(myname[4])

##Problem 3:Write an expression whose value is the string that consists of the first four characters of the string
##associated with s. Set s = “abcdef” and test your expression.
s="abcdef"
print(s[0:4])

##Problem 4:Given that s refers to a string, write an expression that evaluates to a string that is a substring
##of s and that consists of all the characters of s from its start through its fifth character. Set s =
##“abcdef” and test your expression.

s="abcdef"
s[0:5]

##Problem 5: Write an expression that results in a String consisting of the second through fourth characters of
##the String s. Set s = “abcdef” and test your expression.

seconds= s[1:5]
print(seconds)

##Problem 6:Write an expression that evaluates to True if the str associated with s starts with “p”. Test your
##expression with two different strings. In test 1, s = “parameter”. In test 2, s = ‘Parameter’.
def true_string(s):
    result= s.startswith('p') and s.islower()
    return result
true_string("Param")

true_string("param")


##Problem 7:Write an expression that returns True if the str associated with s ends with “ism”. Test your
##expression with two different strings. In test 1, s = “capitalism”. In test 2, s = ‘religion’.
def ends_with(s):
    result= s.endswith('ism')
    return result

ends_with("capitalism")
ends_with('religion')

##Problem 8: Given a variable s associated with a str, write an expression whose value is a str that is identical
##except that all the letters in it are upper-case. Thus, if the str associated with s were “Saint
##Martin”, the value of the expression would be “SAINT MARTIN”.
def identical(s):
    result= s.upper()
print(result)

identical("hello")

##Problem 9: Write a sequence of statements that finds the first comma in the string associated with the variable
##s, and associates the variable first with the portion of s up to, but not including the comma. Test
##your statements with s = “Hello, world”.

def first_comma(s):
    result= s.find(","[0:])
print (result)
first_comma("Hello")

## Problem 10:Write an expression whose value is the arithmetic sum of the int associated with x, and the all-digit
##str associated with s. Test your expression with x = 10 and s = “5”.
def arith_sum(x,s):
    int_x=int(x)
    int_s=int(s)
    
sum_together= int_x + int_s
print(sum_together)

arith_sum(10,'5')