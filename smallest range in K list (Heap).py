#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem : Given K sorted lists of integers of size N each, find the smallest range that includes at 
#           least one element from each of the K lists. If more than one such range's are found, find 
#           the first such range found.

#Example:-
"""
    Input:
    N = 5, K = 3
    KSortedArray[][] = {{1 3 5 7 9},
                        {0 2 4 6 8},
                        {2 3 5 7 11}}
    Output: 1 2
    Explanation: K = 3
    A:[1 3 5 7 9]
    B:[0 2 4 6 8]
    C:[2 3 5 7 11]
    Smallest range is formed by number 1
    present in first list and 2 is present
    in both 2nd and 3rd list.
"""


ptr = [0 for _ in range(501)]

def smallestRange(numbers):
    n = len(numbers[0])
    
    for i in range(len(numbers)+1):
        ptr[i] = 0
    MinVal , MaxVal = 0,0
    Range = 502
    
    while(1):
        
        maxTemp = -10**8
        minTemp = 10**8
        index = -1
        flag = False
        
        for i in range(k):
            
            if ptr[i] >= n:
                flag = True
                break
            
            if numbers[i][ptr[i]] < minTemp:
                minTemp = numbers[i][ptr[i]]
                index = i
                
            if numbers[i][ptr[i]] > maxTemp:
                maxTemp = numbers[i][ptr[i]]
                
        if flag:
            break
        
        ptr[index] += 1
        if maxTemp-minTemp < Range:
            Range = maxTemp-minTemp
            MaxVal = maxTemp
            MinVal = minTemp
        
        
    return [MinVal,MaxVal]
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = smallestRange(numbers)
    print(r[0],r[1])
# } Driver Code Ends