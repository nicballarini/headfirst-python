hash = "#"
branches = 10

for i in range(10):
    space = ""
    for j in range(10-i,0,-1):
        space = space + " "
    print(space,hash)
    hash = hash + "##"
    
