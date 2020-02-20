from TerminalUtils.terminalfx import *
from items import *
from blessed import Terminal
import pickle

def getAttributes(clazz):
    return {name: attr for name, attr in clazz.__dict__.items()
            if not name.startswith("__") 
            and not callable(attr)
            and not type(attr) is staticmethod
            and not type(attr) is classmethod}
    



t = Terminal()
Menu.selected_choice_color = color("black_on_gold1")
gray = color("gray60")

class player:
    """description of class"""
    @classmethod
    def initialize(cls, name):
        cls.name = name
        cls.hp = 14
        cls.max_hp = 20
        cls.lv = 0
        cls.exp = 0
        cls.inventory = [
            Phone(),
            item("Pen","Mightier than the sword", 2, "Use", use= {"msg":"There was no ink. You should probably get rid of it.", "action":"none"}),
            Bar(),
            item("Badge","A police badge. Your name is engraved on it.", 40, "Do nothing", use= {"msg":"You did nothing with your badge", "action":"none"})
        ]
    @classmethod
    def openinv(cls):
        while True:
            invitems = {thing.id: thing.name for thing in cls.inventory}
            invitems["exit"] = "Exit Inventory"
            invitems["newln"] = ""
            invitems["playername"] = str(gray('"{}"'.format(cls.name)))
            invitems["hp"] = str(gray("HP: {}/{}".format(cls.hp, cls.max_hp)))
            invitems["lv"] = str(gray("LV: {}".format(cls.lv)))

            choice = Menu.menu(
                title = "Inventory",
                contents = invitems 
            )
            if choice == "exit":
                clear()
                return
            try:
                while True:
                    displayed_item = next((thing for thing in cls.inventory if thing.id == choice), None)
                    final_choice = Menu.menu(
                        title = displayed_item.name,
                        contents = {
                            "use":displayed_item.useType,
                            "inspect":"Inspect",
                            "drop":"Drop",
                            "back":"Back"
                        }
                    )
                    if final_choice == "back":
                        break
                    elif final_choice == "use":
                        use = displayed_item.use()
                        clear()
                        echo(indent(use["msg"]))
                        if "heal_" in use["action"]:
                            cls.hp += int(use["action"].replace("heal_", ''))
                            if cls.hp > cls.max_hp:
                                cls.hp = cls.max_hp
                            cls.inventory.remove(displayed_item)
                        wait()
                        break
                    elif final_choice == "inspect":
                        clear()
                        print(displayed_item)
                        wait()
                        continue
                    elif final_choice == "drop":
                        clear()
                        print("You dropped the {}".format(displayed_item.name))
                        cls.inventory.remove(displayed_item)
                        wait()
                        break
            except AttributeError:
                continue
    @classmethod
    def save(cls):
        ad =  getAttributes(cls)
        pickle.dump( ad, open( "user.dat", "wb" ))
        del ad
    @classmethod
    def load(cls):
        stuff = pickle.load( open( "user.dat", "rb" ) )
        for key in stuff:
            cls.name = stuff["name"]
            cls.max_hp = stuff["max_hp"]
            cls.hp = stuff["hp"]
            cls.lv = stuff["lv"]
            cls.inventory = stuff["inventory"]
"""
player.initialize("DH93")
player.hp = 17 #Setting HP value to 10
player.openinv()
#I'm coding an inventory system for a game"""