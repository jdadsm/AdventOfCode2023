def main():
    with open("day10/input.txt",'r') as file:
        input = file.readlines()
        
    for i in range(len(input)):
        input[i] = input[i].removesuffix("\n")
    
    starting_point = get_starting_point(input)
    
    possible_tiles = ['|','-','L','F','J','7']
    
    loop = set()
    for tile in possible_tiles:
        check,loop = is_main_loop(input,starting_point,tile)
        if check:
            input[starting_point[0]] = input[starting_point[0]].replace("S",tile)
            break
    
    input = clean_input(input,loop)
            
    enclosed_tiles = get_enclosed_tiles(input,loop)
    
    print(len(enclosed_tiles))
    
def clean_input(input,loop):
    size1 = len(input)
    size2 = len(input[0])
    for i in range(size1):
        for j in range(size2):
            if (i,j) not in loop:
                temp = list(input[i])
                temp[j] = "."
                input[i] = "".join(temp)
    return input

def get_enclosed_tiles(input,loop):
    size1 = len(input)
    size2 = len(input[0])
    groups = []
    for i in range(size1):
        #print(i)
        for j in range(size2):
            #print(j)
            if input[i][j] == ".":
                if not is_in_groups(groups,i,j):
                    group = get_ground_groups(input,i,j,[(i,j)])
                    groups.append([group,None]) 
    for i in range(len(groups)):
        groups[i][0] = groups[i][0]
        
    starting_point = None
    for i in range(size1):
        for j in range(size2):
            if (i,j) in loop:
                starting_point = (i,j)
                break
        if starting_point:
            break
    
    groups = get_defined_groups(input,starting_point,groups,loop)
    
    enclosed_tiles = []
    for group in groups:
        if group[1] == "INSIDE":
            enclosed_tiles.extend(group[0])
    
    return enclosed_tiles

def get_defined_groups(input,sp,groups,loop):
    inside = ["right"]
    size1 = len(input)
    size2 = len(input[0])
    index = loop.index(sp)
    
    loop = loop[index:-1]+loop[:index]
    
    for index in range(len(loop)-1):
        (i,j) = loop[index]
        if inside[0] == "right":
            if j+1 < size2:
                if input[i][j+1] == ".":
                    groups = alter_group(i,j+1,groups)
        elif inside[0] == "left":
            if j-1 > 0:
                if input[i][j-1] == ".":
                    groups = alter_group(i,j-1,groups)
        elif inside[0] == "up":
            if i-1 > 0:
                if input[i-1][j] == ".":
                    groups = alter_group(i-1,j,groups)
        elif inside[0] == "down":
            if i+1 < size1:
                if input[i+1][j] == ".":
                    groups = alter_group(i+1,j,groups)
        if len(inside) == 2:
            if inside[1] == "top-left":
                if input[i-1][j-1] == ".":
                    groups = alter_group(i-1,j-1,groups)
            elif inside[1] == "top-right":
                if input[i-1][j+1] == ".":
                    groups = alter_group(i-1,j+1,groups)
            elif inside[1] == "down-left":
                if input[i+1][j-1] == ".":
                    groups = alter_group(i+1,j-1,groups)
            elif inside[1] == "down-right":
                if input[i+1][j+1] == ".":
                    groups = alter_group(i+1,j+1,groups)
        inside = change_inside_prespective(input,i,j,loop[index+1],inside)
        
    return groups
        
def change_inside_prespective(input,i,j,next,inside):
    tile = input[i][j]
    diff = [next[0]-i,next[1]-j]
    if tile == "|":
        return inside
    elif tile == "-":
        return inside
    elif tile in "F":
        if inside[0] in ["right","down"]:
            if diff == [0,1]:
                inside = ["down"]
            elif diff == [1,0]: 
                inside = ["right"]
        elif inside[0] in ["top","left"]:
            if diff == [0,1]:
                inside = ["top"]
            elif diff == [1,0]: 
                inside = ["left"]
            inside.append("top-left")
    elif tile in "J":
        if inside[0] in ["right","down"]:
            if diff == [0,-1]:
                inside = ["down"]
            elif diff == [-1,0]: 
                inside = ["right"]
            inside.append("down-right")
        elif inside[0] in ["top","left"]:
            if diff == [0,-1]:
                inside = ["top"]
            elif diff == [-1,0]: 
                inside = ["left"]
    elif tile in "7":
        if inside[0] in ["right","top"]:
            if diff == [0,-1]:
                inside = ["top"]
            elif diff == [1,0]: 
                inside = ["right"]
            inside.append("top-right")
        elif inside[0] in ["left","down"]:
            if diff == [0,-1]:
                inside = ["down"]
            elif diff == [1,0]: 
                inside = ["left"]
    elif tile in "L":
        if inside[0] in ["right","top"]:
            if diff == [0,1]:
                inside = ["top"]
            elif diff == [-1,0]: 
                inside = ["right"]
        elif inside[0] in ["left","down"]:
            if diff == [0,1]:
                inside = ["down"]
            elif diff == [-1,0]: 
                inside = ["left"]
            inside.append("down-left")    
            
    return inside

