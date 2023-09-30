#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    n,m=len(matrix),len(matrix[0])
    
    rows=[False]*n
    cols=[False]*m

    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==1):
                rows[i]=True
                cols[j]=True
    
    for i in range(n):
        for j in range(m):
            if(rows[i] or cols[j]):
                matrix[i][j]=1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends