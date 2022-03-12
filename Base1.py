from PySimpleGUI import PySimpleGUI as sg

# Criar as janelas e estilos (layout)
def janela_login():
    sg.theme('black')
    layout = [
        [sg.Text('Usuário'),sg.Input(key='Usuario',size=(30,1))],   #linha1
        [sg.Text('Senha:'),sg.Input(key='Senha', password_char='*', size=(30,1))], #linha 2 
        [sg.Checkbox('Salvar o login?')], #linha 3
        [sg.Button('Entrar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)
def janela_menu():
    sg.theme('black')
    layout = [
        [sg.Text('Menu Inicio')],
        [sg.Button('Voltar'), sg.Button('Continuar')],
        [sg.Text('  ')]
    ]
    return sg.Window('Menu', layout=layout, finalize=True)
# Eventos
def janela_inicio():
    sg.theme('black')
    layout = [
        [sg.Text('Seja Bem vindo ao meu Primerio Aplicativo', )],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Tela incial', layout=layout, finalize=True)

janela1, janela2 = janela_login(), janela_menu
janela3 = janela_inicio()
# Criar loop de eventos

while True:
    window, eventos = sg.read_all_windows()
    if window  == janela1 and eventos == sg.WINDOW_CLOSED:
        break
    if window  == janela1 and eventos == 'Entrar':
     janela2
     janela1.hide()
    '''if window == janela2 and eventos == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and eventos == 'Continuar':
        janela2.un_hide()
        janela3.hide()
    elif window == janela3 and eventos == 'Voltar':
        janela3 = janela3()
        janela3.un_hide()
    #if valores['Usuario'] == 'jonas' and valores['Senha'] == '123' and window == ['Entrar']:
     ##janela2 = janela_menu()'''