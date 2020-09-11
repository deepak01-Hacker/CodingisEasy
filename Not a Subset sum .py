#User function Template for python3
"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem:-Given a sorted array of N positive integers, find the smallest 
#         positive integer S such that S cannot be represented as sum of 
#         elements of any subset of the given array set.

#Tags : Medium , Array , Sort, GeeksForGeeks

class Solution:
    def findSmallest(self, arr, n):
        if arr[0] > 1:
            return 1
        max_pos = 0
        for i in range(0,len(arr)):
            if arr[i] > max_pos+1:
                return max_pos+1
            else:
                max_pos += arr[i]
        return max_pos+1
            
