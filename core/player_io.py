
def ask_player_action() -> str:
    ask_player=input("if you want to stop press: S" + " " "if you want to play press:" "H")
    while ask_player!="S" and ask_player!="H":
        ask_player = input("if you want to stop press: S" + " " "if you want to play press:" "H")

    ask_player = ask_player.upper()
    return ask_player
