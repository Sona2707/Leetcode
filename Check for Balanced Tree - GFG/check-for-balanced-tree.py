#User function Template for python3


'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self, root):
        def checkBalance(node):
            if node is None:
                return 0
            
            left_height = checkBalance(node.left)
            if left_height == -1:
                return -1
            
            right_height = checkBalance(node.right)
            if right_height == -1:
                return -1
            
            return -1 if abs(left_height - right_height) > 1 else 1 + max(left_height, right_height)
        
        return checkBalance(root) != -1





#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        if ob.isBalanced(root):
            print(1) 
        else:
            print(0)
# } Driver Code Ends