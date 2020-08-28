#Python3 
"""
    Code By : Deepak Kumar(Insan)
    Contact Us : a9649060356@gmail.com

Q -> Given two binary arrays arr1[] and arr2[] of same size n. Find length of the longest common span (i, j) 
     where j >= i such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j]. 
     Elements are only 0 or 1.

"""
#Approach is O(n)
#Array Medium Level Problem of GFG

def longestCommonSum(arr1, arr2, n): 
    maxLen = 0
      
    
    presum1 = 0
    presum2 = 0
    diff = {} 
      
    for i in range(n): 
         
        presum1 += arr1[i] 
        presum2 += arr2[i] 
          
        curr_diff = presum1 - presum2 
          
        if curr_diff == 0: 
            maxLen = i+1  
        elif curr_diff not in diff: 

            diff[curr_diff] = i 
        else:                   
            length = i - diff[curr_diff] 
            maxLen = max(maxLen, length) 
          
    return maxLen 
for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int,input().rstrip().split(" ")))
    arr2 = list(map(int,input().rstrip().split(" ")))
    print(longestCommonSum(arr1, arr2, n))



#this For you 

"""
The idea is based on below observations.

    1.Since there are total n elements, maximum sum is n for both arrays.
    2.Difference between two sums varies from -n to n. So there are total 2n + 1 possible values of difference.
    3.If differences between prefix sums of two arrays become same at two points, then subarrays between these two points have same sum.

Below is Complete Algorithm.

    1.Create an auxiliary array of size 2n+1 to store starting points of all possible values of differences (Note that possible values of differences vary from -n to n, i.e., there are total 2n+1 possible values)
    2.Initialize starting points of all differences as -1.
    3.Initialize maxLen as 0 and prefix sums of both arrays as 0, preSum1 = 0, preSum2 = 0
    4.Traverse both arrays from i = 0 to n-1.
        Update prefix sums: preSum1 += arr1[i], preSum2 += arr2[i]
        Compute difference of current prefix sums: curr_diff = preSum1 – preSum2
        Find index in diff array: diffIndex = n + curr_diff // curr_diff can be negative and can go till -n
        If curr_diff is 0, then i+1 is maxLen so far
        Else If curr_diff is seen first time, i.e., starting point of current diff is -1, then update starting point as i
        Else (curr_diff is NOT seen first time), then consider i as ending point and find length of current same sum span. If this length is more, then update maxLen
    5.Return maxLen

"""