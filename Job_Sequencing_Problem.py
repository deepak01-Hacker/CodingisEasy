#Python3

"""
    Code By     : Deepak Kumar
    Contact us  : a9649060356@gmail.com
    Code Logic  : GeeksForGeeks
"""

#Problem :- > Given an array of jobs where every job has a deadline and associated 
#             profit if the job is finished before the deadline. It is also given that every 
#             job takes single unit of time, so the minimum possible deadline for any job is 1. 
#             How to maximize total profit if only one job can be scheduled at a time.



Code: 

def maxProfit(profit,n):
    zip = []
    n = 0
    
    for i in range(0,len(profit),3):
        n = max(n,profit[i+1])
        zip.append([profit[i+2],profit[i+1],profit[i]])

    zip.sort(reverse=True)
    ans = 0
    jobs = 0
    visited = [False] *n
    
    for i in range(len(zip)):

        for j in range(min(n-1,zip[i][1]-1),-1,-1):

            if visited[j] is False:
                ans += zip[i][0]
                visited[j] = True
                jobs += 1
                break
    print("Jobs : " +str(jobs)+ " Maximum Profit "+str(ans))

if __name__ == "__main__":
    for _ in range(int(input())):
        DeadLine = int(input())
        Profit = list(map(int,input().rstrip().split(" ")))
        maxProfit(Profit,DeadLine)

#Happy Coding ; )