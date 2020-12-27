'''
Question Description :-
Jump Game IV

Given an array of integers arr, you are initially positioned at the first index of the array.
In one step you can jump from index i to index:
    i + 1 where: i + 1 < arr.length.
    i - 1 where: i - 1 >= 0.
    j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.
Notice that you can not jump outside of the array at any time.


Example 1:
    Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
    Output: 3
    Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example 2:
    Input: arr = [7]
    Output: 0
    Explanation: Start index is the last index. You don't need to jump.

Example 3:
    Input: arr = [7,6,9,6,9,6,9,7]
    Output: 1
    Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Example 4:
    Input: arr = [6,1,9]
    Output: 2

Example 5:
    Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
    Output: 3
 

Constraints:
    1) 1 <= arr.length <= 5 * 10^4
    2) -10^8 <= arr[i] <= 10^8
'''
import collections
def minJumps(arr):

    n = len(arr)
    if n == 1:
        return 0
    
    queue = collections.deque([0])
    visited = set([0])
    
    pos = collections.defaultdict(set)
    for i, num in enumerate(arr):
        pos[num].add(i)
    
    level = 0
    while len(queue)>0:
        
        for _ in range(len(queue)):
            
            node = queue.popleft()
            if node == n-1:
                return level

            nexts = [node-1, node+1] + list(pos[arr[node]])
            for i in nexts:
                if 0<=i<n and i not in visited:
                    queue.append(i)
                    visited.add(i)
            pos[arr[node]] = set()
        level += 1
    return -1

print(minJumps([7,6,9,6,9,6,9,7]))

#Reference :- https://code.dennyzhang.com/jump-game-iv 