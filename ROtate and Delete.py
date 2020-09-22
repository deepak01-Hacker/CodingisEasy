#Python3

"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com

"""

#Problem : Given an array arr[] of N integers. Do the following operation n-1 times. For every Kth operation:

#   * Right rotate the array clockwise by 1.
#   * Delete the (n-k+1)th last element.

# Now, find the element which is left at last.



"""
    Approach : 

    Patteren Recognize in This Question So : --

    for odd N : floor( (n-3)/4 )+2
    for even N : floor( (n-2)/4 )+1
"""

#O(n)
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().rstrip().split(" ")))
    if n%2 != 0:
        t= n-3
        t = t//4
        t += 2
        print(arr[t%len(arr)])
    else:
        t= n-2
        t = t//4
        t += 1
        print(arr[t%len(arr)])

#O(n^2)
for _ in range(int(input())):
    n = int(input())
    arr =  list(map(int,input().rstrip().split(" ")))
    k = 0
    for i in range(n//2):
        t = []
        t.append(arr[-1])
        t += arr[:len(arr)-1]
        arr = t
        th = (k%len(arr)+1)
        arr.pop(-th)
        k += 1
    print(arr[0])
