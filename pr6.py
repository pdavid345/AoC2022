with open('input/6') as f:
    dat = f.read()

# dat = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

for i in range(len(dat)):
    if(len(set(dat[i:i+4])) == 4):
        print(i+4)
        break


for i in range(len(dat)):
    if(len(set(dat[i:i+14])) == 14):
        print(i+14)
        break