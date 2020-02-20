from TerminalUtils.terminalfx import *
from player_h import player
import time
import game
import sys
from blessed import Terminal;t = Terminal()
red = color("red1")
yellow = color("gold1")
#gray = color("gray60")
Menu.selected_choice_color = color("black_on_gold1")
def newgame():
    while True:
        clear()
        with t.cbreak():
            t.inkey(timeout=2/1000)
        echo(indent("Name your character."), delay=ms(40))
        playerName = input(">")
        ch = Menu.menu(
            title = "Are you sure you want the name, '" + t.gold1 + playerName + t.normal + "'?",
            contents = {
                "yes":"Yes","no":"No"}
        )
        if ch == "yes":
            break
        else:
            continue
    player.initialize(playerName)
    game.run()

def cont():
    game.runip()

class onStart:
    game_title = red("Dust.")
    def credit():
        clear()
        echo(indent("Copyright (C) 2020 DH93"))
        echo(indent("Created using Blessed > "), end='')
        echo("https://blessed.readthedocs.io/", color="underline", end='\n\n')
        echo(indent("Use the arrow keys and [Z]/[ENTER] to navigate menus."))
        while True:
            with t.cbreak():
                key = t.inkey()
                if key == "z" or key.name == "KEY_ENTER":
                    return
    mappings = {
            "newgame":newgame,
            "cont":cont,
            "credit":credit,
            "quit":sys.exit
        }
    @classmethod
    def titleScreen(cls):
        while True:
            choice = Menu.menu(
                title = cls.game_title,
                contents = {
                    "newgame":"New Game",
                    "cont":"Continue",
                    "credit":"Help/Credits",
                    "quit":"Quit"
                }
            )
            cls.mappings[choice]()
onStart.titleScreen()