def main():
    with open("day3/input.txt",'r') as file:
        input = file.readlines()
        
    sum = 0
    
    number_coordinates = set()
    gears = []
    for i in range(len(input)):
        for j in range(len(input[i])-1):
            if input[i][j] != "." and not input[i][j].isdigit():
                number_coordinates.update(check_numbers(input,i,j))
            if input[i][j] == "*":
                check,g_coords = is_a_gear(input,i,j)
                if check:
                    gears.append(g_coords)
                    
    number_coord = []   
    while number_coordinates:
        number,coords = get_number(input,number_coordinates.pop())
        number_coord.append([number,coords])
        for c in coords:
            try:
                number_coordinates.remove(c)
            except KeyError:
                pass
        sum+=number
    
    gear_ratios = 0
    
    for gear in gears:
        val = 1
        for n in number_coord:
            temp_gear = list(gear)
            for gear_coord in temp_gear:
                if gear_coord in n[1]:
                    val*=n[0]
                    #print(n[0])
                    for c in n[1]:
                        try:
                            temp_gear.remove(c)
                        except ValueError:
                            pass
        gear_ratios+=val
    
    print("Gear ratios:",gear_ratios)
    
def is_a_gear(input,i,j):
    n = 0
    u_coords = []
    if input[i+1][j+1].isdigit():
        u_coords.append((i+1,j+1))
    if input[i+1][j-1].isdigit():
        u_coords.append((i+1,j-1))
    if input[i+1][j].isdigit():
        u_coords.append((i+1,j))
    
    if len(u_coords) == 2:
        if abs(u_coords[0][1] - u_coords[1][1]) > 1:
            n+=2
        else:
            n+=1
    elif len(u_coords)!=0:
        n+=1
    
    lo_coords = []
    
    if input[i-1][j-1].isdigit():
        lo_coords.append((i-1,j-1))
    if input[i-1][j].isdigit():
        lo_coords.append((i-1,j))
    if input[i-1][j+1].isdigit():
        lo_coords.append((i-1,j+1))
        
    if len(lo_coords) == 2:
        if abs(lo_coords[0][1] - lo_coords[1][1]) > 1:
            n+=2
        else:
            n+=1
    elif len(lo_coords)!=0:
        n+=1
    
    coords = []
    
    if input[i][j+1].isdigit():
        coords.append((i,j+1))
    if input[i][j-1].isdigit():
        coords.append((i,j-1))
    
    n+=len(coords)
    
    coords.extend(u_coords)
    coords.extend(lo_coords)
    
    return n==2,coords

def get_number(input,coord):
    line = input[coord[0]]
    
    number_coords = []
    
    i = coord[1]
    while line[i].isdigit():
        number_coords.append((coord[0],i))
        i-=1
    
    i = coord[1]+1
    while line[i].isdigit():
        number_coords.append((coord[0],i))
        i+=1
    
    number_coords.sort()   
    
    number = ""
    for char in number_coords: 
        number+=input[char[0]][char[1]]
    
    return int(number),number_coords

def check_numbers(input,i,j):
    coords = []
    if input[i+1][j+1].isdigit():
        coords.append((i+1,j+1))
    if input[i+1][j-1].isdigit():
        coords.append((i+1,j-1))
    if input[i][j+1].isdigit():
        coords.append((i,j+1))
    if input[i][j-1].isdigit():
        coords.append((i,j-1))
    if input[i-1][j+1].isdigit():
        coords.append((i-1,j+1))
    if input[i-1][j-1].isdigit():
        coords.append((i-1,j-1))
    if input[i+1][j].isdigit():
        coords.append((i+1,j))
    if input[i-1][j].isdigit():
        coords.append((i-1,j))
    return coords

if __name__ == "__main__":
    main()