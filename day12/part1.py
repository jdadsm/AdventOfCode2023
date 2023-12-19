from itertools import product
import re

def main():
    with open("day12/input.txt",'r') as file:
        input = [line.removesuffix("\n") for line in file.readlines()]
        
    first = []
    second = []
    for line in input:
        line = line.split()
        first.append(line[0])
        second.append([int(val) for val in line[1].split(",")])
    
    arragements = []
    for i in range(len(input)):
        count = 0
        unknowns = first[i].count("?")
        current_qm = sum(second[i])-first[i].count("#")
        combinations = [''.join(comb) for comb in product(['.', '#'], repeat=unknowns) if comb.count('#') == current_qm]
        for comb in combinations:
            temp = str(first[i])
            for j in range(len(comb)):
                temp = temp.replace("?",comb[j],1)
            if check_criteria(temp,second[i]):
                count+=1
        arragements.append(count)
    print(sum(arragements))
            
def check_criteria(comb,second):
    last = "."
    res = []
    for i in range(len(comb)):
        if comb[i] == "#":
            if last == "#":
                res[-1] += 1
            else:
                res.append(1)        
        last = comb[i]
    return res == second

if __name__ == "__main__":
    main()