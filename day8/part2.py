import math

def main():
    with open("day8/input.txt",'r') as file:
        input = file.readlines()
    
    instructions = input[0].removesuffix("\n")
    size = len(instructions)
    input = input[2:]
    
    left = []
    right = []
    starting_nodes = []
    
    for line in input:
        line = line.removesuffix("\n").split(" = ")
        left.append(line[0])
        right.append(line[1].removeprefix("(").removesuffix(")").split(", "))
        if line[0].endswith("A"):
            starting_nodes.append(line[0])
    
    multiples = []
    for i in range(len(starting_nodes)):
        multiples.append(find_pattern(starting_nodes[i],left,right,instructions))
        
    res = multiples[0]
    for m in multiples[1:]:
        res = lcm(res,m)
        
    print(res*size)
    
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def find_pattern(starting_node,left,right,instructions):
    z_nodes = []
    z_counter = []
    repetitions = []
    
    curr_repetition = 0
    while 2 not in z_counter:
        curr_repetition+=1
        for instruction in instructions:
            if instruction=="L":
                index = left.index(starting_node)
                starting_node = right[index][0]
            else:
                index = left.index(starting_node)
                starting_node = right[index][1]
        if starting_node.endswith("Z"):
            if starting_node in z_nodes:
                index = z_nodes.index(starting_node)
                z_counter[index]+=1
                repetitions[index].append(curr_repetition)
            else:
                z_nodes.append(starting_node)
                z_counter.append(1)
                repetitions.append([curr_repetition])
    index = z_counter.index(2)
    return repetitions[index][0]

        
if __name__ == "__main__":
    main()