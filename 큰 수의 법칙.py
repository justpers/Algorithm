N, M, K = map(int, input().split())
num_array = input().split()
num_array = list(map(int, num_array))

num_array.sort()
max = num_array[N-1]
second_max = num_array[N-2]

count = 0
sum = 0
while count < M:
    for _ in range(K):
        sum += max
        count += 1
    sum += second_max
    count+= 1
print(sum)