//c++

/*
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
*/

#TAgS : Dynamic Programming , Array , C++ 

//Problem :- The first line of input contains an integer T denoting the no of test cases . 
//           Then T test cases follow. Each test case contains 3 lines . The first line of 
//           each test case is an integer N denoting the size of the array A. In the next line 
//           are N space separated values of the array A. In the next line is an integer x.


#include <iostream>
#include <algorithm>
using namespace std;

int pairsSum(int arr[],int n,int k){
    
    int res=0;
    int i = n-1;
    while(i>0){
        
        if (arr[i]-arr[i-1] < k){
            res += arr[i];
            res += arr[i-1];
            i = i-1;
        }
        i = i-1;
    }
    return res;
}

int main() {
	int t;
	cin>>t;
	while(t>0){
	    int n;
	    cin>>n;
	    int arr[n];
	    for (int i=0;i<n;i++){
	        cin>>arr[i];
	    }
	    int k;
	    cin>>k;
	    sort(arr,arr+n);
	    int result = pairsSum(arr,n,k) ;
	    cout<<result<<endl;
	    t = t-1;
	}
	return 0;
}