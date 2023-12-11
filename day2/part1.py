def main():
    with open("day2/input.txt",'r') as file:
        input = file.readlines()
        
    RED = 12
    GREEN = 13
    BLUE = 14
        
    sum_ids = 0
    
    for line in input:
        id = int(line.split(":")[0].removeprefix("Game "))
        sum_ids+=id
        sets = line.split(":")[1].removesuffix("\n").split(";")
        for set in sets:
            if not cubeSet(set,RED,GREEN,BLUE).setIsPossible():
                sum_ids-=id
                break
        
        
    print("Sum:",sum_ids)
    
class cubeSet:
    
    def __init__(self,line,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.line = line
        
    def setIsPossible(self):
        values = self.line.split(",")
        reds = 0
        greens = 0
        blues = 0
        for val in values:
            if val.find("red") != -1:
                reds += int(val.removesuffix("red"))
            elif val.find("blue") != -1:
                blues += int(val.removesuffix("blue"))
            elif val.find("green") != -1:
                greens += int(val.removesuffix("green"))

        if reds > self.red or greens > self.green or blues > self.blue:
            return False
        return True

if __name__ == "__main__":
    main()