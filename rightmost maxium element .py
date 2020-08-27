#python3
#Problem : find righttmost maximum element froom each element of array 
#Save Gotham array problem is Same with This you can solve that with this
#GFG Array Medium Level Problem

""" 
Code by : Deepak Kumar
Contact us : a9649060356@gmail.com
"""
if __name__ == "__main__":
    for _ in range(int(input())):
        lenght_of_array = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        sum = 0 # I use this um for total of all maxs
        stack = [arr[0]]
        for index in range(1,lenght_of_array):
            if stack != [] and st[-1] > arr[index]: # IS there -1 show the stack top element this is inbuilt functionality of list of python
                stack.append(arr[index])
            else:
                while (stack != []) and (stack[-1] < arr[index]):
                    sum += arr[index]
                    stack.pop()
                stack.append(arr[index])
        print(sum%1000000001)

# Coding is Game , so If you want to become good in this so learn advance algo and advance dsa that helps you a lot in write code and making a good logic.