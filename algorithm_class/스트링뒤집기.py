t = int(input())
for _ in range(t):
    s = input()
    length = len(s)
    
    s_lst = list(s)
    for i in range(length // 2):
        s_lst[i], s_lst[length-1 - i] = s_lst[length-1 - i], s_lst[i]
        
    result = ''.join(s_lst)
    print(result)