
def main():
    with open("day11/input.txt",'r') as file:
        input = [line.removesuffix("\n") for line in file.readlines()]
        
    coords,galaxies = numerate_galaxies(expand_galaxies(input))
    pairs = [(i, j) for i in range(0, len(coords)) for j in range(i, len(coords) ) if i!=j]
    distances = [manhattan_distance(coords[pair[0]],coords[pair[1]]) for pair in pairs]
    
    print(sum(distances))

def manhattan_distance(pair1,pair2):
    return abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1])

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
    for i in range(len(input)):
        if all(val == "." for val in input[i]):
            galaxies.append(input[i])
        galaxies.append(input[i])
    
    columns_to_duplicate = [col_idx for col_idx, col in enumerate(zip(*galaxies)) if all(elem == '.' for elem in col)]
    columns_to_duplicate = [(columns_to_duplicate[i]+i) for i in range(len(columns_to_duplicate))]
    input = list(galaxies)
    for row_index in range(len(input)):
        for column_index in columns_to_duplicate:
            galaxies[row_index] = galaxies[row_index][:column_index] + "." + galaxies[row_index][column_index:]
    return galaxies
    

if __name__ == "__main__":
    main()