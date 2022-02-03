import PySimpleGUI as sg


# criar as janelas e estilos
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Digite a senha para acesso o sistema: ')],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*', )],
        [sg.Button('Entrar')]
    ]


janela = sg.Window('Teste')
while True:
    eventos, valores = janela_login.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['senha'] == "123456":
            sg.popup('Bem vindo')


def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Peperoni', key='pizza1'), sg.Checkbox('Pizza de frango', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)


# criar as janelas iniciais
janela1, janela2 = janela_login(), None
# criar um loop de leittura d eeventos
while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Entrar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitados as duas pizzas')
        elif values['pizza1'] == True:
            sg.popup('Foi solicitado a pizza1')
        elif values['pizza2'] == True:
            sg.popup('Foi solicitado a pizza 2')
