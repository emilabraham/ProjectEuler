#Problem 2 from Project Euler
#http://projecteuler.net/problem=2

#Function that computes and returns the nth term of the fibonacci sequence.
def fib(n):
  if n == 1:
    return 1
  elif n == 0:
    return 1
  else:
    return fib(n-1) + fib(n-2)

#Function that computes and returns the sum of the even values under 4000000
#in the Fibonacci sequence.
def evenFibSum():
  n = 2
  sum = 0
  while fib(n) < 4000000:
    sum = fib(n) + sum
    n = n + 3
  return sum

print evenFibSum()
