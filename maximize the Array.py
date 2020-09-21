#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#TAGs : Array , Medium , Microsoft ,GeeksForGeeks

#Problem :- You are given two arrays of numbers. You have to maximize the first array by using the elements 
#           from the second array such that the new array formed contains unique elements. For example, let 
#           the size of array be 'n'. Then the output should be n greatest but unique elements of both the arrays. 
#           The order of elements should be as explained in example below, i.e., giving the second array priority.


#Example:
"""
    Input:
        2
        5
        7 4 8 0 1
        9 7 2 3 6
        4
        6 7 5 3
        5 6 2 9
    Output:
        9 7 6 4 8
        5 6 9 7
"""


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().rstrip().split(" ")))
    arr2 = list(map(int,input().rstrip().split(" ")))
    temp = [0 for _ in range(10)]
    for i in range(n):
        temp[arr[i]] = 1
        temp[arr2[i]] = 1
    s_sort = set()
    t = 0
    for i in range(9,-1,-1):
        if t >= n:
            break
        if temp[i]:
            s_sort.add(i)
            t += 1
    res = []
    result_same = set()
    s_prior = set(arr2)
    for i in range(len(arr)):
        if arr2[i] in s_sort and arr2[i] not in result_same:
            print(arr2[i],end=" ")
            result_same.add(arr2[i])
        if arr[i] in s_sort and arr[i] not in s_prior and arr[i] not in result_same:
            res.append(arr[i])
            result_same.add(arr[i])
    print(*res,end=" ")
    print()

$Happy Coding ;)
    