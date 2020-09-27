#Python3

"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem :- Given N distinct digits in an array A (from 1 to 9), 
#           Your task is to complete the function getSum which finds 
#           sum of all n digit numbers that can be formed using these digits. 


#Example :
"""
    Input:
        2
        3
        1 2 3
        2
        1 2
    Output:
        1332
        33
"""

MOD = 10**9+7

def interchange(s,a,b):
    string_array = list(s)
    t = string_array[a]
    string_array[a] = string_array[b]
    string_array[b] = t
    return "".join(string_array)


re = 0
def perm(s,l,r,set_,res):
    global re
    if l == r:
        if int(s) not in set_:
            re += int(s)
            set_.add(int(s))
        return 
    for i in range(l,r+1):
        s = interchange(s,l,i)
        perm(s,l+1,r,set_,res)
        s = interchange(s,l,i)

def getSum(n, arr):
    res = 0
    set_ = set()
    s = ""
    for i in arr:
        s += str(i)
    global re
    re = 0
    perm(s,0,n-1,set_,res)
    return re%1000000007

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(getSum(n,arr))
    
    
