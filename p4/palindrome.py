#Problem 4 from Project Euler
#http://projecteuler.net/problem=4

#Returns a list of all of the palindromes as a result of the product of 2,
#3-digit numbers.
def palindrome():
  answer = []
  for i in xrange(100, 1000):
    for j in xrange(100, 1000):
      x = i * j
      y = str(x)
      y = y[::-1]
      w = int(y)
      z = i * j
      if w == z:
        answer.append(w)
  return answer
print max(palindrome())
