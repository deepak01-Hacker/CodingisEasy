#Python3

"""
    Code By     : Deepak Kumar
    Contact us  : a9649060356@gmail.com
"""

#Problem : - Is array Contain that Subarray have zero sum Then Return True or False ?

#Tags : Hashing , Set ,Array

if __name__ == "__main__":
    for _ in range(int(input())):
        length_Array = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        s = set()
        hash_ = 0
        flag = False
        for val in arr:
            hash_ += val
            if hash_ in s:
                flag = True
                continue
            else:
                s.add(hash_)
        print(flag)


#Happy Coding ;)
        