# Very simple program, converter of hexidecimals, binaries, and numbers

def numToBin(numin):
    output = 0
    mod = 1
    while (numin > 0):
        output += mod * (numin % 2)
        numin = numin//2
        mod = mod * 10
    return output


def binToNum(numin):
    output = 0
    mod = 1
    while (numin > 0):
        output = output + mod * (numin % 10)
        numin = numin // 10
        mod = mod * 2
    return output


def hexToNum(numin):
    output = 0
    for i in numin:
        output = output * 16
        if (i.isnumeric()):
            output = output + int(i)
        else:
            if ((ord(i) < ord('a')) or (ord(i) > ord('f'))):
                return "Invalid Input"
            output = output + (10 + ord(i) - ord('a'))

    return output


def numToHex(numin):
    output = ""
    while (numin > 0):
        temp = numin % 16
        if (temp < 10):
            output = str(temp) + output
        else:
            output = str(chr(ord('a') + int(temp)-10)) + output
        numin = numin//16
    return output


print("1 for Hex to num\n2 for num to hex\n3 for num to bin\n4 for bin to num\n5 for quit")
option = int(input())
print("please give value to convert:   ", end='')
while (option != 5):
    if (option == 1):
        numin = input()
        print("your output = ", hexToNum(numin))
    if (option == 2):
        numin = int(input())
        print("your output = ", numToHex(numin))
    if (option == 3):
        numin = int(input())
        print("your output =  ", numToBin(numin))
    if (option == 4):
        numin = int(input())
        print("The binary to numerical conversion is equal to: ",
              binToNum(numin), end='')
