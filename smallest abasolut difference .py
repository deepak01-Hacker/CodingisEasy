#Python3
"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem :- Given an array of size n containing positive integers n and a number k,
#           The absolute difference between values at indices i and j is |a[i] – a[j]|. 
#           There are n*(n-1)/2 such pairs and you have to print the kth smallest absolute 
#           difference among all these pairs.

#Example:
"""
Input:
    2
    4
    1 2 3 4
    3
    2
    10 10
    1

Output:
    1
    0
"""


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        k = int(input())
        result_arr = []
        for i in range(n-1):
            for j in range(i+1,n):
                result_arr.append(abs(arr[i]-arr[j]))
        result_arr.sort()
        print(result_arr[k-1])