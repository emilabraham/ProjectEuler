#Takes a 3 digit numbers and outputs the english representation

ones = { 0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7:
        "sevin", 8: "eight", 9: "nine" }

tens = { 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7:
        "seventy", 8: "eighty", 9: "ninety" }

specialTens = { 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15:
        "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19:
        "nineteen" }

def convertToWord(number):
    stringRepresentation = str(number)
    print ones[number]

#number : string
# returns English representation of the hundreds place
def hundredsWord(number):
    if (int(number) > 100):
        return ones[int(number[0])] + " hundred"
    else:
        return ""

print hundredsWord("101")
print hundredsWord("099")
print hundredsWord("999")
