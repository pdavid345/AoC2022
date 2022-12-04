import regex as re
with open('input/4') as f:
    dat = f.read()

matches = [[int(j) for j in m] for m in re.findall('(\d+)-(\d+),(\d+)-(\d+)',dat)]

def contains(l):
    return ((l[0] <= l[2] and l[1] >= l[3]) or (l[2] <= l[0] and l[3] >= l[1]))

def overlaps(l):
    A = set(range(l[0],l[1]+1))
    B = set(range(l[2],l[3]+1))
    return (len(A.intersection(B)) > 0)



print(sum(map(contains,matches)))


print(sum(map(overlaps,matches)))
