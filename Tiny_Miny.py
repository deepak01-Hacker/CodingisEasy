#python3
"""
Code By : Deepak Kumar
Contact us : a9649060356@gmail.com

"""
#Array Medium Level Problem of GeeksForGeeks

#Q-> Find the smallest number that can be framed using the series created by the digits 
# obtained by raising the given number  (  "a"  ) to the power from 1 to  n  i.e.  a^1 , a^2 , a^3 .......a^n . We get  b1,b2 , b3 , ........... bn . 
#Using all the digits  ( including repeating ones )  that appear inb1 ,b2 , b3 .... bn . Frame a number that contains all the digits 
# ( including repeating ones )  and find out the combination of digits that make the smallest number of 
# all possible combinations. Excluding or neglecting zeroes  ( " 0 " ).


for _ in range(int(input())):
    a,n = map(int,input().split(" "))
    result = []
    for power in range(1,n+1):
        ans = a ** power
        for each_digit in str(ans):
            if each_digit != "0":
                result.append(int(each_digit))
    result.sort() #it gives the minimum formed number 
    for k in result:
        print(k,end="")
    print()