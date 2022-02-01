from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit') #tema do layout
layout = [
    [sg.Text('Usuário'),sg.Input(key='Usuario',size=(30,1))],   #linha1
    [sg.Text('Senha:'),sg.Input(key='Senha', password_char='*', size=(30,1))], #linha 2 
    [sg.Checkbox('Salvar o login?')], #linha 3
    [sg.Button('Entrar')] 
]
#Janela
janela = sg.Window('Tela de login', layout)  #cabeçalho
#ler comentários
while True:
    eventos, valores = janela.read()
    if eventos  == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuario'] == 'jonas' and valores['Senha'] == '123':
            print("Bem vindo ao mundo Python!")
        else:
            print('Senha incorreta')