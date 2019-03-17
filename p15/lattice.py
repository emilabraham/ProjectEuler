#Problem 15 from Project Euler
#https://projecteuler.net/problem=15

#Thanks ronbrz for suggesting I try Pascal's Triangle

#Create a size x size array filled with 0's
def initializeLattice(size):
    baseLattice = [[0 for x in range(size+1)] for y in range(size+1)]
    return baseLattice

#Fill the edges of the lattice with 1's
def fillEdgesOfLattice(lattice):
    for y in range(len(lattice)):
        if y != 0:
            lattice[y][0] += 1

    for x in range(len(lattice[0])):
        if x != 0:
            lattice[0][x] += 1

    return lattice

#Fill the inner portion of the array.
#Which is just going to be the sum of the two adjacent corners
def fillInnerLattice(lattice):
    for y in range(1,len(lattice)):
        for x in range(1,len(lattice)):
            lattice[y][x] = lattice[y][x-1] + lattice[y-1][x]

    return lattice

print fillInnerLattice(fillEdgesOfLattice(initializeLattice(20)))
