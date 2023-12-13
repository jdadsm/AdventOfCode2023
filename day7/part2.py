import re

def main():
    with open("day7/input.txt",'r') as file:
        input = file.readlines()
        
    hands = []
    bids = []
    labels = "J23456789TQKA"
    
    for line in input:
        line = line.split()
        hands.append(line[0])
        bids.append(int(line[1]))
    
    ranks = len(hands)    
    types_index = []
    for i in range(ranks):
        types_index.append((i,get_type(hands[i]),labels.find(hands[i][0]),labels.find(hands[i][1]),labels.find(hands[i][2]),labels.find(hands[i][3]),labels.find(hands[i][4])))
    
    types_index.sort(key=lambda types_index:(types_index[1],types_index[2],types_index[3],types_index[4],types_index[5],types_index[6]))
    
    winnings = 0
    for i in range(ranks):
        winnings+=(i+1)*bids[types_index[i][0]]
    
    print(winnings)
    
    
def get_type(hand:str):
    diff = []
    if 'J' in hand:
        hand = re.sub('J','',hand)
        nJ = 5-len(hand)
        while hand:
            count = len(re.findall(hand[0],hand))
            diff.append(count)
            hand = re.sub(hand[0],"",hand)
        length = len(diff)
        diff.sort()
        if length == 4: #1,1,1,1
            return 2 #One pair
        elif length == 3: # 1,1,1 1,1,2 
            if nJ==1:
                return 4 #Three of a kind 
            elif nJ==2:
                return 4 #Three of a kind
        elif length == 2: #1,1 1,2 1,3 2,2
            if nJ==1:
                if diff[1] == 3:
                    return 6 #Four of a kind
                elif diff[1] == 2:
                    return 5 #Full house
            elif nJ==2:
                return 6 #Four of a kind
            elif nJ==3:
                return 6 #Four of a kind
        elif length == 1: # 1
            return 7 #Five of a kind
        elif length == 0:
            return 7 #FIve of a kind
        
    while hand:
        count = len(re.findall(hand[0],hand))
        diff.append(count)
        hand = re.sub(hand[0],"",hand)
    length = len(diff)
    diff.sort()
    if length == 5: 
        return 1 #High card
    elif length == 4:
        return 2 #One pair
    elif length == 3:
        if diff[2] == 2:
            return 3 #Two pairs
        return 4 #Three of a kind
    elif length == 2:
        if diff[1] == 3:
            return 5 #Full house
        return 6 #Four of a kind
    elif length == 1:
        return 7 #Five of a kind
    
if __name__ == "__main__":
    main()