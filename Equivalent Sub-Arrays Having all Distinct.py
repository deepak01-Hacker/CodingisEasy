#Python3

"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com

"""

#Problem :- Given an array arr[] of n integers. Count the total number of sub-array having total distinct elements 
#           same as that of total distinct elements of the original array.

#Example :
"""
    Input:
        N=5
        arr[] = {2, 1, 3, 2, 3} 
    Output: 5
    Explanation:
        Total distinct elements in array is 3
        Total sub-arrays that satisfy the condition are:
            Subarray from index 0 to 2
            Subarray from index 0 to 3
            Subarray from index 0 to 4
            Subarray from index 1 to 3
            Subarray from index 1 to 4
"""

def subArrays(arr,n):
    k = len(set(i for i in arr))
    map = {}
    window = 0
    right = 0
    ans = 0
    for left in range(n):
        while(right <n and window < k):
            if arr[right] in map.keys():
                map[arr[right]] += 1
            else:
                map[arr[right]] = 1
            if map[arr[right]] == 1:
                 window += 1
            right += 1
        if window == k:
            ans += n-right+1
        map[arr[left]] -= 1
        if map[arr[left]] == 0:
            window -= 1
    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split("")))
        subArrays(arr,len(arr))