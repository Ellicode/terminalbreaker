import __init__

def window1(init = False):
    global win
    if not init:
        win2.destroy()

    win = __init__.Window("Window 1",f"""Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut ornare lectus sit amet est. Interdum
consectetur libero id faucibus nisl tincidunt eget nullam
non. Et ultrices neque ornare aenean euismod elementum 
nisi. Ac placerat vestibulum lectus mauris ultrices eros.
Hendrerit dolor magna eget est. Sed viverra tellus in hac
habitasse. Ut tristique et egestas quis ipsum suspendisse
ultrices gravida. Sit amet purus gravida quis blandit
turpis cursus. Gravida neque convallis a cras semper
auctor neque.""",
    width=70,
    buttons = [{"text":"Switch","type":"button","action":window2}],
    fields=[{"name":"Username","type":"field", "hide": False},{"name":"Password","type":"field","hide":True}]
    )
    win.mainloop()
def window2():
    global win2
    win.destroy()
    win2 = __init__.Window("Window 2","""Hello!""",
    width=40,
    buttons = [{"text":"Switch","type":"button","action":window1}],
    )
    win2.mainloop()
window1(init=True)