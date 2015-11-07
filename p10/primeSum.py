#Problem 10 from Project Euler
#http://projecteuler.net/problem=10
import math
import sys
#Had to set the recursion higher otherwise the maxmum would be reached.
#Efficiency was not attempted, although it will be in the future.
sys.setrecursionlimit(7000)

#Function that returns the sum of the prime numbers under 2000000
def primeSum():
  answer = []
  for x in xrange(2, 2000000):
    if isPrime(x):
      answer.append(x)
  #print answer
  return sum(answer)

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

print primeSum()
