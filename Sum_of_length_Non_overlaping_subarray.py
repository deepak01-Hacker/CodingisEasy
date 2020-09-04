#Python3
"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
"""
# Que- > Given an array of N elements, you are required to find the maximum sum 
#        of lengths of all non-overlapping subarrays with K as the maximum 
#        element in the subarray.


#Tags : Array,Medium,GeeksForGeeks

def sumOverlapingLength(arr,k):
    Sum_ans = 0
    count = 0
    flag = False
    for index in range(len(arr)):
        if arr[index] == k:
            flag = True
        if arr[index] < k+1:
            count += arr[index]
        else:
            if flag:
                Sum_ans += count
                flag = False
            count = 0
    if flag:
        Sum_ans += count
    return Sum_ans

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        k = int(input())                        #Here K is Maximum element of any subarray 
        print(sumOverlapingLength(arr,k))

#Happy Coding ;)