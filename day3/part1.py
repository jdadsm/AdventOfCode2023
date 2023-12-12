def main():
    with open("day3/input.txt",'r') as file:
        input = file.readlines()
        
    sum = 0
    
    number_coordinates = set()
    for i in range(len(input)):
        for j in range(len(input[i])-1):
            if input[i][j] != "." and not input[i][j].isdigit():
                number_coordinates.update(check_numbers(input,i,j))
                
    while number_coordinates:
        number,coords = get_number(input,number_coordinates.pop())
        for c in coords:
            try:
                number_coordinates.remove(c)
            except KeyError:
                pass
        sum+=number
        
    print("Sum:",sum)

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