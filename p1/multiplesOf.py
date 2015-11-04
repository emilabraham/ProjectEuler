#Solution for problem 1

#Returns a set of numbers less than given number that are divisble by divisor
def multiplesOf(number, divisor):
    multiples = set()
    for x in range(1, number):
        #If divisible by divisor, then add it to the set
        if x % divisor == 0:
            multiples.add(x)

    return multiples

#Sets for multiples of 5 and 3 less than 1000
set1 =  multiplesOf(1000,5)
set2 =  multiplesOf(1000,3)

#A combination of these sets without duplicates
set1.update(set2)
print sum(set1)
