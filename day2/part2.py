def main():
    with open("day2/input.txt",'r') as file:
        input = file.readlines()
        
    RED = 12
    GREEN = 13
    BLUE = 14
        
    power = 0
    
    for line in input:
        min_values = Game(line,RED,GREEN,BLUE).getMinValues()
        power+= min_values[0]*min_values[1]*min_values[2]
        
    print("Total power:",power)
    
class Game:
    
    def __init__(self,line,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.line = line
        
    def getMinValues(self):
        sets = self.line.split(":")[1].removesuffix("\n").split(";")
        min_red = 0
        min_green = 0
        min_blue = 0

        for set in sets:
            values = set.split(",")
            
            for val in values:
                if val.find("red") != -1:
                    if int(val.removesuffix("red")) > min_red:
                        min_red = int(val.removesuffix("red"))
                elif val.find("blue") != -1:
                    if int(val.removesuffix("blue")) > min_blue:
                        min_blue = int(val.removesuffix("blue"))
                elif val.find("green") != -1:
                    if int(val.removesuffix("green")) > min_green:
                        min_green = int(val.removesuffix("green"))
        
        return (min_red,min_green,min_blue)
    
if __name__ == "__main__":
    main()