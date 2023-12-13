def main():
    with open("day8/input.txt",'r') as file:
        input = file.readlines()
    
    instructions = input[0].removesuffix("\n")
    size = len(instructions)
    input = input[2:]
    
    left = []
    right = []

    for line in input:
        line = line.removesuffix("\n").split(" = ")
        left.append(line[0])
        right.append(line[1].removeprefix("(").removesuffix(")").split(", "))
        
    steps = 0
    
    node="AAA"
    while node != "ZZZ":
        for instruction in instructions:
            steps+=1
            if instruction=="L":
                index = left.index(node)
                node = right[index][0]
            else:
                index = left.index(node)
                node = right[index][1]
            #print(node)
        
    print(steps)
        
if __name__ == "__main__":
    main()