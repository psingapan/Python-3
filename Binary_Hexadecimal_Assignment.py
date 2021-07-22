##Problem 1:Write python code to calculate the decimal value of the binary integer represented by the string
##“11110101”. Your code should show how this string is interpreted as a sum of powers of 2.

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)

if __name__ == '__main__':
    binaryToDecimal(11110101)

##Problem 2:Use a python utility function to do the conversion you did in Problem 1.

def BinaryToDec():
    s="11110101"
    for i in s:
        print(int(s, base=2))
BinaryToDec()

##Problem 3: Write python code to calculate the decimal value of the hexadecimal integer represented by the
##string “FF2E”. Your code should show how this string is interpreted as a sum of powers of 16. Hint:
##Start by creating a dictionary to show the decimal value of the hexadecimal digits 0 through F.

hex_dict = {"0": 0, "2": 2, "A": 41 ,"B": 42, "C": 43, "D": 44,"E": 45,"F": 46}
hex_input = "FF2E"

for i in hex_input:
    print(i, ord(i), hex(ord(i)))
print(int(hex_input, base = 16))

##Problem 4: Use a python utility function to do the conversion you did in Problem 3.
print(int("FF2E",base = 16))
