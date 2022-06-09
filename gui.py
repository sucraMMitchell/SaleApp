import PySimpleGUI as sg

sg.theme("DarkAmber")
layout = [[sg.T('The Home Page'), sg.T(size = (15, 1), key = '-OUTPUT-')],
          [sg.In(key='-IN-')],
          [sg.Submit(), sg.Cancel()]]
window = sg.Window('Gents of Dominion', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Quit'):
        break
    if event == 'Submit':
        window['-OUTPUT-'].update(values['-IN-'])
        window.refresh()

window.close()
