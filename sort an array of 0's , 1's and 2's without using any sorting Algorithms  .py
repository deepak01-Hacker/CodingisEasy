#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

#Example :- 
"""
    Input :
        2
        5
        0 2 1 2 0
        3
        0 1 0

    Output:
        0 0 1 2 2
        0 0 1

    Explanation:
        Testcase 1: After segragating the 0s, 1s and 2s, we have 0 0 1 2 2 which shown in the output.
"""


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        zero = 0 
        ones = 0
        twos = 0
        for i in range(n):
            if arr[i] == 1:
                ones += 1
            elif arr[i] == 0:
                zero += 1
            else:
                twos += 1
        for i in range(n):
            if zero:
                arr[i] = 0
                zero -= 1
            elif ones:
                arr[i] = 1
                ones -= 1
            else:
                arr[i] = 2
        print(*arr)