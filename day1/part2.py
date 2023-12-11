def main():
    with open("day1/input.txt",'r') as file:
        input = file.readlines()
        
    sum = 0
    
    for line in input:
        templine = replaceByDigits(line)
        templine = [digit for digit in templine if digit.isdigit()]
        sum += int(templine[0]+templine[-1])
        
    print("Sum:",sum)


def replaceByDigits(line:str):
    line = line.replace("zero","z0o")
    line = line.replace("one","o1e")
    line = line.replace("two","t2o")
    line = line.replace("three","t3e")
    line = line.replace("four","f4r")
    line = line.replace("five","f5e")
    line = line.replace("six","s6x")
    line = line.replace("seven","s7n")
    line = line.replace("eight","e8t")
    return line.replace("nine","n9e")

if __name__ == "__main__":
    main()