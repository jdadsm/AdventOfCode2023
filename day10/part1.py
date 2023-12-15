def main():
    with open("day10/input.txt",'r') as file:
        input = file.readlines()
        
    for i in range(len(input)):
        input[i] = input[i].removesuffix("\n")
    
    starting_point = get_starting_point(input)
    
    possible_tiles = ['|','-','L','F','J','7']
    
    for tile in possible_tiles:
        check,res = is_main_loop(input,starting_point,tile)
        if check:
            print(tile)
            print(res)
            break
        
def is_main_loop(input,starting_point,tile):
    #input[starting_point[0]][starting_point[1]] = tile
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
    path1 = [starting_point,first1]
    path2 = [starting_point,first2]
    while path1[-1] != path2[-1] and path1[-1] != None and path2[-1] != None:
        path1.append(get_next_point(input,path1[-2],path1[-1]))
        path2.append(get_next_point(input,path2[-2],path2[-1]))
    
    print(tile)
    print(path1)
    print(path2)    
    
    if path1[-1] != None and path2[-1] != None:
        return True,len(path1)-1
    return False,None
    
# last 1,1
# curr 2,1
# next 3,1
# diff 1,0
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
    size = len(input)
    
    for i in range(size):
        for j in range(size):
            if input[i][j] == "S":
                return i,j

if __name__ == "__main__":
    main()