#python3

"""
Code By : Deepak Kumar
Contact Us : a9649060356@gmail.com

Specail Thanks To Yug Soni Bcz HE give me the idea of this ALgo REally its amazing
"""
#Q> Missing element in Continous array from 0 :)
#Main Idea or Algorithm - >
#step 1: find array element sum
#step 2 : find max_element_array and find sum of max_element _sum
#step 3 : print(max_element_array_sum - array_element_sum)
              #or
#You use Hashing 
              #or
#using Indexing Maping 

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        max_number = max(arr)
        sum_ = max_number*(max_number+1)//2
        print(sum_ - sum(arr))


#Extra Space : O(1)
#complexity : O(n)

