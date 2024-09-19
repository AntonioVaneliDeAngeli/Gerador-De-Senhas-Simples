import PySimpleGUI as sg
from random import randint
import clipboard

sg.theme('Reddit')
numeros = '123456789'
letras = 'abcdefghijklmnopqrstuvwxyz'
mletras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
carac= '!@#$%&'

layout = [
    [sg.Checkbox('Numeros', key='num'), sg.Checkbox('Letras', key='letras'), sg.Checkbox('Letras maisculas', key='mletras'), sg.Checkbox('Caracteres', key='carac')],
    [sg.Slider(range=(5, 20), size=(23,10 ), orientation='horizontal', key='quantc'), sg.Text('Quantidades de caracteres')],
    [sg.Output(size=(53,5))],
    [sg.Button('Gerar', size=(48, 0))],
    [sg.Checkbox('Copiar para o clipbord?', key='clip'), sg.Checkbox('Repetir caracteres?', key='repet')]
]

janela = sg.Window('Gerador de senha', layout=layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    elif eventos == 'Gerar':
        senha = ''
        while True:
            escolhido = randint(1, 4)
            if valores['num'] == True and escolhido == 1:
                senha = senha + numeros[randint(0, 8)]
            elif valores['letras'] == True and escolhido == 2:
                senha = senha + letras[randint(0, 25)]
            elif valores['mletras'] == True and escolhido == 3:
                senha = senha + mletras[randint(0, 25)]
            elif valores['carac'] == True and escolhido == 4:
                senha = senha + carac[randint(0, 5)]
            if len(senha) == valores['quantc']:
                break
        if senha == '':
            print('Marque alguma caixa!')
        else:
            print(f'Senha gerada: {senha}')
            if valores['clip'] == True:
                clipboard.copy(senha)
