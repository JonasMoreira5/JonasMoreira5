import PySimpleGUI as sg

# criar as janelas e estilos (layout)


def janela_Login():
    sg.theme('black')
    layout = [
        [sg.Text('Nome:')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_pedido():
    sg.theme('black')
    layout = [
        [sg.Text('fazer pedido')],
        [sg.Checkbox('Pizza peperone', key='pizza1'), sg.Checkbox(
            'Pizza com catupiri', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)

# Criar janelas iniciais
janela1, janela2 = janela_Login(), None
# criar loop de leitura de eventos
while True:
    window,Event,Values = sg.read_all_windows()
    # Quando janela for fechada
    if window == janela1 and Event == sg.WIN_CLOSED:
        break
    # Quando queremos ir para próxima janela
    if window == janela1 and Event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and Event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and Event == 'Fazer Pedido':
        if Values ['pizza1'] == True and Values ['pizza2'] == True:
            sg.popup('Foram solicitadas uma pizza Peperoni e uma pizza Catupiri')
        elif Values ['pizza1'] == True:
            sg.popup('Foram solicitadas uma pizza Peperoni')
        elif Values ['pizza2'] == True:
            sg.popup('Foram solicitadas uma pizza de catupiri')
        elif Event == 'Fazer Pedido':
            sg.popup('Selecione o sabor! Por favor!')