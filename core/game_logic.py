from core import player_io
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
    player["hand"].append(deck[0])
    player["hand"].append(deck[1])
    dealer["hand"].append(deck[2])
    dealer["hand"].append(deck[3])
    deck.remove(deck[0])
    deck.remove(deck[1])
    deck.remove(deck[2])
    deck.remove(deck[3])
    value_hand_1=calculate_hand_value(player["hand"])
    value_hand_2=calculate_hand_value(dealer["hand"])
    value=value_hand_1+value_hand_2
    print(value)

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    sum_hand_dealer = calculate_hand_value(dealer["hand"])
    for i in range(len(deck)):
        dealer["hand"].append(deck[i])
        deck.remove(deck[i])
        sum_hand_dealer=calculate_hand_value(dealer["hand"])
        if sum_hand_dealer>=17:
            break
    if sum_hand_dealer>21:
        print("The game is cancelled")
        return False
    elif 17<=sum_hand_dealer<=21:
        print("the dealer finish the game")
        return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    player_action = player_io.ask_player_action()
    hand_value_player = calculate_hand_value(player["hand"])
    while player_action=="H":
        for i in range(len(deck)):
            player["hand"].append(deck[i])
            deck.remove(deck[i])
            hand_value_player=calculate_hand_value(player["hand"])
            if hand_value_player>21:
                print("The game is cancelled ")
                break
            else:
                player_action = player_io.ask_player_action()
    if player_action=="S":
        play_dealer=dealer_play(deck, dealer)
        if play_dealer and hand_value_player<=21:
            sum_hand_dealer=calculate_hand_value(player["hand"])
            hand_value_player=calculate_hand_value(player["hand"])
            if sum_hand_dealer>hand_value_player:
                print("the dealer win the game")
                print(sum_hand_dealer, hand_value_player)
            elif sum_hand_dealer<hand_value_player:
                print("the player win the game")
                print(hand_value_player,sum_hand_dealer)
            else:
                print("the game finish with teko")
                print(hand_value_player,sum_hand_dealer)










