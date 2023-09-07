#User function Template for python3

from typing import List

from collections import deque

class Solution:
    def minimumMultiplications(self, arr, start, end):
        level = 0
        queue = deque()
        visited = [False] * 100001
        
        queue.append(start)
        visited[start] = True
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                current = queue.popleft()
                
                if current == end:
                    return level
                
                for number in arr:
                    newStart = (current * number) % 100000
                    if not visited[newStart]:
                        queue.append(newStart)
                        visited[newStart] = True
            
            level += 1
        
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends