with open('input/1') as f:
    dat = f.read().split('\n\n')


maxSum = 0
for l in dat:
    maxSum = max([(sum([int(i) for i in l.split('\n')])),maxSum])

print(f'Part 1: {maxSum}')
