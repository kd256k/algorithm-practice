# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/389478
# 접근: 2D 배열 구성 후 열 기준 카운

def solution(n, w, num):
    grid = []
    row = []
    
    for i in range(1, n+1):
        row.append(i)
        if len(row) == w:
            if len(grid) % 2 == 1:
                row = row[::-1]  
            grid.append(row)
            row = []
    if row:
        if len(grid) % 2 == 1:
            row = row[::-1]
            padding = w - len(row)
            row = [None] * padding + row[::-1]
        grid.append(row)
        
    for r_idx, row in enumerate(grid):
        for c_idx, val in enumerate(row):
            if val == num:
                count = 0
                for r in grid[r_idx:]:
                    if c_idx < len(r) and r[c_idx] is not None:
                        count += 1
                return count
              

