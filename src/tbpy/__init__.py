import os
import keyboard
import time
import subprocess
import platform
import sys



columns, rows = os.get_terminal_size()
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
def clear():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    subprocess.call(command, shell=True)


def init():
    clear()
init()
class Button (dict):
    def __new__(
        cls,
        name,
        action = None,
    ):
        return {
            "text" : name,
            "action" : action,
            "type" : "button"
        }
class Field (dict):
    def __new__(
        cls,
        name,
        hide : bool = False
    ):
        return {
            "name" : name,
            "hide" : hide,
            "type" : "field"
        }
class TwoBitColor:
    BLACK =       "\033[30m"
    RED =         "\033[31m"
    GREEN =       "\033[32m"
    YELLOW =      "\033[33m"
    BLUE =        "\033[34m"
    MAGENTA =     "\033[35m"
    CYAN =        "\033[36m"
    LIGHTGRAY =   "\033[37m"
    COLORS =      [
        BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,LIGHTGRAY
    ]
RESET = "\033[0m"
class Color:
    def rgb(r : str, g : str, b : str):
        return "\033[38;2;{};{};{}m".format(r,g,b)
    def background(color : str):
        return color.replace("\033[38;2;","\033[48;2;")
    BLACK       = rgb(25, 25, 25)
    GRAY        = rgb(75, 75, 75)
    WHITE       = rgb(200, 200, 200)
    LIGHTGRAY   = rgb(150,150,150)
    RED         = rgb(165, 45, 45)
    ORANGE      = rgb(205, 105, 45)
    YELLOW      = rgb(175, 165, 45)
    GREEN       = rgb(75, 175, 75)
    BLUE        = rgb(45, 105, 165)
    PURPLE      = rgb(135, 75, 165)
    PINK        = rgb(205, 125, 145)
    BROWN       = rgb(135, 95, 45)
    NAVY        = rgb(25, 45, 85)
    TEAL        = rgb(45, 145, 145)
    OLIVE       = rgb(105, 105, 45)
    GOLD        = rgb(205, 165, 45)
    MAGENTA     = rgb(165, 45, 125)
    LIME        = rgb(145, 205, 45)
    CYAN        = rgb(45, 165, 165)
    MAROON      = rgb(105, 25, 45)
    FOREST      = rgb(45, 105, 55)
    AQUA        = rgb(45, 145, 125)
    KHAKI       = rgb(155, 135, 65)
    VIOLET      = rgb(125, 45, 145)
    TURQUOISE   = rgb(75, 175, 145)
    INDIGO      = rgb(55, 25, 105)
    BRONZE      = rgb(165, 105, 45)
    MUSTARD     = rgb(175, 145, 45)
    SKY         = rgb(105, 165, 205)
    PEACH       = rgb(205, 145, 115)
    BURGUNDY    = rgb(105, 25, 75)
    SEAGREEN    = rgb(45, 145, 105)
    CORAL       = rgb(205, 105, 85)
    BEIGE       = rgb(175, 165, 135)
    TAN         = rgb(165, 135, 85)
    SAGE        = rgb(105, 135, 75)
    SALMON      = rgb(205, 125, 105)
    COPPER      = rgb(165, 95, 45)
    MAUVE       = rgb(165, 75, 115)
    LAVENDER    = rgb(145, 105, 165)
    SAND        = rgb(175, 155, 125)
    CHOCOLATE   = rgb(135, 75, 35)
    BEET        = rgb(125, 35, 55)
    TOMATO      = rgb(205, 75, 75)
    OLIVEGREEN  = rgb(105, 125, 45)
    MINT        = rgb(105, 205, 145)


    COLORS = [BLACK, GRAY, WHITE, LIGHTGRAY, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, BROWN, NAVY, TEAL, OLIVE, GOLD, MAGENTA, LIME, CYAN, MAROON, FOREST, AQUA, KHAKI, VIOLET, TURQUOISE, INDIGO, BRONZE, MUSTARD, SKY, PEACH, BURGUNDY, SEAGREEN, CORAL, BEIGE, TAN, SAGE, SALMON, COPPER, MAUVE, LAVENDER, SAND, CHOCOLATE, BEET, TOMATO, OLIVEGREEN, MINT]
    
