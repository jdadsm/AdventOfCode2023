
def main():
    with open("day1/input.txt",'r') as file:
        input = file.readlines()
        
    sum = 0
    
    for line in input:
        templine = [digit for digit in line if digit.isdigit()]
        sum += int(templine[0]+templine[-1])
        
    print("Sum:",sum)


if __name__ == "__main__":
    main()