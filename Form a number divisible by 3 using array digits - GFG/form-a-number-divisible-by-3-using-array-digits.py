#User function Template for python3

class Solution:
    def digitsum(self, n):
        sum = 0
        while n > 0:
            sum += n % 10
            n = n // 10
        return sum

    def isPossible(self, N, arr):
        sum = 0
        for i in range(N):
            sum += self.digitsum(arr[i])
        return 1 if sum % 3 == 0 else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends