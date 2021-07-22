##Problem 1: You have a file “Crime and Punishment.txt” in this folder. Write a program to read the contents
##of the file line by line into a list called lines. In the reading loop, count the number of lines you
##read. Compare this with the length of the list you get from the len() function.

myfile=open("Crime and Punishment.txt","r")
readfile= myfile.read()

count= 0

for items in readfile:
    count = count + 1

print('Line Count:', count)


##Problem 2:Use the type() function to determine the type of items in the list.

type(readfile)
str

##Problem 3:Compute the average length of a line.

myfile=open("Crime and Punishment.txt","r")

readfile= myfile.read()

total=0
count= 0
for items in readfile:
    count = count + 1
    total = total + len(readfile)
avg_length = total/count
print(avg_length)

##Problem 4:Consider a word to be defined as any sequence of non-blank characters separated by whitespace.
##Create a list of all of the words in the file. Use the string method split(). Print out the first 100
##words in the list of words. Print the length of the list of words.

myfile=open("Crime and Punishment.txt","r")
words = []

for line in myfile:
    lwords = line.split()

    for word in lwords:
        words.append(word)

for i in range(100):
    print(words[i])

## Problem 5:Count the number of occurrences of the word “is” in the list of words. Be sure to allow for
##capitalization. What fraction of all the words is this?
count = 0
for item in words:
    if item.lower() == "and":
    count = count + 1
print("Number of and is:",count)