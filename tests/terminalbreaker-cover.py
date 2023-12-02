from tbpy import *

win = Window(
    name="Terminalbreaker.exe",
    text="TerminalBreaker is a python module\nto create better guis, forms and more"
    ,ac=Color.CYAN
    ,fields=[Field("Username"),Field("Password")]
    ,buttons=[Button("Submit"),Button("Cancel")])
win.mainloop()