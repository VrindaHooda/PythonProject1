#print("Hello world")

import PySimpleGUI as sg
def main():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Want to know if a marine animal is in extreme danger of endangerment?')],
                [sg.Text('Wrtie the name of the marine animal you want to know about!'), sg.InputText(key='box')],
                [sg.Button('Ok'), sg.Button('Close Window')]]



    window = sg.Window('Endangered Animals', layout).Finalize()
    #sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
    while True:
        event, values = window.read()
        if event in (None, 'Close Window'): # if user closes window or clicks cancel
            break
        print('You entered in the box:')
        print(values['box'])  # get the content of multiline via its unique key
        if my_function(values['box']):
            sg.popup(values['box'], ' is endangered')
        else:
            sg.popup(values['box'], ' is not endangered')    
        
    
    window.close()

def my_function(animalName):
    b=('Vaquita', 'Whale Sharks', 'Hawksbill Sea Turtle', 'Sea Otter')
    print(animalName)
    if animalName in b:
        print(animalName + ' is an extremely endangered species!')
        return True
    else:
        print(animalName + ' is not extremely endangered!')
        return False

main()