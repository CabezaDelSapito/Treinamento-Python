import PySimpleGUI as sg

sg.theme('reddit')

janela_principal = [
    [sg.Text('E-mail'), sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.FolderBrowse('Escolher Pasta Anexos', target='input_anexos'), sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher Pasta Planilha', target='input_planilha'), sg.Input(key='input_planilha')],
    [sg.Button('Salvar')]
]

janela = sg.Window('principal', layout=janela_principal)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = values['email']
        senha = values['senha']
        caminho_anexos = values['input_anexos']
        caminho_planilha = values['input_planilha']
        print(f'O email digitado foi {email}')
        print(f'A senha digitado foi {senha}')
        print(f'O caminho do anexos digitado foi {caminho_anexos}')
        print(f'O caminho da planilha digitado foi {caminho_planilha}')