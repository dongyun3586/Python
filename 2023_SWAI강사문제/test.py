lis = [10, 90, 30, 70, 20]

for j in range(0, len(lis) - 1):
    for k in range(0, (len(lis) - 1) - j):
        if lis[k] < lis[k + 1]:
            lis[k], lis[k + 1] = lis[k + 1], lis[k]

print(lis)
