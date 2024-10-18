# 펠린드롬 판별 & recursion 함수를 몇 번 호출하는지 count

def is_palindrome(s, cnt):
    return recursion(s, 0, len(s) - 1, cnt)

def recursion(s, left, right, cnt):
    cnt[0] += 1
    if left >= right:
        return 1
    elif s[left] != s[right]:
        return 0
    else:
        return recursion(s, left + 1, right - 1, cnt)

t = int(input())
for _ in range(t):
    s = input()
    cnt = [0]
    
    palindrome = is_palindrome(s, cnt)
    # 회문이면 1, 아니면 0
    print(palindrome, cnt[0])