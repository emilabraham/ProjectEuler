#Problem 5 from Project Euler
#http://projecteuler.net/problem=5

#Checks if the given number is divisible by every number under and including
#divisor.
def divisibleByUnder(number, divisor):
  if divisor == 1:
    return True
  elif number%divisor == 0:
    return True and divisibleByUnder(number, divisor - 1)
  else:
    return False

#Returns the first number that is divisble by every number under and including
#divisor.
def divisibleBy(divisor):
  answer = 10
  while not divisibleByUnder(answer, divisor):
      answer = answer + 10
  return answer

print divisibleBy(20)
