def main():
    with open("day6/input.txt",'r') as file:
        input = file.readlines()
        
    time = int("".join(input[0].removeprefix("Time:").removesuffix("\n").split()))
    distance = int("".join(input[1].removeprefix("Distance:").removesuffix("\n").split()))
    
    victories = 0
    
    if time%2 == 1:    
        for j in range((time+1)/2):
            if j*(time-j) > distance:
                victories+=1
        victories*=2
    else:
        for j in range((time+1)//2):
            if j*(time-j) > distance:
                victories+=1
        victories*=2
        victories+=1
    print(victories)
    
if __name__ == "__main__":
    main()