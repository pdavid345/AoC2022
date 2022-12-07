class File:
    def __init__(self,parent, name, size):
        self.parent = parent
        self.name = name
        self.size = size

class Folder:
    def __init__(self,parent, name):
        self.parent = parent
        self.name = name
        self.children = []
        self.size = None

with open('input/7') as f:
    dat = f.read().split('\n')


# Parse

root = Folder(None,'/')

head = root

for l in dat:
    tags = l.split(' ')
    # print(tags)
    if tags[0] == '$':
        # Command is happening
        if tags[1] == 'cd':

            # Change dir mode

            if tags[2] == '/':
            # change to root
                head = root
            
            elif tags[2] == '..':
                head = head.parent
            
            else:
            # go into folder
                for c in head.children:
                    if c.name == tags[2]:
                        head = c
        # no need for 'ls' if statement, it's the only other option. if tags[0] not $, then we're reading output of ls
    else:
    # we are in ls mode

        # Create list of names in current folder
        names = [i.name for i in head.children] 

        if tags[0] == 'dir':
            dirName = tags[1]            
            # check if dir has already been indexed in folder, if not then append to children list
            if dirName not in names:
                head.children.append(Folder(head,dirName))
        
        else:
        # file read
            fName = tags[1]
            if fName not in names:
                head.children.append(File(head,fName,int(tags[0])))
                


def printStructure(h):
    out = ''
    if(h.parent == None):
        out = out + '/ (dir, size ='  + str(h.size) + ')\n'

    
    for i in h.children:
        out = out + '- '+(i.name) 

        if isinstance(i,Folder):
            out = out + ' (dir, size =' + str(i.size) +')\n'
            folderOut = printStructure(i)
            lines = folderOut.split('\n')[:-1]
            for l in lines:
                out = out + '\t' + l + '\n'
        else:
            out = out + ' (file, size = '+str(i.size)+')\n'
    return out

#  Solve Problem 1

# crawl through structure, assign sizes to folders


def setSize(h):
    sizes = [c.size for c in h.children]

    # if all sizes are assigned
    if( all(s is not None for s in sizes) ):
        h.size = sum([int(sString) for sString in sizes])
    
    # else there are folders in h that are not assigned
    # print(f'folder: {h.name}')
    # print(sizes)
    for c in h.children:
        # found not assigned folder
        if c.size is None:
            c =  setSize(c)
    
    # print(f'folder: {h.name}')
    sizes = [c.size for c in h.children]
    # print(sizes)

    h.size = sum([int(sString) for sString in sizes])
    return h


# Set sizes

root = setSize(root)
# Print updated tree with folder sizes
# print(printStructure(root),'------------------------------------------\n')


# Look for small dirs, sum up values
sumSize = 0

def calcSumsPr1(head):
    sumSize = 0

    for c in head.children:
        if isinstance(c,Folder):
            if c.size <= 100000:
                sumSize = sumSize + c.size
            sumSize = sumSize + calcSumsPr1(c)

    return sumSize


print(f'Problem 1 solution: {calcSumsPr1(root)}')

# Part 2
spaceNeeded = root.size - 40000000
print(f'space needed: {spaceNeeded}')


def getSizesPr2(head):
    sizes = []
    if head.size > spaceNeeded:
        sizes.append(head.size)
    for c in head.children:
        if isinstance(c,Folder):
            for s in getSizesPr2(c):
                sizes.append(s)

    return sizes


print(f'minimum folder size: {min(getSizesPr2(root))}')