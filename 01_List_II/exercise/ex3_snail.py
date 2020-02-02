def sel_min(ary):
    minX, minY= 0, 0
    min = 99
    for i in range(5):
        for j in range(5):
            if min > ary[i][j]:
                min = ary[i][j]
                minX, minY =i, j
    ary[minX][minY] = 99
    return min

ary = [ [ 9, 20, 2, 18, 11 ],
	[ 19, 1, 25, 3, 21 ],
	[ 8, 24, 10, 17, 7 ],
	[ 15, 4, 16, 5, 6 ],
	[ 12, 13, 22, 23, 14 ] ]

sorted_ary = [[0  for _ in range(6)] for _ in range(6)]
cur_min = -1
X, Y = 0, 0
newX, newY = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir_stat = 0  # 0:왼쪽, 1:아래, 2:오른쪽, 3:위

for i in range(25):
    cur_min = sel_min(ary)
    X, Y = newX, newY
    sorted_ary[Y][X] = cur_min
    newX = X + dx[dir_stat]
    newY = Y + dy[dir_stat]

    if sorted_ary[newY][newX] != 0 or newY > 4 or newX > 4 or newY < 0 or newX < 0:
        dir_stat =(dir_stat + 1) % 4
        newX = X + dx[dir_stat]
        newY = Y + dy[dir_stat]

#출력
for i in range(5):
    for j in range(5):
        print(sorted_ary[i][j], end=" ")
    print()