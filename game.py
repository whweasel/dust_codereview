from player_h import player
from TerminalUtils.terminalfx import *
import pickle
gray = color("gray60")

def without(d, key):
    new_d = d.copy()
    new_d.pop(key)
    return new_d
def dialogue(person, msg):
    clear()
    print(indent(person + ":"))
    print(indent("="*len(person)))
    echo(indent(msg))
    wait()
def cmenu(title, contents):
    contents["newln0"] = "=============="
    contents["inventory"] = "Inventory"
    contents["newln1"] = ""
    contents["playername"] = str(gray('Police Chief "{}"'.format(player.name)))
    contents["hp"] = str(gray("HP: {}/{}".format(player.hp, player.max_hp)))
    contents["lv"] = str(gray("LV: {}".format(player.lv)))
    while True:
        result = Menu.menu(title, contents)
        if result == "inventory":
            player.openinv()
            continue
        elif result in ["newln0", "newln1", "playername", "hp", "lv"]:
            continue
        elif result not in ["newln0", "inventory", "newln1", "playername", "hp", "lv"]:
            return result
def intro():
    clear()
    echo(indent("Aurora Police Department"), delay=ms(30), color="gold1")
    sleep(.7)
    echo(indent("COTTONWOOD, COLORADO"), delay=ms(30), color="gray30")
    wait()

def cottonwood_1():
    cmenu("WIP, cottonwood_1 function", {
        "cont":"Exit"}
    )
    clear()
    echo(indent("Game saved."))








global saves
saves = [
    intro,
    cottonwood_1
]
def run():
    global saves
    for save in saves:
        player.saved = save.__name__
        player.save()
        save()
        
        clear()
        player.save()
        echo(indent("Game saved."))
        wait()
def runip():
    global saves
    eff = pickle.load( open( "user.dat", "rb" ) )
    for funct in saves:
        if funct.__name__ == eff["saved"]:
            i = saves.index(funct)
            break
    player.load()
    saves = saves[i:]
    for save in saves:
        player.saved = save.__name__
        player.save()
        save()
        clear()
        player.save()
        echo(indent("Game saved."))
        wait()