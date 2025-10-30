import random


def build_standard_deck() -> list[dict]:#יוצר חבילת קלפים
    type_cards=["H","c","D","s"]
    cards_degree=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    lst=[]
    for i in range(len(type_cards)):
        for j in range(len(cards_degree)):
            dic={}
            dic["rank"]=cards_degree[j]
            dic["suit"]=type_cards[i]
            lst.append(dic)
    return lst

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]: #ערבוב הקלפים
    for s in range(swaps):
        i=random.randint(0,len(deck)-1)
        card_1=deck[i]
        type_suit=card_1["suit"]
        j=random.randint(0,len(deck)-1)
        while j==i:
            j=random.randint(0,len(deck)-1)
        while type_suit == "H" and j%5 != 0:
            j=random.randint(0,len(deck)-1)
        while type_suit == "c" and j%3 != 0:
            j=random.randint(0,len(deck)-1)
        while type_suit == "D" and j%2 != 0:
            j=random.randint(0,len(deck)-1)
        while type_suit == "s" and j%7 != 0:
            j=random.randint(0,len(deck)-1)
        card_2=deck[j]
        deck[i],deck[j]=card_2,card_1
    return deck




