import os
import PySimpleGUI as sg
import processos as pc

janela = pc.layout()

janela.bind("<Alt>", "Alt")
janela.bind("<Control-KeyPress-B>", "CTRL-B")
janela.bind("<Control-KeyRelease-b>", "Release-B")
janela.bind("<Control-KeyRelease-B>", "Release-B")

event_on = False

while True:    
    eventos, valores = janela.read()
    
    if eventos in (sg.WIN_CLOSED, 'Exit'):
        break

    if eventos == "Alt":
        pass

    if eventos == 'pasta_proc':
        pasta = valores['pasta_proc']

        #print(pasta, '\n')

        # Lista tudo o que tem na pasta selecionada
        arquivos = os.listdir(pasta)
        # Seleciona apenas os arquivos .xml
        arqs_xml = [arq for arq in arquivos if os.path.splitext(arq)[1] == '.xml']

        # Se não houver arquivos .xml, a execução não avança
        if len(arqs_xml) < 1:
            print('Não há arquivos \".xml\" na pasta selecionada. Selecione outra.')
            pass
        else:
            nome_arqs = []
            tabelas = []

            for arq in arqs_xml:
                try:
                    # Armazena todos os valores de todos os arquivos .xml
                    tabelas.append(pc.carrega_xml(pasta+'/'+arq))
                    # Armazena os nomes dos arquivos sem a extensão ".xml"
                    nome_arqs.append(os.path.splitext(arq)[0])

                # Retorna a excessão/erro, caso algo dê errado
                except Exception as E:
                    print(f'Erro: {E}.\n')
                    pass
                
            # Informa o usuário a quantidade de arquivos encontrados
            print(len(arqs_xml), 'aqruivos \".xml\" encontrados. \n')

            # Libera o uso do botão para a seleção da pasta onde os
            # novos arquivos serão salvos
            janela['salva_botao'].update(disabled=False)
            
         
    if eventos == 'pasta_salva':
        pasta_salva = valores['pasta_salva'] + '/'

        try:
            # Salva as informações de cada arquivo .xml
            for tab in tabelas:
                # Cria os arquivos .txt
                with open(pasta_salva + nome_arqs[tabelas.index(tab)] + '.txt', 'a') as arq:
                    # Escreve cada linha no arquivo
                    for line in tab:
                        # Escreve cada valor da linha
                        for val in line:
                            arq.write(str(val)+'\t')
                        # Separa as linhas por uma quebra
                        arq.write('\n')

            # Informa os status finais do processo
            print(len(arqs_xml), 'aqruivos \".xml\" excluídos. \n')
            print(len(arqs_xml), 'aqruivos \".txt\" criados. \n')

            # Apaga todos os arquivos .xml da pasta de origem
            for arq in arqs_xml:
                os.remove(pasta+'/'+arq)
        
        # Retorna a excessão/erro, caso algo dê errado
        except Exception as E:
            print(f'Erro: {E}.\n')
            pass
            
janela.close()
