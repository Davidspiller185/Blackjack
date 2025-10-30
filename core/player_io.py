
def ask_player_action() -> str:
    ask_player=input("if you want to stop press: S" + " " "if you want to play press:" "H")
    while ask_player!="S" or ask_player!="H":
        ask_player = input("if you want to stop press: S" + " " "if you want to play press:" "H")
        if ask_player=="S" or ask_player=="S":
            break
    ask_player = ask_player.upper()
    return ask_player
