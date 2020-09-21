#C++;
"""
    Code By : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

//Problem :-Given a binary tree, find the depth of the deepest odd level leaf node in a binary tree. If there is no leaf at odd level then return 0.
//          Consider that level starts with 1. Depth of a leaf node is number of nodes on the path from root to leaf (including both leaf and root).


int depthOfOddLeafUtil(struct Node *root,int level)
{
    if(!root) 
        return 0;
    queue<Node*> q;
    level=0;
    q.push(root);
    int count=0;
    while(!q.empty()){
        int size=q.size();
        level++;
        while(size--){
            Node* temp=q.front(); q.pop();
            if(!temp->left and !temp->right and level%2==1)
            {
                count=max(count,level);
            }
            if(temp->left) q.push(temp->left);
            if(temp->right) q.push(temp->right);
        }
    }
    return count;
}
#include<bits/stdc++.h>
using namespace std;

// A utility function to find maximum of two integers
int max(int x, int y) { return (x > y)? x : y; }

// A Binary Tree node
struct Node
{
	int data;
	struct Node *left;
	struct Node *right;
	
	Node(int x){
	    data = x;
	    left = NULL;
	    right = NULL;
	}
};

// A recursive function to find depth of the deepest odd level leaf
int depthOfOddLeafUtil(struct Node *root,int level);

/* Main function which calculates the depth of deepest odd level leaf.
This function mainly uses depthOfOddLeafUtil() */
int depthOfOddLeaf(struct Node *root)
{
	int level = 1, depth = 0;
	return depthOfOddLeafUtil(root, level);
}
void insert(struct Node *root,int n1,int n2,char lr)
 {
     if(root==NULL)
        return;
     if(root->data==n1)
     {
         switch(lr)
         {
          case 'L': root->left=new Node(n2);
                    break;
          case 'R': root->right=new Node(n2);
                    break;
         }
     }
     else
     {
         insert(root->left,n1,n2,lr);
         insert(root->right,n1,n2,lr);
     }
 }
int main()
{
    /* Let us construct the tree shown in above diagram */
    int t,k;
    cin>>t;
    while(t--)
    {
    int n;
    cin>>n;
    struct Node *root=NULL;
    while(n--)
    {
        char lr;
        int n1,n2;
        cin>>n1>>n2;
        cin>>lr;
        if(root==NULL)
        {
            root=new Node(n1);
            switch(lr){
                    case 'L': root->left=new Node(n2);
                    break;
                    case 'R': root->right=new Node(n2);
                    break;
                    }
        }
        else
        {
            insert(root,n1,n2,lr);
        }
    }
    	printf("%d\n", depthOfOddLeaf(root));
	
	}
	return 0;
}
// } Driver Code Ends


// A recursive function to find depth of the deepest odd level leaf
int depthOfOddLeafUtil(struct Node *root,int level)
{
    if(!root) 
        return 0;
    queue<Node*> q;
    level=0;
    q.push(root);
    int count=0;
    while(!q.empty()){
        int size=q.size();
        level++;
        while(size--){
            Node* temp=q.front(); q.pop();
            if(!temp->left and !temp->right and level%2==1)
            {
                count=max(count,level);
            }
            if(temp->left) q.push(temp->left);
            if(temp->right) q.push(temp->right);
        }
    }
    return count;
}