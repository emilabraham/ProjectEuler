import math
#Find all the factors of a number
#Returns a list containing all of those factors
def factors(number):
    factorList = []
    #Only need to go to the sqrt of the number. The rest are redundant for this
    #problem because we only need to look at the number of divisors. The sqrt
    #Will give us half of the divisors.
    for i in range(1, int(math.ceil(math.sqrt(number)))):
        if number%i == 0:
            factorList.append(i)
    return factorList

#Returns the first triangle number to have over numDiv divisors
def triangleDivCount(numDiv):
    divisors = []
    #The triangle number
    triNum = 0
    #The index that will be added to triNum to create the new triangle number
    index = 1
    #Exit when you have more than numDiv divisors
    while(len(divisors)*2 < numDiv):
        triNum += index
        index += 1
        divisors = factors(triNum)

    return triNum
        

print triangleDivCount(500)
