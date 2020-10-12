#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a949060356@gmail.com

"""
$TaGs :- Array ,#InterView Prepration

#Problem :- The cost of stock on each day is given in an array A[] of size N. 
#           Find all the days on which you buy and sell the stock so that in 
#           between those days your profit is maximum.


#Example :- 
"""
    Input:
        3
        7
        100 180 260 310 40 535 695
        4
        100 50 30 20
        10
        23 13 25 29 33 19 34 45 65 67

    Output:
        (0 3) (4 6)
        No Profit
        (1 4) (5 9)

    Explanation:
        Testcase 1: We can buy stock on day 0, and sell it on 3rd day, which will give us maximum profit.
"""


def ans(arr,n):
    result = []
    maxs = arr[0]
    maxs_Index = 0
    prev = arr[0]
    prev_Index = 0
    for i in range(1,n):
        if arr[i] > maxs:
            maxs = arr[i]
            maxs_Index = i
        elif ((prev_Index+1) == i) and (maxs > arr[i]):
            prev_Index ,prev = i,arr[i]
            maxs = prev
            maxs_Index  = prev_Index
        else:
            result.append((prev_Index,maxs_Index))
            prev_Index,prev = i ,arr[i]
            maxs,maxs_Index = prev,prev_Index
    if prev < maxs:
        result.append((prev_Index,maxs_Index))
    return result


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        result = ans(arr,n)
        if len(result):
            for res in result:
                print("("+str(res[0]),str(res[1]) +")",end=" ")
            print()
        else:
            print("No Profit")