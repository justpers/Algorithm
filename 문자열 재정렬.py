s = input()

string = ''
num_sum = 0
for i in range(len(s)):
    if int(ord(s[i])) >= int(ord('A')):
        string += s[i]
    else:
        num_sum += int(s[i])
        
print(''.join(sorted(string)), num_sum, sep='')