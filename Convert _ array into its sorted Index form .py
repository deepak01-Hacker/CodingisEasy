#User function Template for python3


#User function Template for python3
"""
    Code By    : Deepak Kumar(Insan)
    Contact us : a9649060356@gmail.com
"""


#Problem : Given an array with N distinct elements, convert the given array to a reduced 
#          form where all elements are in range from 0 to N-1. The order of elements is same, 
#          i.e., 0 is placed in place of smallest element, 1 is placed for second smallest element,
#           … N-1 is placed for largest element.

#Explanation :- 
"""
Input:
    N = 3   
    Arr[] = {10, 40, 20}

    Output: 0 2 1

    Explanation: 10 is the least element so it
    is replaced by 0. 40 is the largest
    element so it is replaced by 3-1 = 2. And
    20 is the 2nd smallest element so it is
    replaced by 1.
    
"""


#User function Template for python3
class Solution:

	def convert(self,arr, n):
		set_arr = [i for i in arr]
		map = {}
		set_arr.sort()
		for i in range(n):
		    map[set_arr[i]] = i
		for i in range(n):
		    arr[i] = map[arr[i]]
		    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends