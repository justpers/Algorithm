n = input()

point = len(n) / 2

left_sum = 0
right_sum = 0

for i in range(len(n)):
    if i < point:
        left_sum += int(n[i])
    else:
        right_sum += int(n[i])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')