sentinel = object()
class Window():
    def __init__(self,
        name: str = "Title of the window",
        text: str = "Hello, world!",
        width : int = 40, 
        fields: list = None,
        tabindex: int = 0,
        buttons: list = [Button("OK"), Button("Cancel")],
        inputvalues: dict = {},
        ac : Color | TwoBitColor = Color.BLUE,
        wg : Color | TwoBitColor = Color.WHITE,
        bg : Color | TwoBitColor = sentinel,
        fg : Color | TwoBitColor = Color.BLACK,
        sc : Color | TwoBitColor = Color.LIGHTGRAY,
        bc : Color | TwoBitColor = Color.LIGHTGRAY,
    ) -> None:
        # ╭╮╰╯├┤─│ 40
        clear()
        if bg is sentinel:
            bg = ac
        self.destroyed = False
        self.buttons = buttons
        self.tabindex = tabindex
        self.kwargs = {"name":name,"text":text,"width":width,"fields":fields,"buttons":buttons,"tabindex":self.tabindex,"inputvalues":inputvalues,"ac":ac,"bg":bg,"fg":fg,"sc":sc,"wg":wg,"bc":bc}
        self.inputvalues = inputvalues
        self.padx = ((columns - width + 1) // 2) - 2
        self.pady = int((rows - (len(text.split("\n")) + 4 + len(fields) if fields else 0 + 1 if buttons else 0)) / 2)
        self.height = rows
        #self.height = int((rows + (len(text.split("\n")) + 4 + len(fields) if fields else 0 + 1 if buttons else 0)))
        self.width = width
        self.fields = fields
        self.tabs = self.buttons + (self.fields if self.fields else [])
        self.text_to_print = ""

        self.text_to_print += bg + (("█" * columns) + "\n") * int(self.pady-5) +  RESET
        self.text_to_print += bg + ("█" * self.padx) +  RESET + Color.background(wg) + bc + "╭─"  + fg + str(name) + RESET + Color.background(wg) + bc + "─" * ((self.width - 1) - len(str(name))) + "╮"+ bg + ("█" * (self.padx)) + "██" +  RESET +"\n"
        if self.fields:
            a=0
            for i in text.split("\n"):
                if len(str(i)) >= (self.width - 1):
                    raise ValueError("To much text! Text must be less than {} characters (line {})".format(self.width,a))
                else:
                    self.text_to_print += bg + ("█" * self.padx) +  RESET + Color.background(wg) + bc + "│ " + fg + str(i) + " " * ((self.width - 1) - len(str(i))) +  RESET + Color.background(wg) + bc + "│"+ fg + "█" + bg + ("█" * (self.padx)) +  RESET  + "\n"
                a+=1
            self.text_to_print += bg + ("█" * self.padx) +  RESET + Color.background(wg) + bc + "├"+ ("─" * self.width) + "┤"+ sc + "█" + bg + ("█" * (self.padx)) +  RESET  + "\n"
            b = 0
            

            for j in self.fields:
                
                try:
                    self.kwargs["inputvalues"][j["name"]] = inputvalues[j["name"]]
                except KeyError:
                    self.kwargs["inputvalues"][j["name"]] = ""
                if j["hide"]:
                    value = "*" * len(self.inputvalues[j["name"]])
                else:
                    value = self.inputvalues[j["name"]][:(self.width - 7) - len(str(j["name"]))] + "..." if len(self.inputvalues[j["name"]]) > (self.width - 7) - len(str(j["name"])) else self.inputvalues[j["name"]]
                if self.tabindex == self.tabs.index(j):
                    self.text_to_print += bg + ("█" * self.padx) +  RESET + Color.background(wg) + bc + "│" + Color.WHITE + Color.background(fg) + " " + str(j["name"]) + " : " + value + "_" + " " * ((self.width - 5) - len(value) - len(str(j["name"]))) +  RESET + Color.background(wg)  + "│"+ fg + "█" + bg + ("█" * (self.padx)) +  RESET  + "\n"
                else:
                    self.text_to_print += bg + ("█" * self.padx) +  RESET + Color.background(wg) + bc + "│ " + fg + str(j["name"]) + " : " + value + " " * ((self.width - 4) - len(value) - len(str(j["name"]))) +  RESET + Color.background(wg) + bc + "│"+ fg + "█" + bg + ("█" * (self.padx)) +  RESET  + "\n"
                b+=1
        else:
            a=0
            for i in text.split("\n")[:-1]:
                if len(str(i)) >= (self.width - 1):
                    raise ValueError("To much text! Text must be less than {} characters (line {})".format(self.width,a))
                else:
                    self.text_to_print += bg + ("█" * self.padx) +  RESET + Color.background(wg) + bc + "│ " + fg + str(i) + " " * ((self.width - 1) - len(str(i))) +  RESET + Color.background(wg) + "│"+ fg + "█" + bg + ("█" * (self.padx)) +  RESET  + "\n"
                a+=1
            self.text_to_print += bg + ("█" * self.padx) +  RESET + Color.background(wg) + bc + "│ " + fg + str(text.split("\n")[-1]) + " " * ((self.width - 1) - len(str(text.split("\n")[-1]))) +  RESET + Color.background(wg) + bc + "│" + sc + "█" + bg + ("█" * (self.padx)) +  RESET 

        
        self.text_to_print += bg + ("█" * self.padx) + "█" +  RESET + Color.background(wg) + bc + "├"+ ("─" * self.width) + "┤" + sc + "█" + bg + ("█" * (self.padx)) + "█" +  RESET  + "\n"
        self.text_to_print += bg + ("█" * self.padx) +  RESET + Color.background(wg) + bc + "│ "
        self.buttonpad = 1
        for i in self.buttons:
            if self.tabindex == self.tabs.index(i):
                self.text_to_print += Color.background(ac) + Color.WHITE + "< " + str(i["text"]) + " >" + RESET + Color.background(wg) + "     "
                self.buttonpad+=len(str( "< " + str(i["text"]) + " >" + "     "))
            else:
                self.text_to_print += fg + "< "+ str(i["text"]) + " >" + RESET + Color.background(wg) + "     "
                self.buttonpad+=len(str( "< " + str(i["text"]) + " >" + "     "))
            #  + " " * ((self.width - 1) - len(str(i))) + "│\n"
            # + fg + "█" + bg + ("█" * (self.padx)) +  RESET  + "\n"
        self.text_to_print += (width - int(self.buttonpad))*" " + bc + "│"+ sc + "█" + bg + ("█" * (self.padx)) + "█" +  RESET + "\n"
        self.text_to_print += bg + ("█" * self.padx) +  RESET + Color.background(wg) + bc + "╰" + ("─" * self.width) + "╯" + sc + "█" + bg + ("█" * (self.padx)) + "█" +  RESET  + "\n"
        self.text_to_print += bg + ("█" * (self.padx+1)) +  RESET + sc + Color.background(bg) + ("▀" * self.width) + "▀▀" + bg + ("█" * (self.padx)) + "█" +  RESET + "\n"
        self.text_to_print += bg + ("█" * columns) * self.pady +  RESET
        if not self.destroyed:
            # for i in range(len(self.text_to_print.split("\n"))):
            #     delete_last_line()
            sys.stdout.write(self.text_to_print)





        
    def destroy(self):
        clear()
        self.destroyed = True


    def mainloop(self):
        while True:  # making a loop
            try:
                if not self.destroyed:
                    key = keyboard.read_key()
                    if key == "tab":
                        if self.tabindex < len(self.tabs) - 1:
                            self.tabindex += 1
                            self.kwargs["tabindex"] += 1
                        else:
                            self.tabindex = 0
                            self.kwargs["tabindex"] = 0
                        self.__init__(**self.kwargs)
                        time.sleep(0.35)
                    elif keyboard.read_key() == "enter": 
                        for i in self.tabs:
                            if i["type"] == "button":
                                if "action" in i:
                                    if self.tabindex == self.tabs.index(i):
                                        act = i["action"]
                                        if act != None:
                                            act()
                    else:
                        if self.fields != []:
                            if self.tabs[self.tabindex]["type"] == "field":
                                if key == "backspace":
                                    self.inputvalues[self.tabs[self.tabindex]["name"]] = self.kwargs["inputvalues"][self.tabs[self.tabindex]["name"]][:-1]
                                    self.kwargs["inputvalues"] = self.inputvalues
                                    self.__init__(**self.kwargs)
                                    time.sleep(0.2)
                                elif len(key) == 1:
                                    self.inputvalues[self.tabs[self.tabindex]["name"]] += key
                                    self.kwargs["inputvalues"] = self.inputvalues
                                    self.__init__(**self.kwargs)
                                    time.sleep(0.1)
                else:
                    break

            except KeyboardInterrupt:
                self.destroy()
                exit()

