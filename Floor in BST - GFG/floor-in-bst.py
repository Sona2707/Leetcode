#User function Template for python3

class Solution:
    def floor(self, root, x):
        floorValue = -1  # Initialize with a default value

        while root:
            if root.data == x:
                # If the current node's data is equal to x, it's the floor
                return x
            elif root.data < x:
                # If the current node's data is less than x, it could be the floor
                floorValue = root.data
                root = root.right  # Check the right subtree for a potentially larger floor
            else:
                # If the current node's data is greater than x, move to the left subtree
                root = root.left

        return floorValue


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends