from core import deck
from core import  game_logic

if __name__ == '__main__':
    deck_card=deck.build_standard_deck()
    swap_card=deck.shuffle_by_suit(deck_card)
    player={"hand":[]}
    dealer={"hand":[]}
    game_logic.run_full_game(deck_card,player,dealer)
