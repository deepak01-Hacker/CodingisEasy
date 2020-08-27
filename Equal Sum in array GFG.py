#python3

"""
Code By : Deepak Kumar
Contact us: a9649060356@gmail.com
"""
#Q - >" " Equal Sum Problem" in array topic of GFG Medium level Question


"""
QUESTION : Given an array A of length N. Determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of
the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero. 
Formally, find an i, such that, A1+A2...Ai-1 =Ai+1+Ai+2...AN.



Example:

Input
1
4
1 2 3 3
Output:
YES
"""
def IsExistEqualSum(arr,arr_sum):
    left_sum = 0
    for i in arr:
        arr_sum -= i
        if left_sum == arr_sum:
            return "YES"
        left_sum += i
        
    return "NO"
        
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().rstrip().split(" ")))
    if n == 1:
        print("YES")
    else:
        arr_sum = sum(arr)
        print(IsExistEqualSum(arr,arr_sum))
# O(n) Solution
 
#Happy Coding :-) 