
def calculate_hand_value(hand: list[dict]) -> int:
    lst=[]
    for i in range(len(hand)):
        if hand[i]["rank"].isdigit():
             lst.append(int(hand[i]["rank"]))
        elif hand[i]["rank"].isalpha():
            if hand[i]["rank"] == "j" or hand[i]["rank"] == "Q" or hand[i]["rank"] == "K":
                lst.append(10)
            elif hand[i]["rank"] == "A":
                lst.append(1)
    return sum(lst)

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player_hand=[deck[0],deck[1]]
    dealer_hand=[deck[2],deck[3]]
    value_hand_1=calculate_hand_value(player_hand)
    deck.remove(deck[0])
    deck.remove(deck[1])
    value_hand_2=calculate_hand_value(dealer_hand)
    deck.remove(deck[2])
    deck.remove(deck[3])
    value=value_hand_1+value_hand_2
    print(value)

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    for i in range(len(deck)):
        dealer_hand=[deck[i]]
        




