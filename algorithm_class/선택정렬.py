def InsertionSort(n, num_lst):
    count_total = 0
    count_swap = 0
    
    for i in range(1, n):
        for j in range(i, 0, -1):
            count_total += 1
            
            if num_lst[j-1] > num_lst[j]:
                count_swap += 1
                num_lst[j-1], num_lst[j] = num_lst[j], num_lst[j-1]
            else:
                break
    return count_total, count_swap
                
t = int(input())
for _ in range(t):
    data = input().split()
    n = int(data[0])
    num_lst = list(map(int, data[1:]))
    
    count_total, count_swap = InsertionSort(n, num_lst)
    print(count_total, count_swap)