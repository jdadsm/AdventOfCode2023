def main():
    with open("day5/input.txt",'r') as file:
        input = file.readlines()
        
    seeds = input[0].removeprefix("seeds:").split()
    input = input[1:]
    
    maps = []
    while input:
        line = input[0].removesuffix("\n")
        input = input[1:]
        if line == "":
            continue
        if line.endswith("map:"):
            maps.append([])
        elif line[-1].isdigit():
            maps[-1].append(line.split())
    
    locations = []
    for seed in seeds:
        value = int(seed)
        for map in maps:
            for line in map:
                if value >= int(line[1]) and value < int(line[1])+int(line[2]):
                    value = int(line[0]) + value-int(line[1])
                    break
        locations.append(value)
    
    print(min(locations))
        
if __name__ == "__main__":
    main()