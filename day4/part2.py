import math

def main():
    with open("day4/input.txt",'r') as file:
        input = file.readlines()
    
    cards_copies = [0 for line in input]
    for i in range(len(input)):
        cards_copies[i]+=1
        
        card = input[i]
        card = card.removesuffix("\n").split("|")
    
        winning_numbers = set(card[0].split(":")[1].split())
        numbers = set(card[1].split())
        
        n_matches = len(winning_numbers.intersection(numbers))
        for j in range(n_matches):
            cards_copies[i+j+1]+=cards_copies[i]
        
    
    print(sum(cards_copies))

if __name__ == "__main__":
    main()