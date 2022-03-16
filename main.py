#from datetime import datetime
#from os import path, mkdir
#
# def emitir_certidao(nome: str, titulo: str, eleitores: list):
#    for eleitor in eleitores:
#        if (eleitor[0] == nome) and (eleitor[4] == titulo):
#            if eleitor[-1] == 0:
#                print('Situação Irregular, eleitor não votou na ultima eleição, por favor comparecer ao cartório eleitoral para regularização do titulo.')
#
#            else:
#                base = open('certidao_modelo.html', 'r')
#                modelo = base.read()
#                base.close()
#
#                data_atual = datetime.now().strftime("%d/%m/%Y")
#                hora_atual = datetime.now().strftime("%H:%M:%S")
#
#                modelo = modelo.replace('$NOME$', f'{eleitor[0]}')
#                modelo = modelo.replace('$TITULO$', f'{eleitor[4]}')
#                modelo = modelo.replace(' $CIDADE$', f'{eleitor[7]}')
#                modelo = modelo.replace('$NASC$', f'{eleitor[3]}')
#                modelo = modelo.replace('$MAE$', f'{eleitor[1]}')
#                modelo = modelo.replace('$PAI$', f'{eleitor[2]}')
#                modelo = modelo.replace('$ZONA$', f'{eleitor[5]}')
#                modelo = modelo.replace('$SEC$', f'{eleitor[6]}')
#                modelo = modelo.replace('$UF$', f'{eleitor[8]}')
#                modelo = modelo.replace('$DATA_DOMILICIO$', f'{eleitor[9]}')
#                modelo = modelo.replace('$HORA$', f'{hora_atual}')
#                modelo = modelo.replace('$DATA$', f'{data_atual}')
#
#                if not path.exists('certidoes_emitidas'):
#                    mkdir('certidoes_emitidas')
#
#                caminho = f'certidoes_emitidas\certidao_{titulo.strip()}.html'
#
#                certidao = open(caminho, 'w')
#                certidao.write(modelo)
#                certidao.close()
#
