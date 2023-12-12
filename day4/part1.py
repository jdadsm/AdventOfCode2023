import math

def main():
    with open("day4/input.txt",'r') as file:
        input = file.readlines()
    
    points_per_card = []    
    for card in input:
        card = card.removesuffix("\n").split("|")
    
        winning_numbers = set(card[0].split(":")[1].split())
        numbers = set(card[1].split())
        
        points_per_card.append( math.floor( 2**(len(winning_numbers.intersection(numbers))-1) ) )
    
    print(sum(points_per_card))

if __name__ == "__main__":
    main()