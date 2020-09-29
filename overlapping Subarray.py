#User function Template for python3

"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com

"""

#Problem :- Given a collection of Intervals, the task is to merge all of the overlapping Intervals.

#Example :-
"""
  1 :Input:
        N = 4
        Intervals = {(1,3),(2,4),(6,8),(9,10)}
    Output: 
        1 4 6 8 9 10
    Explanation: Given intervals: [1,3],[2,4],[6,8],[9,10], 
                we have only two overlapping intervals here,[1,3] 
                and [2,4]. Therefore we will merge these two and 
                return [1,4],[6,8], [9,10].

  2 :Input:
        N = 4
        Intervals = {(6,8),(1,9),(2,4),(4,7)}
    Output: 
        1 9
"""

def overlappedInterval(parr,n):
    result = []
    parr.sort()
    check_range = -1
    result.append([])
    for pair in parr:
        if pair[0] > check_range:
            if check_range == -1:
                result[-1].append(pair[0])
            else:
                result[-1].append(check_range)
                result.append([])
                result[-1].append(pair[0])
            check_range = pair[0]
        if pair[1] > check_range:
            check_range = pair[1]
    result[-1].append(check_range)
    return result



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t= int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        parr=[]

        i=0
        while i<2*n:
            parr.append([arr[i],arr[i+1]])
            i+=2

        ans=overlappedInterval(parr,n)

        for e in ans:
            print(*e,end=' ')
        print()


# } Driver Code Ends