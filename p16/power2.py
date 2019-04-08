#Problem 16 from Project Euler
#https://projecteuler.net/problem=16

#Find the 2^1000
#Praise be modern computing power
x = 1
for i in range(1001):
    x = 2**i

#Sum the digits
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print sum_digits(x)
