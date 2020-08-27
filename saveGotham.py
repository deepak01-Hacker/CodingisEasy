for _ in range(1):
    n = 9
    arr = [112 ,133 ,161 ,311 ,122 ,512 ,1212, 0 ,19212]
    mins = [0,0]
    sum = 0
    st = [arr[0]]
    for i in range(1,n):
        if st != [] and st[-1] > arr[i]:
            st.append(arr[i])
        else:
            while (st != []) and (st[-1] < arr[i]):
                sum += arr[i]
                st.pop()
            st.append(arr[i])
    print(sum%1000000001)