"""
LCS: Given two string (of lengths n and m) find the length of the longest string
which is a subsequence of both inputs
"""
import string

from tabulate import tabulate


def LCS(input1: string, input2: string):
    iRange = list(range(len(input1) + 1))
    jRange = list(range(len(input2) + 1))
    L = list(list())
    # base values
    L.append([0 for _ in iRange])
    for i in iRange:
        if i > 0:
            L.append([0])

    # populate
    for i in iRange:
        if i == 0: continue
        row = L[i]
        for j in jRange:
            if j == 0: continue
            if input1[i - 1] == input2[j - 1]:
                row.append(1 + L[i - 1][j - 1])
            else:
                row.append(max(L[i - 1][j], L[i][j - 1]))
    tabulated(iRange, (input1, input2), L)
    m, n = iRange[-1], jRange[-1]
    return L[m][n]


def tabulated(iRange, input, L):
    (a, b) = input
    # headers = ['i/j'] + iRange
    table = [['a/b'] + [''] + list(a), [''] + L[0]]
    for index, x in enumerate(b):
        table.append([x] + L[index])
    print(tabulate(table, tablefmt="grid"))


def test():
    print("\tLCS: Longest Common Subsequence")
    testPasses(("ABECBAB","BCDBCDA"), 4)
    testPasses(("ABECBA","BCDBCDA"), 4)
    print(f"{'-' * 200}")


def testPasses(input, expectedOutput):
    (a, b) = input
    output = LCS(a, b)
    print()
    if (output == expectedOutput):
        print(f"\t\tPass LCS({input}) == {expectedOutput} ")
        return True
    print(f"\t\tFail LCS({input}) == {expectedOutput} but got {output}")
    return False
