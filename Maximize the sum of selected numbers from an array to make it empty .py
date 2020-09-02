#python3
"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
# Tags : Dynamic Programming , Map ,Array
#GeeksforGeeks , Medium level array Problem
#Question - > Maximize the sum of selected numbers from an array to make it empty 
"""
Explanation: Given an array of N numbers, we need to maximize the sum of 
             selected numbers. At each step, you need to select a number Ai, 
             delete one occurrence of Ai-1 (if exists) and Ai each from the array. 
             Repeat these steps until the array gets empty. The problem is to maximize 
             the sum of selected numbers. 
"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().rstrip().split(" ")))
    arr.sort()
    sums = 0
    while(arr):
        maximum_element = arr[-1]
        arr.pop(-1)
        sums += maximum_element
        try:
            index_of_lesser_from_max = arr.index(maximum_element-1)
            arr.pop(index_of_lesser_from_max)
        except:
            sums = sums
    print(sums)

#Happy Coding ;)


#Don't Compete youself to others , Compete with you what you have today and what was you yesterday 
# Death is real Truth of our life so Enjoy coding whenever you not die 
# #A lot of Money is not success Satisfaction is Real Success                                  MEANWHILE :) b/w ;)

    
