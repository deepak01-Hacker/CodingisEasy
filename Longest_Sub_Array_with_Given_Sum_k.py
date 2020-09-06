#Python3

"""
    Code By     : Deepak Kumar
    Contact us  : a9649060356@gmail.com
"""
#Problem :- Given an array containing N integers and an integer K. 
#           Your task is to find the length of the longest Sub-Array 
#           with sum of the elements equal to the given value K


#Tags : Medium ,Array,hash,dictionary,set,Sliding Window,GeeksForGeeks

if __name__ == "__main__":
    for _ in range(int(input())):
        n,k = map(int,input().split(" "))
        arr = list(map(int,input().rstrip().split(" ")))
        hash_ = {}
        max_ = 0
        s = set()
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            s.add(sum)
            if sum == k:
                max_ = max(max_,i+1)
            try:
                if hash_[sum]:
                    hash_[sum] = hash_[sum]
            except:
                hash_[sum] = i
            print(sum-k in s,sum-k,sum,arr[i])
            if sum-k in s:
                max_ = max(max_,i-hash_[sum-k])
        print(max_)
        n,k = map(int,input().split(" "))
        arr = list(map(int,input().rstrip().split(" ")))
        hash_ = {}
        max_ = 0
        s = set()
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            s.add(sum)
            if sum == k:
                max_ = max(max_,i+1)
            try:
                if hash_[sum]:
                    hash_[sum] = hash_[sum]
            except:
                hash_[sum] = i
            print(sum-k in s,sum-k,sum,arr[i])
            if sum-k in s:
                max_ = max(max_,i-hash_[sum-k])
        print(max_)




/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
!@ Method : 2
#Time Compexity: o(nlogn) ~ O(n2)

if __name__ == "__main__":
    for _ in range(int(input())):
        n,k = map(int,input().split(" "))
        arr = list(map(int,input().rstrip().split(" ")))
        maxs_ = 0
        sum = 0
        for i in range(n):
            for j in range(i,n):
                sum += arr[j]
                if sum == k:
                    max_ = max(max_,(j-i)+1)
        print(max_)

#Happy Coding

#My one day effort == this Problem Code :) So first Try After See the Code ;)