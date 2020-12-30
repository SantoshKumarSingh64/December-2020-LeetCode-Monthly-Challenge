'''
Question Description :-
Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton
devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: 
live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors 
(horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
        Any live cell with fewer than two live neighbors dies as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


Example 1:
          0  |  1  |   0             0  |  0  |  0
          ---------------            --------------
          0  |  0  |   1             1  |  0  |  1
          ---------------     -->    --------------
          1  |  1  |   1             0  |  1  |  1
          ---------------            --------------
          0  |  0  |   0             0  |  1  |  0

    Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
    1  |  1          1  |  1        
    -------   -->    -------
    1  |  0          1  |  1

    Input: board = [[1,1],[1,0]]
    Output: [[1,1],[1,1]]
 

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 25
    board[i][j] is 0 or 1.
 

Follow up:
1) Could you solve it in-place? Remember that the board needs to be updated simultaneously: 
   You cannot update some cells first and then use their updated values to update other cells.
2) In this question, we represent the board using a 2D array. In principle, the board is infinite, 
   which would cause problems when the active area encroaches upon the border of the array 
   (i.e., live cells reach the border). How would you address these problems?
'''
def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])
    next = [[0 for x in range(n)]for y in range(m)]

    dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

    for i in range(m):
        for j in range(n):
            countLive = 0
            for x,y in dir:
                x += i
                y += j
                if 0<= x < m and 0<= y < n and board[x][y] == 1:
                    countLive += 1
            if board[i][j] == 0 and countLive == 3:
                next[i][j] = 1
            elif board[i][j] == 1 and 2 <= countLive <= 3:
                next[i][j] = 1
    for x in range(m):
        for y in range(n):
            board[x][y] = next[x][y]
    
    return board

print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))

#Reference :- https://www.youtube.com/watch?v=YZ-W5DrKPQ0