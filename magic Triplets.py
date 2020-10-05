#User function Template for python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem :- Given an array of size n, a triplet (a[i], a[j], a[k]) is called a Magic Triplet 
#           if a[i] < a[j] < a[k] and i < j < k.  Count the number of magic triplets in a given array.

#Example :-
"""
  1.Input: arr = [3, 2, 1]
    Output: 0
    Explanation: There is no magic triplet.

  2.Input: arr = [1, 2, 3, 4]
    Output: 4
    Explanation: Fours magic triplets are 
    (1, 2, 3), (1, 2, 4), (1, 3, 4) and (2, 3, 4).

"""
 

class Solution:
	def countTriplets(self, nums):
	    res = 0
	    for i in range(1,len(nums)):
	        left = i-1
	        right = i+1
	        l_count = 0
	        r_count = 0
	        
	        while(left>= 0):
	            if (nums[left] <nums[i]):
	                l_count += 1
	            left -= 1
	        while(right<len(nums)):
	            if nums[right] > nums[i]:
	                r_count += 1
	            right += 1
	        res += l_count*r_count
	    return res