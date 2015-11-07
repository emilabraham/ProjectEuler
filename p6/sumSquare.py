#Problem 6 from Project Euler
#http://projecteuler.net/problem=6

#The sum of the squares of the numbers up to given number(inclusive)
def sumOfSquares(number):
  sum = 0
  while number != 0:
    sum = sum + number*number
    number = number - 1
  return sum

#The square of the sum of the numbers up to given number(inclusive)
def squareOfSum(number):
  square = 0
  while number != 0:
    square = square + number
    number = number - 1
  return square * square

print squareOfSum(100) - sumOfSquares(100)
