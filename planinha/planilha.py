import openpyxl
import pyperclip
import pyautogui

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']

for linha in sheet_produtos.iter_rows(min_row=2):
    nome_produto = linha[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(815,240, duration=1)
    pyautogui.hotkey('ctrl','v')

    descricao_produto = linha[1].value
    pyperclip.copy(descricao_produto)
    pyautogui.click(786,310, duration=1)
    pyautogui.hotkey('ctrl','v')

    categoria_produto = linha[2].value
    pyperclip.copy(categoria_produto)
    pyautogui.click(794,412, duration=1)
    pyautogui.hotkey('ctrl','v')

    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.click(775,480, duration=1)
    pyautogui.hotkey('ctrl','v')

    peso= linha[4].value
    pyperclip.copy(peso)
    pyautogui.click(801,554, duration=1)
    pyautogui.hotkey('ctrl','v')

    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.click(773,622, duration=1)
    pyautogui.hotkey('ctrl','v')

    #preco = linha[6].value
    #quantidade_em_estoque = linha[7].value
    #data_de_validade = linha[8].value
    #cor = linha[9].value
    #tamanho = linha[10].value
    #material = linha[11].value
    #fabricante = linha[12].value
    #pais_origem = linha[13].value
    #observacoes = linha[14].value
    #codigo_de_barras = linha[15].value
    #localizacao_armazem = linha[16].value
