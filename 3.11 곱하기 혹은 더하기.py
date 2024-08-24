s = input()
# 0하고 1일 때 빼고는 곱하는게 좋을 듯

result = int(s[0])
for i in range(len(s)-1):
    if int(s[i]) == 0 or int(s[i]) == 1:
        result += int(s[i+1])
    else:
        result *= int(s[i+1])
print(result)