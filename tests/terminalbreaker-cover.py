from tbpy import *

clear()
win = Window(
    "Terminalbreaker.exe"
    ,["BREAK THE TERMINAL!"
    ,"Create panels, forms, dialogs and buttons into your"
    ,"Python CLI app! Install this package with :"
    ,"","pip install terminalbreaker_py", ""
    , "This library is in work in progress!"]
    ,buttons=[{"text": "Submit"}, {"text": "Cancel"}]
    ,width=60
    ,fields=["A field", "Another field"]
    ,padx=20)
win.mainloop()