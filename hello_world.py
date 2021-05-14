import PySimpleGUI as sg
def main():
    sg.theme('LightBlue1')   # Theme color for my UI
    # All the things inside my window.
    layout = [  [sg.Text('Want to know if a marine animal is in the top ten most endangered marine animals list?')],
                [sg.Text('Name of marine animal:'), sg.InputText(key='box')],
                [sg.Button('Ok'), sg.Button('Close Window')],
                [sg.Button('Submit', visible=False, bind_return_key=True)]]



    window = sg.Window('Endangered Animals', layout).Finalize()
    while True: # Loop
        event, values = window.read()
        if event in (None, 'Close Window'): # if user closes window or clicks "close window"
            break
        if check_endangered_animal(values['box']): # if my_function is true
            sg.popup(values['box'], 'is in the top ten most endangered marine animals list!')
        else: # if my function is false
            sg.popup(values['box'], 'is not in the top ten most endangered marine animals list!')    
        
    
    window.close()
    
endangeredList = ('VAQUITA', 'WHALESHARK', 'HAWKSBILLSEATURTLE', 'SEAOTTER', 'BLUEWHALE', 'RIVERDOLPHIN', 'FLORIDAMANATEE', 'GALAPAGOSPENGUIN', 'HAWAIIANMONKSEAL', 'KEMPSRIDLEYSEATURTLE') # globallist of animals in uppercase without special characters

def check_endangered_animal(animalName):
    alphanum = ''.join(e for e in animalName if e.isalnum())
    if alphanum.upper() in endangeredList:
        print(alphanum.upper()  + ' is an extremely endangered species!')
        return True
    else:
        print(alphanum.upper()  + ' is not extremely endangered!')
        return False

main()