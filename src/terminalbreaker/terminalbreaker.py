from colorama import Fore, Back, Style
import colorama
import os
import sys
import keyboard

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def init():
    colorama.init()
    clear()

class Window():
    def __init__(self,name=str("Title of the window"),lines=list(["Hello, world!"]),padx=int(50),pady=int(5), width=int(40),fields=list(),buttons=list()):
        # ┌┐└┘├┤─│ 40
        self.destroyed = False
        self.buttons = buttons
        self.buttonindex = 0
        self.padx = padx
        self.pady = pady
        self.width = width
        self.text = ""
        self.fields = fields
        self.text += "\n" * self.pady
        self.text +=  " " * self.padx + "┌"+ ("─" * self.width) + "┐\n"
        self.text += " " * self.padx + "│ " + Style.BRIGHT + str(name) + Style.RESET_ALL + " " * ((self.width - 1) - len(str(name))) + "│\n"
        self.text += " " * self.padx + "├"+ ("─" * self.width) + "┤\n"

        if self.fields:
            for i in lines:
                if len(str(i)) >= (self.width - 1):
                    raise ValueError("To much text! Text must be less than {}".format(self.width))
                else:
                    self.text += " " * self.padx + "│ " + str(i) + " " * ((self.width - 1) - len(str(i))) + "│\n"
            self.text += " " * self.padx + "├"+ ("─" * self.width) + "┤"
        else:
            for i in lines[:-1]:
                if len(str(i)) >= (self.width - 1):
                    raise ValueError("To much text! Text must be less than {}".format(self.width))
                else:
                    self.text += " " * self.padx + "│ " + str(i) + " " * ((self.width - 1) - len(str(i))) + "│\n"
            self.text += " " * self.padx + "│ " + str(lines[-1]) + " " * ((self.width - 1) - len(str(lines[-1]))) + "│"


        self.end = ""
        self.buttonsend = ""
        if self.buttons:
            self.buttonsend += " " * self.padx + "├"+ ("─" * self.width) + "┤\n"
            self.buttonsend += " " * self.padx + "│ "
            for i in self.buttons:
                if self.buttonindex == self.buttons.index(i):
                    self.buttonsend += Back.BLUE + str(i["text"]) + Style.RESET_ALL + " "
                else:
                    self.buttonsend += Back.LIGHTBLACK_EX + str(i["text"]) + Style.RESET_ALL + " "
                #  + " " * ((self.width - 1) - len(str(i))) + "│\n"
        self.end += " " * self.padx + "└" + ("─" * self.width) + "┘\n"
        self.end += "\n" * self.pady
        self.input_values = {}
        if not self.destroyed:
            print(self.text)
            for i in self.fields:
                self.input_values[i] = input(" " * self.padx + "│ " + Back.BLUE + str(i) + Style.RESET_ALL + " : ")
            if self.buttons:
                print(self.buttonsend)
            print(self.end)

        
    def destroy(self):
        clear()
        self.destroyed = True


    def mainloop(self):
        while True:  # making a loop
            try:
                if not self.destroyed:
                    if keyboard.read_key() == "tab":
                        if self.buttons:
                            if self.buttonindex < len(self.buttons):
                                self.buttonindex += 1
                            else:
                                self.buttonindex -= 2
                            for i in self.buttons:
                                if self.buttonindex == self.buttons.index(i):
                                    clear()
                                    print(self.text)
                                    for i in self.fields:
                                        print(" " * self.padx + "│ " + Back.BLUE + str(i) + Style.RESET_ALL + " : " + self.input_values[i])
                                    self.buttonsend = ""
                                    self.buttonsend += " " * self.padx + "├"+ ("─" * self.width) + "┤\n"
                                    self.buttonsend += " " * self.padx + "│ "
                                    for i in self.buttons:
                                        if self.buttonindex == self.buttons.index(i):
                                            self.buttonsend += Back.BLUE + str(i["text"]) + Style.RESET_ALL + " "
                                        else:
                                            self.buttonsend += Back.LIGHTBLACK_EX + str(i["text"]) + Style.RESET_ALL + " "
                                    print(self.buttonsend)
                                    print(self.end)
                    elif keyboard.read_key() == "enter":
                        if self.buttons:
                            for i in self.buttons:
                                if "action" in i:
                                    if self.buttonindex == self.buttons.index(i):
                                        act = i["action"]
                                        act()
                else:
                    break

            except KeyboardInterrupt:
                clear()
                exit()

