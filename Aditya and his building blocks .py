#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
$TaGs :- Arrays , Medium , GeeksForGeeks
#Problem :- Aditya has arranged some of his building blocks in N columns. Each column has a certain number of blocks given by an array A.
#           Each element of A(i.e. Ai) is the height of the ith column. Aditya now has M blocks left. He doesn't like small columns.
#           So he wants to maximum the minimum of all heights. He may or may not use all of the M blocks.
#           Determine the maximised height.


#Example :- 
"""
    Input : 
        3
        5 6
        1 2 3 4 5
        3 4
        2 8 9
        6 3
        1 1 2 2 1 2
    Output : 
        4
        6
        2

Explaination : 
Case 1 : Final heights of blocks - 4 4 4 4 5
Case 2 : Final heights of blocks - 6 8 9
Case 3 : Final heights of blocks - 2 2 2 2 2 2
 
"""

import heapq

if __name__ == "__main__":
    for _ in range(int(input())):
        n,m = map(int,input().split(" "))
        arr = list(map(int,input().rstrip().split(" ")))
        heapq.heapify(arr)
        while(m):
            temp = arr[0]
            heapq.heappop(arr)
            temp += 1
            heapq.heappush(arr,temp)
            m -= 1
        print(arr[0])

        
