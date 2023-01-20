"""
In the longest increasing subsequence problem, the input is a sequence of numbers a 1 , . . . , a n .
A subsequence is any subset of these numbers taken in order, of the form a i 1 , a i 2 , . . . , a i k where
1 ≤ i 1 < i 2 < · · · < i k ≤ n, and an increasing subsequence is one in which the numbers are
getting strictly larger. The task is to find the increasing subsequence of greatest length.
"""
from typing import List

from tabulate import tabulate


def LIS(input: List[int]):
    if not input:  # case of empty list
        return 0
    L = [1 for _ in input]  # initialize all spots as i
    iRange = list(range(len(input)))
    for i in iRange:
        for j in range(1, i):
            if (input[j] < input[i]):
                if L[i] < L[j] + 1:
                    L[i] = L[j] + 1
    tabulated(iRange, input, L)
    return max(L)


def tabulated(iRange, input, L):
    headers = ['i'] + iRange
    table = [['a'] + input, ['L'] + L]
    print(tabulate(table, headers=headers,tablefmt="grid"))


def test():
    print("\tLIS: Longest Increasing subsequence")
    # testPasses([], 0)
    testPasses([5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3], 6)
    print(f"{'-' * 200}")


def testPasses(input, expectedOutput):
    output = LIS(input)
    print()
    if (output == expectedOutput):
        print(f"\t\tPass LIS({input})=={expectedOutput} ")
        return True
    print(f"\t\tFail LIS({input})=={expectedOutput} but got {output}")
    return False
