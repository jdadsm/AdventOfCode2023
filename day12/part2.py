def transform_input(input):
    first = []
    second = []
    for line in input:
        line = line.split()
        first.append(((line[0]+"?")*5)[:-1])
        second.append([int(val) for val in line[1].split(",")]*5)
    return first,second
    
def main():
    with open("day12/input.txt",'r') as file:
        input = [line.removesuffix("\n") for line in file.readlines()]
        
    first,second = transform_input(input)
    combinations = 0
    for i in range(len(input)):
        hash_table = {}
        c,hash_table = get_combinations(first[i],second[i],0,hash_table)
        combinations+=c
        
    print(combinations)

def get_combinations(first,second,combinations,hash_table):
    if (first+str(len(second))) in hash_table:
        return hash_table[(first+str(len(second)))],hash_table
    if not second:
        if "#" in first:
            return 0,hash_table
        else:
            return 1,hash_table
    current_index = 0
    while second:
        status = try_to_fit(first,second[0],current_index)
        if status == "STOP":
            return combinations,hash_table
        elif status == "FIT":
            c,hash_table = get_combinations(first[current_index+second[0]+1:],second[1:],0,hash_table)
            hash_table[(first[current_index+second[0]+1:]+str(len(second)-1))] = c
            combinations += c
        current_index+=1
    hash_table[(first+str(len(second)))] = combinations
    return combinations,hash_table

def try_to_fit(first,size_to_fit,index):
    if len(first[index:]) < size_to_fit or "#" in first[:index]:
        return "STOP"
    if "." in first[index:index+size_to_fit]:
        return "NFIT"
    if len(first[index:]) == size_to_fit:
        return "FIT"
    if len(first[index:]) > size_to_fit:
        if first[index+size_to_fit] != "#":
            return "FIT"
        return "NFIT"
   
if __name__ == "__main__":
    main()