#Problem 7 from Project Eulter
#http://projecteuler.net/problem=7
import math

def nthPrime(n):
  answer = [2]
  j = 3
  while len(answer) < 10002:
    if isPrime(j):
      answer.append(j)
      j = j + 2
    else:
      j = j + 2
  return answer[n-1]

#Abstracts a level to avoid the divisor parameter.
#Determines if a number is prime.
def isPrime(number):
  return isPrimeHelper(number, 2)

#Recursive function that calculates if given number is divisble by any number
#under it  > 0
def isPrimeHelper(number, divisor):
  y = math.trunc(math.sqrt(number))
  if divisor <= y:
    if number%divisor == 0:
      return False
    else:
      return True and isPrimeHelper(number, divisor + 1)
  else:
    return True

print nthPrime(10001)
