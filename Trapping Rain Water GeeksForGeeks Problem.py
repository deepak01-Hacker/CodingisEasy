"""
Code By : Deepak kumar
Contact us : a9649060356@gmail.com
"""
#Python is My favourite but it is Not best
#Some Time this Question Give TLE error but You can use this Code for your Hint
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().rstrip().split(" ")))
    st = [] # we use stack in this Question Bcz using stack we find rightmost greater in this
    maxs = 0
    for item in reversed(arr):
        if item > maxs:
            maxs = i
        st.append(maxs)
    maxs_blocks = 0
    area = 0
    for index in range(n):
        if arr[index] < maxs_blocks and arr[index]<st[-1]:
            area += min(st[-1],maxs_blocks)- arr[index]
        else:
            maxs_blocks = arr[index]
        st.pop()
    print(area)