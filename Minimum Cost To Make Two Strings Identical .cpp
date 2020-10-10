//C++

/*
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
*/

//Problem :- Given two strings X and Y, and two values costX and costY, the task is to find the minimum cost 
//           required to make the given two strings identical. You can delete characters from both the strings. 
//           The cost of deleting a character from string X is costX and from Y is costY. The cost of removing 
//           all characters from a string is the same.


//Example :- 
/*
    Input: X = "abcd", Y = "acdb", costX = 10 costY = 20.
    Output: 30
    Explanation: For Making both strings 
        identical we have to delete character 
        'b' from both the string, hence cost 
        will be = 10 + 20 = 30.
*/

// Hint :- Use LCS(Longest Common SubSequence) Happy Coding ;)


int dp[1001][1001];
class Solution{

	public:
	int findMinCost(string X, string Y, int costX, int costY)
	{
	    int i,j;
	    int len_string1 = X.size();
	    int len_string2 = Y.size();
	    for(i=0;i<=len_string1;i++){
	        dp[i][0] = 0;
	    }
	    for(j=0;j<=len_string2;j++){
	        dp[0][i] = 0;
	    }
	    for(i=1;i<=len_string1;i++){
	        for(j=1;j<=len_string2;j++){
	            if (X[i-1] == Y[j-1]){
	                dp[i][j] = 1+dp[i-1][j-1];
	            }
	            else{
	                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
	            }
	        }
	    }
	    int st_1 = costX * (len_string1-dp[len_string1][len_string2]);
	    int st_2 = costY * (len_string2-dp[len_string1][len_string2]);
	    return st_1+st_2;
	    
	    
	}
  

};