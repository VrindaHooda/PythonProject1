import PySimpleGUI as sg
def main():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Want to know if a marine animal is in extreme danger of endangerment?')],
                [sg.Text('Name of marine animal:'), sg.InputText(key='box')],
                [sg.Button('Ok'), sg.Button('Close Window')],
                [sg.Button('Submit', visible=False, bind_return_key=True)]]



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

b=('VAQUITA', 'WHALESHARKS', 'HAWKSBILLSEATURTLE', 'SEAOTTER') # globallist of animals in uppercase without special characters

def my_function(animal_name):
    #print(''.join(e for e in animal_name if e.isalnum()))
    #loop through each character in animal_name and add them to blank if its a alphanumeric character to remove any other characters
    alphanum = ''.join(e for e in animal_name if e.isalnum())
    # check against uppercase of what the user inputs to match against our master list which is in upper case
    if alphanum.upper() in b:
        print(alphanum.upper()  + ' is an extremely endangered species!')
        return True
    else:
        print(alphanum.upper()  + ' is not extremely endangered!')
        return False

main()