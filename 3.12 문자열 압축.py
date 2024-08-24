def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        result = ""
        count = 1
        pre = s[0:i]
        
        for j in range(i, len(s), i):
            now = s[j:j+i]
            if pre == now:
                count += 1
            else:
                if count != 1:
                    result += str(count) + pre
                else:
                    result += pre
                pre = now
                count = 1
        
        if count != 1:
            result += str(count) + pre
        else:
            result += pre
        
        answer = min(answer, len(result))
    return answer