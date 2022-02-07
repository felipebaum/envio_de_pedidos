import PySimpleGUI as sg

def home():
    barcode=0
    sg.theme = 'Black'
    flayout =[
        [sg.Text('  ')],
        [sg.Text('Por favor Escolha o Serviço que deseja enviar: ')],
        [sg.Checkbox('Entrega Convencional', key='envio_1p')],
        [sg.Checkbox('3P Malha direta', key='envio3p')],
        [sg.Text('Quandos pedidos deseja enviar? '),sg.Input(key='qtd_envio')],
        [sg.Text('Barcode '),sg.Input(key='barcode')],
        [sg.Text('Pedido: '), sg.Input(key='pedido')],
        [sg.Button('Enviar', key='enviar')],
        [sg.Text(' ')],
        

        [sg.Button('Sair')]
    ]
    janela1 =sg.Window('Envio de Pedidos', flayout, size=(400,400))
    button,values = janela1.Read()

    if button == 'enviar':
        sg.popup(barcode)
        janela1.close()
    if button == 'redes':
        exit()


home()
