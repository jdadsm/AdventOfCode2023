def main():
    with open("day6/input.txt",'r') as file:
        input = file.readlines()
        
    time = [int(i) for i in input[0].removeprefix("Time:").removesuffix("\n").split()]
    distance = [int(i) for i in input[1].removeprefix("Distance:").removesuffix("\n").split()]
    
    victories = [0 for t in time]
    for i in range(len(time)):
        t = time[i]
        d = distance[i]
        for j in range(t+1):
            if j*(t-j) > d:
                victories[i]+=1
    
    res = 1
    for i in victories:
        res*=i
    print(res)

if __name__ == "__main__":
    main()