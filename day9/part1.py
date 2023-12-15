def main():
    with open("day9/input.txt",'r') as file:
        input = file.readlines()
        
    for i in range(len(input)):
        input[i] = [int(val) for val in input[i].split()]

    res = []
    for line in input:
        lines = [line]    
        while [non_zero for non_zero in lines[-1] if non_zero!=0]:
            new_line  = []
            temp = lines[-1][0]
            for val in lines[-1][1:]:
                new_line.append(val-temp)
                temp = val
            lines.append(new_line)
            
        res.append(sum([last[-1] for last in lines]))

    print(sum(res))
    
if __name__ == "__main__":
    main()