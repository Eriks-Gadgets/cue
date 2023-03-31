import PySimpleGUI as sg
sg.theme("HotDogStand")
print("Cue Log")
sg.Popup("Cue\n© Erik's Gadgets, 2023")
cue_win = sg.Window(title="Cue", layout=[[sg.Text("Cue")], [sg.Text("Message"), sg.Input()], [sg.Text("Interval (secs)"), sg.Input()], [sg.Button("Done")], [sg.Text("© Erik's Gadgets, 2023")]])
while True:
    event, values = cue_win.Read()
    if event == sg.WIN_CLOSED:
        broken = True
        break
    if event == "Done":
        broken = False
        msg = values[0]
        inv = values[1]
        break
if broken == True:
    exit(0)

cue_win.close


import time
while True:
    sg.Popup(msg)
    time.sleep(int(inv))
