with open('input/2') as f:
    dat = f.read().split('\n')


lookUp = dict(zip(['A X', 'B X', 'C X','A Y', 'B Y', 'C Y','A Z', 'B Z', 'C Z'],[4,1,7,8,5,2,3,9,6]))

print(sum([lookUp[i] for i in dat]))

lookUp = dict(zip(['A X', 'B X', 'C X','A Y', 'B Y', 'C Y','A Z', 'B Z', 'C Z'],[3,1,2, 4,5,6, 8,9,7]))
print(sum([lookUp[i] for i in dat]))