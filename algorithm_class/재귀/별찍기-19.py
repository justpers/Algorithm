def make_star(n, start_row, start_col, star_length, arr):
    if n == 1:
        arr[start_row][start_col] = '*'
        return
    length = 1 + 4*(n-1)
    end_row = start_row + length - 1
    end_col = start_col + length - 1
    
    for i in range(start_col, end_col + 1):
        arr[start_row][i] = '*'
        arr[end_row][i] = '*'
        
    for i in range(start_row, end_row + 1):
        arr[i][start_col] = '*'
        arr[i][end_col] = '*'
        
    make_star(n - 1, start_row + 2, start_col + 2, star_length, arr)

n = int(input())
star_length = 1 + 4*(n-1)
arr = [[' '] * star_length for _ in range(star_length)]

make_star(n, 0, 0, star_length, arr)

for row in arr:
    print(''.join(row))
    