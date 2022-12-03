with open('input/3') as f:
    dat = f.read().split('\n')

lookUp = dict(zip( map(chr,list(range(65,91))[:]+list(range(97,123))[:])  , list(range(27,53))[:]+list(range(1,27))[:] ) )

sol1 = sum([lookUp[set(l[0:int(len(l)/2)]).intersection(set(l[int(len(l)/2):])).pop()] for l in dat])
sol2 = sum([lookUp[set(x).intersection(set(y)).intersection(set(z)).pop()] for x, y, z in zip(*[iter(dat)]*3)])

print(sol2)
print(sol2)
    