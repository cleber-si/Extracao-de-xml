import PySimpleGUI as sg
from bs4 import BeautifulSoup

def layout():
    layout = [
    [sg.Text('Selecionar Pasta de Consulta'), 
     sg.Input(enable_events=True, key='pasta_proc', disabled=True),
     sg.FolderBrowse('Procurar')],
    [sg.Text('Selecionar Pasta para Salvar'), 
     sg.Input(enable_events=True, key='pasta_salva', disabled=True),
     sg.FolderBrowse('Procurar', key='salva_botao', disabled=True)],
    #[sg.Frame('Informações de Processamento',
    # [[sg.Output(key = 'output', size=(84, 10))]])]
    ]

    return sg.Window('Processar Arquivos XML', layout, finalize=True)

def carrega_xml(arquivo):
    # Abre o arquivo .xml
    with open(arquivo) as arq:
        soup = BeautifulSoup(arq, "html.parser")

    # Conta o número de colunas
    num_cols = len(soup.find_all('column'))
    # Carrega as informações 'cruas'
    informacoes = soup.find_all("data")

    # Extrai os valores de interesse
    valores = []
    for i in informacoes:
        valores.append(i.get_text())

    # Retorna uma lista 2D com as informações do arquivo
    return [valores[i:i+num_cols] for i in range(0, len(valores), num_cols)]