import PySimpleGUI as sg
def main():
    sg.theme('LightBlue1')   # Theme color for my UI
    # All the things inside my window.
    layout = [  [sg.Text('Want to know if a marine animal is in the top ten most endangered marine animals list?')],
                [sg.Text('Write the name of the marine animal and we will let you know!'), sg.InputText(key='box')],
                [sg.Button('Ok'), sg.Button('Close Window')]]

    window = sg.Window('Endangered Animals', layout).Finalize()
    while True: # Loop
        event, values = window.read()
        if event in (None, 'Close Window'): # if user closes window or clicks "close window"
            break
        if my_function(values['box']): # if my_function is true
            sg.popup(values['box'], 'is in the top ten most endangered marine animals list!')
        else: # if my function is false
            sg.popup(values['box'], 'is not in the top ten most endangered marine animals list!')    
        
    
    window.close()
    
    endangeredList = ('Vaquita', 'Whale Shark', 'Hawksbill Sea Turtle', 'Sea Otter', 'Blue Whale', 'River Dolphin', 'Florida Manatee', 'Galapagos Penguin', 'Hawaiian Monk Seal', 'Kemp\'s Ridley Sea Turtle')
def check_endangered_animal(animalName):
    if animalName in endangeredList: # if user input matches my list
        return True
    else: # if user input does not match my list
        return False

main()