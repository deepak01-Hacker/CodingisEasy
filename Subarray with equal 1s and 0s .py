#Python3
"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem :- Given an array arr[] of size N containing 0s and 1s only. The task is to count the subarrays having equal number of 0s and 1s. 
#TaGS : Medium , Array , Binary , HashMap ,GeeksForGeeks

#Explanation : 
"""
    Input:
        7                // length_of_array
        1 0 0 1 0 1 1
    Output:
        8

    Explanation:
    Testcase 1: The index range for the 8 sub-arrays are:
    (0, 1), (2, 3), (0, 3), (3, 4), (4, 5)
    (2, 5), (0, 5), (1, 6) 
"""


def subArrayCount(arr,lengthOfArray):
    map = {}
    sum = 0
    count = 0 //number of subArray
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1
        sum += arr[i]
        if sum == 0:
            count+= 1
        try:
            count += map[sum]
        except:
            count += 0
        map[sum] = map.get(sum,0)+1
    print(count)

if __name__ == "__main__":
    for _ in range(int(input())):
        lengthOfArray = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        subArrayCount(arr,lengthOfArray)