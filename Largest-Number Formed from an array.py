#python3
#get biggest Element from array

"""
the first approach is Taken from GFG
"""

def largestNumber(array): 
      
    # extval is a empty list for extended  
    # values and ans for calculating answer 
    extval, ans = [], "" 
      
    # calculating the length of largest number 
    # from given and add 1 for further operation 
    l = len(str(max(array))) + 1
      
    # iterate given values and  
    # calculating extended values 
    for i in array: 
        temp = str(i) * l 
          
        # make tuple of extended value and  
        # equivalant original value then  
        # append to list 
        extval.append((temp[:l:], i)) 
      
    # sort extval in descending order 
    extval.sort(reverse = True) 
      
    # iterate extended values 
    for i in extval: 
          
        # concatinate original value equivalant 
        # to extended value into ans variable 
        ans += str(i[1]) 
  
    if int(ans)==0: 
        return "0"
    return ans 
  
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().rstrip().split(" ")))
    print(largestNumber(arr))



"""
Second Aprroach , get maximum from all permutaions
"""
  
from itertools import permutations 
def largest(l): 
    lst = [] 
    for i in permutations(l, len(l)): 
        # provides all permutations of the list values, 
        # store them in list to find max 
        lst.append("".join(map(str,i)))  
    return max(lst) 
  
print(largest([54, 546, 548, 60]))