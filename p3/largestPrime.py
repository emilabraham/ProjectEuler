#Problem 3 from Project Euler
#http://projecteuler.net/problem=3

import math
import sys
#Had to set the recursion limit higher. Default is 1000, I believe.
#I don't think Python is very good at recursion. Or I might be bad at it.
sys.setrecursionlimit(7000)

#Returns the largest prime number that is a factor of given number
def largestPrimeFactor(number): 
  y = math.trunc(math.sqrt(number))
  answer = 1
  for x in xrange(y):
    if number%(x+1) == 0 and isPrime(x+1):
      answer = x+1
  return answer
  
#Abstracts a level to avoid the divisor parameter.
#Determines if a number is prime.
def isPrime(number):
  return isPrimeHelper(number, 2)

#Recursive function that calculates if given number is divisble by any number
#under it  > 0
def isPrimeHelper(number, divisor):
  if divisor < number:
    if number%divisor == 0:
      return False
    else:
      return True and isPrimeHelper(number, divisor + 1)
  else:
    return True


print largestPrimeFactor(600851475143)
