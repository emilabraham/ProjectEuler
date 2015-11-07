#Problem 9 from Project Euler
#http://projecteuler.net/problem=9

#Function that returns the product a*b*c that satisfies the following
#conditions:
# 1. a < b < c
# 2. a*a + b*b = c*c
# 3. a + b + c = 1000
def pythagorean():
  for a in xrange(1,333):
    for b in xrange(a+1, 499):
      for c in xrange(b+1, 997):
        if a + b + c == 1000 and a * a + b * b == c * c:
          answer = a * b * c
          print a
          print b
          print c
  return answer

print pythagorean()
