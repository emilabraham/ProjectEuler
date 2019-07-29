#Takes a 3 digit numbers and outputs the english representation

ones = { 0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7:
        "seven", 8: "eight", 9: "nine" }

tens = { 0: "", 1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7:
        "seventy", 8: "eighty", 9: "ninety" }

specialTens = { 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15:
        "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19:
        "nineteen" }

def loop():
    conglomerate = ""
    for i in range(1,1000):
        conglomerate += convertToWord(str(i))
    return len(conglomerate + "onethousand")

def convertToWord(number):
    return hundredsWord(number) + tensWord(number)

#number : string
# returns English representation of the hundreds place
def hundredsWord(number):
    if (int(number) > 100):
        return ones[int(number[0])] + "hundred"
    else:
        return ""

#number : stirng
# returns English representation of the tens and ones place
def tensWord(number):
    if(len(number) == 2):
        return tensWord("0"+number)
    if(len(number) == 1):
        return tensWord("00"+number)

    if(int(number[1:]) > 10 and int(number[1:]) < 20):
        if(int(number[0]) >= 1):
            return "and" + specialTens[int(number[1:])]
        else:
            return specialTens[int(number[1:])]
    elif(int(number[1:]) == 0):
        return ""
    else:
        if(int(number[0]) >= 1):
            return "and"+tens[int(number[1])] + ones[int(number[2])]
        else:
            return tens[int(number[1])] + ones[int(number[2])]

print loop()
