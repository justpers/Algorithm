def SelectionSort(n, num_lst):
    count_total = 0
    count_swap = 0
    
    for i in range(n):
        min = i
        for j in range(i+1, n):
            count_total += 1
            
            if num_lst[j] < num_lst[min]:
                min = j
        if i != min:
            count_swap += 1
            tmp = num_lst[i]
            num_lst[i] = num_lst[min]
            num_lst[min] = tmp
    return count_total, count_swap

t = int(input())
for _ in range(t):
    data = input().split()
    n = int(data[0])
    num_lst = list(map(int, data[1:]))
    
    count_total, count_swap = SelectionSort(n, num_lst)
    print(count_total, count_swap)