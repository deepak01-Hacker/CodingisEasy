#Python3 

"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem : You have to given a array of integers and you will to find sum of bit difference in pairs of Binary numbers of array element ">"

#Tags : Easy , GeeksForGeeks , Array , BitMagic , Google


#User function Template for python3
class Solution:
    def sumBitDifferences(self,arr,n):
        ans = 0
        for i in range(0,32):
            count = 0
            for j in range(0,n):
                if ((arr[j] & (1<<i))):
                    count += 1
            ans += (count*(n-count)*2)
        return ans 

