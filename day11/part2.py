
def main():
    with open("day11/input.txt",'r') as file:
        input = [line.removesuffix("\n") for line in file.readlines()]
    
    EXPAND_N = 1000000
    galaxies,rows,columns = expand_galaxies(input)
    coords,galaxies = numerate_galaxies(galaxies)
    pairs = [(i, j) for i in range(0, len(coords)) for j in range(i, len(coords) ) if i!=j]
    distances = [manhattan_distance2(coords[pair[0]],coords[pair[1]],rows,columns,EXPAND_N-2) for pair in pairs]
    
    print(sum(distances))

def manhattan_distance(pair1,pair2):
    return abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1])

def manhattan_distance2(pair1,pair2,rows,columns,x):
    r1,r2 = pair1[0],pair2[0]
    if pair1[0] > pair2[0]:
        r1,r2 = r2,r1
    c1,c2 = pair1[1],pair2[1]
    if pair1[1] > pair2[1]:
        c1,c2 = c2,c1
    add = 0
    if r1 < r2:
        for row in rows:
            if row > r1 and row < r2:
                add+=x
    if c1 < c2:
        for col in columns:
            if col > c1 and col < c2:
                add+=x
    return abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1]) + add

def numerate_galaxies(galaxies):
    coords = []
    size1 = len(galaxies)
    size2 = len(galaxies[0])
    for i in range(size1):
        for j in range(size2):
            if galaxies[i][j] == "#":
                coords.append((i,j))
    return coords,galaxies

def expand_galaxies(input):
    galaxies = []
    rows = []
    added_lines = 0
    for i in range(len(input)):
        if all(val == "." for val in input[i]):
            rows.append(i+added_lines)
            added_lines+=1
            galaxies.append(input[i])
        galaxies.append(input[i])
    
    columns_to_duplicate = [col_idx for col_idx, col in enumerate(zip(*galaxies)) if all(elem == '.' for elem in col)]
    columns_to_duplicate = [(columns_to_duplicate[i]+i) for i in range(len(columns_to_duplicate))]
    input = list(galaxies)
    for row_index in range(len(input)):
        for column_index in columns_to_duplicate:
            galaxies[row_index] = galaxies[row_index][:column_index] + "." + galaxies[row_index][column_index:]
    return galaxies,rows,columns_to_duplicate
    

if __name__ == "__main__":
    main()