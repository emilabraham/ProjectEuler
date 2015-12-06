def collatz(number):
    sequence = []

    while not number == 1:
        if number%2 == 0:
            number /= 2
            sequence.append(number)
        else:
            number = 3 * number + 1
            sequence.append(number)

    return sequence

def longestCollatz():
    maxLength = 0
    maxIndex = 0

    #Create list of collatz sequence from 1 to 1000000
    for i in range(1, 1000000):
        sequence = collatz(i)
        if len(sequence) > maxLength:
            maxIndex = i
            maxLength = len(sequence)

    print maxIndex

longestCollatz()
