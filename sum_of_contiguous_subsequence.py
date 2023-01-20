from typing import List

from tabulate import tabulate

"""
A contiguous subsequence of a list S is a subsequence made up of consecutive elements of S. For
instance, if S is 5, 15, −30, 10, −5, 40, 10,then 15, −30, 10 is a contiguous subsequence but 5, 15, 40 is not. 

Give a linear-time algorithm for
the following task:
Input: A list of numbers, a 1 , a 2 , . . . , a n .
Output: The contiguous subsequence of maximum sum (a subsequence of length zero has sum zero).
For the preceding example, the answer would be 10, −5, 40, 10, with a sum of 55.
(Hint: For each j ∈ {1, 2, . . . , n}, consider contiguous subsequences ending exactly at position j.)
"""


def SCS(input: List[int]):
    if not input:  # case of empty list
        return 0
    iRange = list(range(len(input) + 1))
    L = [0]
    for i in iRange:
        if i == 0: continue
        L.append(max(0, L[i - 1] + input[i - 1]))
    tabulated(iRange, input, L)
    return max(L)


def tabulated(iRange, input, L):
    headers = ['i'] + iRange
    table = [['a', 0, ] + input, ['L'] + L]
    print(tabulate(table, headers=headers, tablefmt="grid"))


def test():
    print("\tSCS: Sum of contiguous subsequence")
    # testPasses([], 0)
    testPasses([5, 15, -30, 10, -5, 40, 10], 55)
    testPasses([5, 40, 15, -60, 10, -5, 40, 10], 60)
    print(f"{'-' * 200}")


def testPasses(input, expectedOutput):
    output = SCS(input)
    print()
    if (output == expectedOutput):
        print(f"\t\tPass SCS({input})=={expectedOutput} ")
        return True
    print(f"\t\tFail SCS({input})=={expectedOutput} but got {output}")
    return False
