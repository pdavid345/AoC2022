with open('input/5') as f:
    datin = f.read()
dat = datin.split('\n')
rows = [l[1:-1:4] for l in dat[0:8]]

# print(rows)

stacks  = ['' for x in range(9)]


for i in range(len(rows)-1,-1,-1):
    for c in range(9):
        if(rows[i][c] != ' '):
            stacks[c] = stacks[c] + (rows[i][c])

for i in stacks:
    print(i)

import regex as re

comms = re.findall('move (\d+) from (\d+) to (\d+)',datin)

for comm in comms:
    nMove = int(comm[0])
    idx1 = int(comm[1])-1
    idx2 = int(comm[2])-1
    # 
    # print(f'Moving {nMove} from {idx1} to {idx2}')
    if(nMove == len(stacks[idx1])):
        Lifted = stacks[idx1][::-1]
    else:
        Lifted = stacks[idx1][: len(stacks[idx1])-nMove -1 :-1 ]

    stacks[idx1] = stacks[idx1][0:len(stacks[idx1])-nMove] 
    stacks[idx2] = stacks[idx2] + Lifted

    # print(f'Lifted {Lifted}')

    # print('\nafter: \n')
    # for i in range(len(stacks)):
    #     print(i, stacks[i])
print('\n last items: \n')
sol = ''
for i in stacks:
    if len(i) > 0:
        sol = sol+i[-1]
print(sol)

print('\nafter: \n')
for i in range(len(stacks)):
    print(i, stacks[i])

#  Part 2
#  Reinitialize Stacks
stacks = ['' for x in range(9)]
for i in range(len(rows)-1,-1,-1):
    for c in range(9):
        if(rows[i][c] != ' '):
            stacks[c] = stacks[c] + (rows[i][c])

for comm in comms:
    nMove = int(comm[0])
    idx1 = int(comm[1])-1
    idx2 = int(comm[2])-1
    # 
    # print(f'Moving {nMove} from {idx1} to {idx2}')
    if(nMove == len(stacks[idx1])):
        Lifted = stacks[idx1]
    else:
        Lifted = stacks[idx1][len(stacks[idx1])-nMove : ]

    stacks[idx1] = stacks[idx1][0:len(stacks[idx1])-nMove] 
    stacks[idx2] = stacks[idx2] + Lifted

    # print(f'Lifted {Lifted}')

    # print('\nafter: \n')
    # for i in range(len(stacks)):
    #     print(i, stacks[i])

print('\nafter: \n')
for i in range(len(stacks)):
    print(i, stacks[i])   

print('\n last items: \n')
sol = ''
for i in stacks:
    if len(i) > 0:
        sol = sol+i[-1]
print(sol)