import collections
def numIslands(grid):
    num=0
    m=len(grid)
    if m==0:
        return 0
    n=len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]=="1":
                bfs(grid,i,j,m,n)
                num=num+1
    return num

def bfs(grid,i,j,m,n):
    dir=[[-1,0],[0,-1],[0,1],[1,0]]
    queue=collections.deque([[i,j]])
    while(queue):
        t=queue.popleft()
        for i in range(4):
            x=t[0]+dir[i][0]
            y=t[1]+dir[i][1]
            if(x>=0)and(y>=0)and(x<m)and(y<n)and(grid[x][y]=="1"):
                grid[x][y]="0"
                queue.append([x,y])      

if __name__=="__main__":
    #grid=[["1"]]
    grid=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    #grid=["11000","11000","00100","00011"]
    ans=numIslands(grid)
    print ans
