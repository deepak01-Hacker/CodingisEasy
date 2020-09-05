#Python3
"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Question -> Count the Groups and Triplets in array that sum is Divisible By 3 ?
#Explanation : arr    = [3,2,1,4]
#              groups : [2,1] = sum(3)%3 == 0,[2,4] = sum(6)%3 == 0
#              Triplets:[3,2,1] = sum(3)%3 == 0,[3,2,4] = sum(9)%3 == 0
#              so Answer is 4


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        hash_ = [0]*3 #Here We hash element Accourding to its Remaninder there is a logic if you have 0 remiander then you have all 
                      #elements in hash_[0] are satisfy conditioin groups and Triplets and 1+2 == 3
        for element in arr:
            hash_[element%3] += 1
        count = 0
        count += (hash_[0]*(hash_[0]-1))//2
        count += hash_[0]*hash_[1]
        count += (hash_[0]*(hash_[0]-1)*(hash_[0]-2))//6
        count += (hash_[1]*(hash_[1]-1)*(hash_[1]-2))//6
        count += (hash_[2]*(hash_[2]-1)*(hash_[2]-2))//6
        count += hash_[0]*hash_[1]*hash_[2]
        print(count) #here All counted Groups and Triplets

#Happy Coding ;)