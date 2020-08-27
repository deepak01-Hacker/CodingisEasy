#python3
"""
Code By : Deepak Kumar
Contact us : a9649060356@gmail.com
"""
#String Medium Level Problem 
#Question-> Smallest Window in a string containing all the characters of  another string ?


for _ in range(int(input())):
    string = input() #This is Longest sTRING 
    second_string = input() #
    hash_string1= [0]*256 #hash
    hash_string2 = [0]*256
    len_second_string = len(second_string)
    for i in second_string:
        hash_string2[ord(i)] += 1
    cnt_ = 0 # this count window substring in longest string
    start = 0
    mins = [0,len(string)] # this contain minimum window
    for index in range(len(string)):
        hash_string1[ord(string[index])] += 1
        if hash_string2[ord(string[index])] >= hash_string1[ord(string[index])]:
            cnt_ += 1
        while cnt_ >= len_second_string:
            if hash_string1[ord(string[start])] < hash_string2[ord(string[start])]:
                break
            if index - start < mins[1] - mins[0]:
                mins[0] = start
                mins[1] = index
            hash_string1[ord(string[start])] -= 1
            if hash_string2[ord(string[start])] > hash_string1[ord(string[start])]:
                cnt_ -= 1
            start += 1
            
    if mins[0] == 0 and mins[1] == len(string):
        print("-1") # Is there no substring presents in String that contain all char of another string
    else:
        for index in range(mins[0],mins[1]+1):
            print(string[index],end="")
        print()
    
# This code look like a complex problem , but You believe me Its one of the easiest 
#this algo take minimum time 

# If there in the Question Time Limit is Not matter then You go with O(n)^2
#solution 