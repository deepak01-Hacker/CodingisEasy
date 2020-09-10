#Python3
"""
    Code By     : Deepak Kumar
    Contact us  : a9649060356@gmail.com
    Logic       : GeeksForGeeks 
"""


#Problem :-> using Frequency and heap print k maximum frequency element
#Tags : Medium , Priority - Queue , Array,Map,Hash ,sort




def kStream(arr,k):
    
    top = [0 for _ in range(k+1)]

    map = {i:0 for i in range(k+1)}
    for i in arr:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
        top[k] = i
        index = top.index(i)
        index -= 1

        while(index>=0):
            if map[top[index]] < map[top[index+1]]:
                t = top[index]
                top[index] = top[index+1]
                top[index+1] = t
            elif map[top[index]] == map[top[index+1]] and top[index] > top[index+1]:
                t = top[index]
                top[index] = top[index+1]
                top[index+1] = t
            else:
                break
            index -= 1
        index = 0
        while (index < k and top[index] != 0):
            print(top[index],end=" ")
            index += 1
    print()


if __name__ == "__main__":
    for _ in range(1):
        n = 5
        arr = [5,2,1,3,2]
        k = 4
        kStream(arr,k)

#Happy Coding ; ) 
