with open('input/1') as f:
    dat = f.read().split('\n\n')


maxSum = 0
for l in dat:
    maxSum = max([(sum([int(i) for i in l.split('\n')])),maxSum])

print(f'Part 1: {maxSum}')

sums = []
for l in dat:
    sums.append((sum([int(i) for i in l.split('\n')])))

sums.sort()
print(f'Part 2: {sum(sums[-3:])}')