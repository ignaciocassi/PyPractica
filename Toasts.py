import win10toast
import PySimpleGUI as sg

def __main__():
    Toaster=win10toast.ToastNotifier()

    layout = [  [sg.Text("PyToast")],     # Part 2 - The Layout
                [sg.Input()],
                [sg.Button('Ok')] ]

    window = sg.Window('Título', layout)
    event, values = window.read()
    titulo=(" ").join(values)

    window = sg.Window('Mensaje', layout)
    event, values = window.read()
    mensaje=(" ").join(values)
    duracion=5

    Toaster.show_toast(title=titulo,msg=mensaje,duration=duracion)

if __name__=="__main__":
    __main__()