def alter_group(i,j,groups):
    for index in range(len(groups)):
        if groups[index][1] == None:
            if (i,j) in groups[index][0]:
                groups[index] = [groups[index][0],"INSIDE"]
                return groups
    return groups
    
def is_in_groups(groups,i,j):
    #print(groups)
    for group in groups:
        if (i,j) in group[0]:
            return True
    return False  
    
def get_ground_groups(input,i,j,group):
    #print(group)
    size1 = len(input)
    size2 = len(input[0])
    group = []
    queue = [(i, j)]

    while queue:
        x, y = queue.pop(0)
        if (x, y) in group:
            continue
        if x < 0 or x >= size1 or y < 0 or y >= size2 or input[x][y] != ".":
            continue
        group.append((x, y))
        queue.extend([(x+1, y+1), (x+1, y), (x+1, y-1), (x, y+1), (x, y-1), (x-1, y+1), (x-1, y), (x-1, y-1)])

    return group
        
        
def is_main_loop(input,starting_point,tile):
    first1 = [starting_point[0],starting_point[1]]
    first2 = [starting_point[0],starting_point[1]]
    if tile == "|":
        first1[0] += 1
        first2[0] -= 1
    elif tile == "-":
        first1[1] += 1
        first2[1] -= 1
    elif tile == "J":
        first1[0] -= 1
        first2[1] -= 1
    elif tile == "L":
        first1[0] -= 1
        first2[1] += 1
    elif tile == "7":
        first1[0] += 1
        first2[1] -= 1
    elif tile == "F":
        first1[0] += 1
        first2[1] += 1
    path1 = [starting_point,tuple(first1)]
    path2 = [starting_point,tuple(first2)]
    while path1[-1] != path2[-1] and path1[-1] != None and path2[-1] != None:
        path1.append(get_next_point(input,path1[-2],path1[-1]))
        path2.append(get_next_point(input,path2[-2],path2[-1]))  
    
    if path1[-1] != None and path2[-1] != None:
        path2.reverse()
        path1.extend(path2[1:])
        path1.append(path1[0])
        return True,path1
    return False,None
    
def get_next_point(input,last_point,current_point):
    current_tile = input[current_point[0]][current_point[1]]
    diff = current_point[0]-last_point[0],current_point[1]-last_point[1]
    if path_is_possible(input,last_point,current_point,diff):
        if current_tile == '|':
            return (current_point[0]+diff[0],current_point[1]+diff[1])
        elif current_tile == '-':
            return (current_point[0]+diff[0],current_point[1]+diff[1])
        elif current_tile == 'L':
            if diff == (1,0):
                return (current_point[0],current_point[1]+1)
            elif diff == (0,-1):
                return (current_point[0]-1,current_point[1])
        elif current_tile == '7':
            if diff == (-1,0):
                return (current_point[0],current_point[1]-1)
            elif diff == (0,1):
                return (current_point[0]+1,current_point[1])
        elif current_tile == 'F':
            if diff == (-1,0):
                return (current_point[0],current_point[1]+1)
            elif diff == (0,-1):
                return (current_point[0]+1,current_point[1])
        elif current_tile == 'J':
            if diff == (1,0):
                return (current_point[0],current_point[1]-1)
            elif diff == (0,1):
                return (current_point[0]-1,current_point[1])

def path_is_possible(input,last_point,current_point,diff):
    last_tile = input[last_point[0]][last_point[1]]
    current_tile = input[current_point[0]][current_point[1]]
    if current_tile == '|':
        if diff == (1,0):
            if last_tile in ['-','J','L']:
                return False
        elif diff == (-1,0):
            if last_tile in ['-','F','7']:
                return False
    elif current_tile == '-':
        if diff == (0,1):
            if last_tile in ['|','J','7']:
                return False
        elif diff == (0,-1):
            if last_tile in ['|','F','L']:
                return False
    elif current_tile == 'L':
        if diff == (1,0):
            if last_tile in ['-','J','L']:
                return False
        elif diff == (0,-1):
            if last_tile in ['|','F','L']:
                return False
    elif current_tile == '7':
        if diff == (-1,0):
            if last_tile in ['-','F','7']:
                return False
        elif diff == (0,1):
            if last_tile in ['|','J','7']:
                return False
    elif current_tile == 'F':
        if diff == (-1,0):
            if last_tile in ['-','F','7']:
                return False
        elif diff == (0,-1):
            if last_tile in ['|','F','L']:
                return False
    elif current_tile == 'J':
        if diff == (1,0):
            if last_tile in ['-','J','L']:
                return False
        elif diff == (0,1):
            if last_tile in ['|','J','7']:
                return False
    return True
    
def get_starting_point(input):
    size1 = len(input)
    size2 = len(input[0])
    
    for i in range(size1):
        for j in range(size2):
            if input[i][j] == "S":
                return i,j

if __name__ == "__main__":
    main()