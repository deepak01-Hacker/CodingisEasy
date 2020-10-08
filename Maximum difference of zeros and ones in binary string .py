#User function Template for python3
"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com

"""
$TaGS : Dynamic Programming , Kadane Algo , GFG ,String 

#Problem :- Given a binary string of 0s and 1s. The task is to find the maximum difference of 
#           the number of 0s and the number of 1s (number of 0s – number of 1s) in the substrings of a string.
#           Note: In the case of all 1s, the answer will be -1. 

#Problem Link : https://practice.geeksforgeeks.org/problems/maximum-difference-of-zeros-and-ones-in-binary-string4111/1/?category[]=Dynamic%20Programming&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]Dynamic%20ProgrammingproblemStatusunsolveddifficulty[]0page1

#Example :
"""
    Input : S = "11000010001" 
    Output : 6 
    Explanatio: From index 2 to index 9, 
    there are 7 0s and 1 1s, so number 
    of 0s - number of 1s is 6. 
"""


class Solution:
	def maxSubstring(self, S):
	    n = len(S)
	    arr = []
	    for i in range(n):
	        if S[i] == "1":
	            arr.append(-1)
	        else:
	            arr.append(1)
	    sum = 0
	    maxs = -10**6
	    for i in range(n):
	        sum += arr[i]
	        if sum < arr[i]:
	            sum = arr[i]
	        maxs = max(maxs,sum)
	    return maxs
	        