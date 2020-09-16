#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
"""

#Problem :- Three arrays of the same size are given. Find a triplet such that (maximum – minimum) in that triplet is the minimum of all the triplets. 
#           A triplet should be selected in a way such that it should have one number from each of the three given arrays. This triplet is the happiest 
#           among all the possible triplets. Print the triplet in decreasing order. If there are 2 or more smallest difference triplets, then the one with 
#           the smallest sum of its elements should be displayed.

#TaGs : Array , Searching , Sorting , Medium , GeeksForGeeks

#Explanation : 
"""
    Input:
        N=3
        a[] = { 5, 2, 8 }
        b[] = { 10, 7, 12 }
        c[] = { 9, 14, 6 }  
    Output: 7 6 5
    
    Explanation:
        The triplet { 5,7,6 }  has difference
        (maximum - minimum)= (7-5) =2 which is
        minimum of all triplets.  
"""

#User function Template for python3

class Solution:
    def smallestDifferenceTriplet(self,a,b,c,n):
        ans = [0,0,0]
        a.sort()
        b.sort()
        c.sort()
        mins= 10**6
        sum_minimum = 10**6
        i=j=k=0
        while(i<n and j < n and k < n):
            max_at_point = max(a[i],b[j],c[k])
            min_at_point = min(a[i],b[j],c[k])
            if mins > max_at_point - min_at_point:
                mins = max_at_point - min_at_point
                sum_minimum = a[i]+b[j]+c[k]
                ans[0] = a[i]
                ans[1] = b[j]
                ans[2] = c[k]
            elif mins == max_at_point - min_at_point and (a[i]+b[j]+c[k]) < sum_minimum:
                sum_minimum = a[i]+b[j]+c[k]
                ans[0] = a[i]
                ans[1] = b[i]
                ans[2] = c[i]
            if min_at_point == a[i]:
                i += 1
            elif  min_at_point == b[j]:
                j += 1
            elif min_at_point == c[k]:
                k += 1
        ans.sort(reverse=True)
        return ans
            
