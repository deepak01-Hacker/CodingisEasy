//c++

/*
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

*/

// Problem :- Given a string which includes characters a, b, c, ..., z. Where value of a=1, b=2, ..., z=26. 
//            Now find the largest increasing sub sequence in the string and print it's length.
//            Note:  Sub sequence doesn't require elements to be consecutively increasing.

/*Example:
    Input:
        2
        pcbhdbjcvhjsdjhvczvd
        abcdapzfqh

    Output:
        7
        6

*/

#include <iostream>
using namespace std;

int main() {
    int t,length,i,j ;
    int maxs;
    cin>>t;
    while(t){
        string s;
        cin>>s;
        length = s.size();
        maxs = -1;
        int dp[length+1];
        for(i=0;i<length;++i){
            dp[i] = 0;
        }
        dp[0] = 1;
        for (i=1;i<length;++i){
            dp[i] = 1;
            int a = s[i];
            for (j=0;j<i;++j){
                int b = s[j];
                if((b<a) && (dp[i] <= dp[j])){
                    dp[i] = 1 + dp[j];
                }
                maxs = max(maxs,dp[i]);
            }
        }
        cout<<maxs<<endl;
        --t;
    }
	return 0;
}