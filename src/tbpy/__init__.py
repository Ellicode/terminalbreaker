from colorama import Fore, Back, Style
import colorama
import os
import keyboard
import time
import sys

columns, rows = os.get_terminal_size()
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def init():
    colorama.init()
    clear()
init()
class Button():
    def __init__(self,
        name : str,
        action : function
    ):
        return {
            "name" : name,
            "action": action,
            "type" : "button"
        }
class Field():
    def __init__(self,
        name : str,
        hide : bool = False
    ):
        return {
            "name" : name,
            "hide" : hide,
            "type" : "field"
        }
class Window():
    def __init__(self,
        name:str = "Title of the window",
        text: str = "Hello, world!",
        width : int = 40, 
        fields: list = None,
        tabindex: int = 0,
        buttons: list = [{"text":"OK", "type": "button"}, {"text":"Cancel", "type": "button"}],
        inputvalues: dict = {}
    ):
        # ╭╮╰╯├┤─│ 40
        clear()
        self.destroyed = False
        self.buttons = buttons
        self.tabindex = tabindex
        self.kwargs = {"name":name,"text":text,"width":width,"fields":fields,"buttons":buttons,"tabindex":self.tabindex,"inputvalues":inputvalues}
        self.inputvalues = inputvalues
        self.padx = ((columns - width + 1) // 2) - 2
        self.pady = int((rows - (len(text.split("\n")) + 4 + len(fields) if fields else 0 + 1 if buttons else 0)) / 2)
        self.height = rows
        #self.height = int((rows + (len(text.split("\n")) + 4 + len(fields) if fields else 0 + 1 if buttons else 0)))
        self.width = width
        self.fields = fields
        self.tabs = self.buttons + (self.fields if self.fields else [])
        self.text_to_print = ""

        self.text_to_print += colorama.Fore.BLUE + (("█" * columns) + "\n") * int(self.pady-5) +  colorama.Style.RESET_ALL
        self.text_to_print += colorama.Fore.BLUE + ("█" * self.padx) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "╭─"  + colorama.Fore.BLACK + Style.BRIGHT + str(name) + Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "─" * ((self.width - 1) - len(str(name))) + "╮"+ colorama.Fore.BLUE + ("█" * (self.padx)) + "█" +  colorama.Style.RESET_ALL +"\n"
        if self.fields:
            a=0
            for i in text.split("\n"):
                if len(str(i)) >= (self.width - 1):
                    raise ValueError("To much text! Text must be less than {} characters (line {})".format(self.width,a))
                else:
                    self.text_to_print += colorama.Fore.BLUE + ("█" * self.padx) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "│ " + colorama.Fore.BLACK + str(i) + " " * ((self.width - 1) - len(str(i))) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX  + "│"+ colorama.Fore.BLACK + "█" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL  + "\n"
                a+=1
            self.text_to_print += colorama.Fore.BLUE + ("█" * self.padx) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "├"+ ("─" * self.width) + "┤"+ colorama.Fore.BLACK + "█" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL  + "\n"
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
                    self.text_to_print += colorama.Fore.BLUE + ("█" * self.padx) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "│" + colorama.Fore.WHITE + colorama.Back.BLACK + " " + str(j["name"]) + " : " + value + "_" + " " * ((self.width - 5) - len(value) - len(str(j["name"]))) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX  + "│"+ colorama.Fore.BLACK + "█" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL  + "\n"
                else:
                    self.text_to_print += colorama.Fore.BLUE + ("█" * self.padx) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "│ " + colorama.Fore.BLACK + str(j["name"]) + " : " + value + " " * ((self.width - 4) - len(value) - len(str(j["name"]))) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX  + "│"+ colorama.Fore.BLACK + "█" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL  + "\n"
                b+=1
        else:
            a=0
            for i in text.split("\n")[:-1]:
                if len(str(i)) >= (self.width - 1):
                    raise ValueError("To much text! Text must be less than {} characters (line {})".format(self.width,a))
                else:
                    self.text_to_print += colorama.Fore.BLUE + ("█" * self.padx) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "│ " + colorama.Fore.BLACK + str(i) + " " * ((self.width - 1) - len(str(i))) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "│"+ colorama.Fore.BLACK + "█" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL  + "\n"
                a+=1
            self.text_to_print += colorama.Fore.BLUE + ("█" * self.padx) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "│ " + colorama.Fore.BLACK + str(text.split("\n")[-1]) + " " * ((self.width - 1) - len(str(text.split("\n")[-1]))) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "│" + colorama.Fore.BLACK + "█" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL 

        
        self.text_to_print += colorama.Fore.BLUE + ("█" * self.padx) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "├"+ ("─" * self.width) + "┤" + colorama.Fore.BLACK + "█" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL  + "\n"
        self.text_to_print += colorama.Fore.BLUE + ("█" * self.padx) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "│ "
        self.buttonpad = 1
        for i in self.buttons:
            if self.tabindex == self.tabs.index(i):
                self.text_to_print += colorama.Back.BLUE + "< " + str(i["text"]) + " >" + Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "     "
                self.buttonpad+=len(str( "< " + str(i["text"]) + " >" + "     "))
            else:
                self.text_to_print += colorama.Fore.BLACK + "< "+ str(i["text"]) + " >" + Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "     "
                self.buttonpad+=len(str( "< " + str(i["text"]) + " >" + "     "))
            #  + " " * ((self.width - 1) - len(str(i))) + "│\n"
            # + colorama.Fore.BLACK + "█" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL  + "\n"
        self.text_to_print += (width - int(self.buttonpad))*" " +  "│"+ colorama.Fore.BLACK + "█" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL + "\n"
        self.text_to_print += colorama.Fore.BLUE + ("█" * self.padx) +  colorama.Style.RESET_ALL + colorama.Back.LIGHTWHITE_EX + "╰" + ("─" * self.width) + "╯" + colorama.Fore.BLACK + "█" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL  + "\n"
        self.text_to_print += colorama.Fore.BLUE + ("█" * (self.padx+1)) +  colorama.Style.RESET_ALL + colorama.Fore.BLACK + colorama.Back.BLUE + ("▀" * self.width) + "▀▀" + colorama.Fore.BLUE + ("█" * (self.padx)) +  colorama.Style.RESET_ALL + "\n"
        self.text_to_print += colorama.Fore.BLUE + ("█" * columns) * self.pady +  colorama.Style.RESET_ALL
        if not self.destroyed:
            # for i in range(len(self.text_to_print.split("\n"))):
            #     delete_last_line()
            print(self.text_to_print,end="\r"*self.height)

        
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

