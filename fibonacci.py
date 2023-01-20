"""
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
The sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
It is named after the Italian mathematician Leonardo of Pisa, who was also known as Fibonacci.
The sequence has many interesting properties and appears in many areas of mathematics and nature.
"""

from tabulate import tabulate


def fn(input: int):
    iRange = list(range(1, input + 1))
    FIB = []
    for i in iRange:
        if i <= 2:
            FIB.append(1)
        else:
            FIB.append(FIB[-2] + FIB[-1])
    tabulated(iRange, FIB)
    return FIB[-1]


def tabulated(iRange, L):
    headers = ['i'] + iRange
    table = [['L'] + L]
    print(tabulate(table, headers=headers, showindex=True, tablefmt="grid"))


def test():
    print("\tFibonacci")
    # testPasses(1, 1)
    # testPasses(2, 1)
    # testPasses(3, 2)
    testPasses(15, 610)
    # testPasses(49, 7778742049)


def testPasses(input, expectedOutput):
    output = fn(input)
    print()
    if (output == expectedOutput):
        print(f"\t\tPass FIB({input})=={expectedOutput} ")
        return True
    print(f"\t\tFail FIB({input})=={expectedOutput} but got {output}")
    return False
