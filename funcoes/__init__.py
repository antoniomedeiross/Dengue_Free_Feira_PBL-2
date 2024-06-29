"""
Autor: Antonio Aparecido Medeiros Santana
Componente Curricular: MI Algoritmos
Concluido em: 29/05/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/
"""
# Importando bibiliotecas que serão usadas ao longo do código
from datetime import datetime, timedelta
import time



# Função que recebe uma dado e retorna ela na cor vermelha
def vermelho(string):
  new = f'\033[31m{string}\033[m'
  return new

def verde(string):
  new = f'\033[32m{string}\033[m'
  return new


def mensagemInicial():
  print('='*50)
  print(vermelho('PARA MELHORAR SUA EXPERIÊNCIA VISUAL, AMPLIE O SEU TERMINAL!'))
  time.sleep(1)
  print(verde('INICANDO EM: [3]'))
  time.sleep(1)
  print(verde('INICANDO EM: [2]'))
  time.sleep(1)
  print(verde('INICANDO EM: [1]'))


# Função que abre algum arquivo com 'rt' e encoding='utf-8', e retorna esse arquivo
def abrirArquivo(nomeArquivo):
  a = open(nomeArquivo, 'rt', encoding='utf-8')
  return a


# A função listaBairros recebe o parâmetro nomeArquivo e data, chama a funcão abrirArquivo percorre cada linha e printa os bairros e retorna uma lista com o nome dos bairros existentes na data determinada
def listaBairros(nomeArquivo, data):
  try:
    print('='*20,'BAIRROS','='*21)
    listaBairros = []
    a = abrirArquivo(nomeArquivo)
    for linha in a:  
      dado = linha.split(',')
      if (not listaBairros.__contains__(dado[1])) and dado[0] == data:
        listaBairros.append(dado[1])
  
    for bairro in listaBairros:
      print(f'[{listaBairros.index(bairro)}]-{bairro}')

    return listaBairros
  except:
    print(vermelho('OCORREU UM ERRO!'))
    return None

# A função listaDatas recebe o parâmetro nomeArquivo, executa a função abrirArquivo, percorre o arquivo e printa uma lista de datas existentes e retorna uma lista com essas datas
def listaDatas(nomeArquivo):
  print('-'*21,'DATAS','-'*22)
  listaDatas = []
  a = abrirArquivo(nomeArquivo)
  for linha in a:  
    dado = linha.split(',')
    if  not listaDatas.__contains__(dado[0]):
      listaDatas.append(dado[0])

  listaDatas.pop(0)
  for datas in listaDatas:
    print(f'[{listaDatas.index(datas)}]-{datas}')
  print('-'*50)

  return  listaDatas


# Função infosDengue printa um pequeno texto com informações sobre a dengue
def infosDengue():
  print(verde('O vírus da dengue é transmitido pela picada da fêmea \ndo Aedes aegypti, um mosquito que costuma picar durante \no dia (no início da manhã ou no final da tarde) e se \nmultiplica em locais onde tem água parada. Ele vive \ndentro das casas e ao redor de residências, como \nem quintais e calçadas, por isso os cuidados precisam \nser contínuos.'))
  print('='*50)
  voltar = input('Digíte qualquer valor para voltar ao MENU PRINCIPAL: ')


# A função totalHabitantes recebe os parâmetros nomeArquivo e data, ambos strings, percorre o arquivo e soma o total de habitantes conforme a data desejada e retorna esse valor total
def totalHabitantes(nomeArquivo, data):
  total = 0
  a = abrirArquivo(nomeArquivo)
  for linha in a:
    dado = linha.split(',')
    if dado[0] == data:
      total+= int(dado[2])

  print('='*100)
  print(verde(f'O total de habitantes cadastrados até o dia {data} foram: {total} habitantes'))
  print('='*100)
  voltar = input('Digíte qualquer valor para voltar ao MENU PRINCIPAL: ')
  return total


# A função pegaData recebe o parâmetro nomeArquivo executa a função lista datas e pede para o ususario escolher uma dessas datas, quando ele escolher uma data existente a função retona essa data escolhida
def pegaData(nomeArquivo):
  datas = listaDatas(nomeArquivo) 
  existe = False
  while not existe:
    try:
      data = datas[int(input('Informe o número da data desejada: '))]
      if datas.__contains__(data):
        existe = True
        return data
      else:
        print(vermelho('Data informada não existe no arquivo!'))
    except:
      print(vermelho('Data informada não existe no arquivo!'))


# Função dadoTotais recebe o parâmetro nomeArquivo e data e printa os dados totais na data que foi informada
def dadosTotais(nomeArquivo, data):
  habitantes = 0
  suspeitos = 0
  negativos = 0
  confirmados = 0
  a = abrirArquivo(nomeArquivo)
  for linha in a:
    dado = linha.split(',')
    if dado[0] == data:
      habitantes += int(dado[2])
      suspeitos += int(dado[3])
      negativos += int(dado[4])
      confirmados += int(dado[5])

  print('='*50)
  print(verde(f'DADOS TOTAIS EM FEIRA DE SANTANA NO DIA {data} \nHABITANTES: {habitantes} \nSUSPEITOS: {suspeitos}    |PERCENTUAL: Total-->{suspeitos/(habitantes/100):.2f}% ; Notificados-->{suspeitos/((suspeitos+confirmados+negativos)/100):.2f}% \nNEGATIVOS: {negativos}     |PERCENTUAL: Total-->{negativos/(habitantes/100):.2f}% ; Notificados-->{negativos/((suspeitos+confirmados+negativos)/100):.2f}%\nCONFIRMADOS: {confirmados}  |PERCENTUAL: Total-->{confirmados/(habitantes/100):.2f}% ; Notificados-->{confirmados/((suspeitos+confirmados+negativos)/100):.2f}%'))
  print('='*50)
  voltar = input('Digíte qualquer valor para voltar ao MENU PRINCIPAL: ')
  a.close()
  return 


# A função vizualizaDadosBairro recebe nomeArquivo, data, e bairro como parametro, e printa os dados do bairro informado na data informada
def vizualizarDadosBairro(nomeArquivo, data, bairro):
  a = abrirArquivo(nomeArquivo)
  for linha in a:
    dado = linha.split(',')
    if dado[0] == data and bairro == dado[1].upper():
      print('='*50)
      print(dado[5])
      print(verde(f'DADOS DO BAIRRO {bairro.upper()} NO DIA {data} \nHABITANTES: {dado[2]} \nSUSPEITOS: {dado[3]}   | Porcentagem total: {int(dado[3])/(int((dado[2]))/100):.2f}% | Porcentagem notificados: {int(dado[3])/((int(dado[3]) + int(dado[4]) + int(dado[5]))/100):.2f}% \nNEGATIVOS: {dado[4]}    | Porcentagem total: {int(dado[4])/(int(dado[2])/100):.2f}% | Porcentagem notificados: {int(dado[4])/((int(dado[3]) + int(dado[4]) + int(dado[5]))/100):.2f}%\nCONFIRMADOS: {int(dado[5])} | Porcentagem total: {int(dado[5])/(int(dado[2])/100):.2f}% | Porcentagem notificados: {int(dado[5])/((int(dado[3]) + int(dado[4]) + int(dado[5]))/100):.2f}%'))
      print('='*50)
      a.close()
      voltar = input('Digíte qualquer valor para voltar ao MENU PRINCIPAL: ')
      return
    
  a.close()
  return


# A função pegaBairro recebe nomeArquivo e data, executa a função lista bairro, pede ao usuário que insira o bairro e retorna o nome do bairro escolhido
def pegaBairro(nomeArquivo, data):
  try:
    existe = False
    bairros = listaBairros(nomeArquivo, data)
    print('='*50)
    while not existe:
      try:
        bairro = bairros[int(input('Informe o número do bairro desejado: '))].upper()
      except:
        print(vermelho('VALOR INVÁLIDO!'))
        continue
      a = abrirArquivo(nomeArquivo)
      for linha in a:
        dado = linha.split(',')
        if dado[1].upper() == bairro:
          existe = True
          a.close()
          return bairro
      print(vermelho('bairro informado não existe!'))
  except:
    print(vermelho('OCORREU UM ERRO DESCONHECIDO!'))
    return False



# Função vizualizarTodasInformacoes recebe os parâmetros nomeArquivo e data e printa todas as inforamações que estão contidas no arquivo na data informada
def vizualizarTodasInformacoes(nomeArquivo, data):
  print('='*100)
  try: 
    a = abrirArquivo(nomeArquivo)
    print('-'*100)
    print('DATA       | BAIRROS              | CADASTRADOS     | \033[33mSUSPEITOS\033[m    | \033[34mNEGATIVOS\033[m     | \033[31mCONFIRMADOS\033[m')
    print(f'\033[33m-\033[m'*100)
    for linha in a:
      dado = linha.split(',')
      if data == dado[0]:
        print(f'{dado[0]:<10} | {dado[1]:<20} | {dado[2]:<15} | \033[33m{dado[3]:<13}\033[m | \033[34m{dado[4]:<13}\033[m | \033[31m{dado[5]:<13}\033[m')
        print('\033[33m-\033[m'*100)
    
    a.close()
  except:
    print(vermelho('Não foi possivel encontrar os dados, as informações estão incorretas ou não exitem'))
    print('-'*100)
    return False
  else:
    return True


# Função vizualizarTodasInformacoes recebe os parâmetros nomeArquivo e data e printa todas as inforamações que estão contidas no arquivo de todo os dias existentes
def vizualizarTodasInformacoesSemData(nomeArquivo):
  print('='*125)
  try: 
    a = abrirArquivo(nomeArquivo)
    print('-'*125)
    for linha in a:
      dado = linha.split(',')
      if dado[0] == 'Data':
        print(f'{dado[0]:<10} | {dado[1]:<18} | {dado[2]:<10} | \033[33m{dado[3]:<16}\033[m | \033[34m{dado[4]:<16}\033[m  | \033[31m{dado[5]:<16}\033[m')
      else:
        print(f'{dado[0]:<10} | {dado[1]:<18} | {dado[2]:<10} | \033[33m{dado[3]:<9}-->{int(dado[3])/(int(dado[2])/100):.2f}%\033[m| \033[34m{dado[4]:<9}-->{int(dado[4])/(int(dado[2])/100):.2f}%\033[m | \033[31m{int(dado[5]):<9}-->{int(dado[5])/(int(dado[2])/100):.2f}%\033[m')
      print('\033[33m-\033[m'*125)

    a.close()
  except:
    print(vermelho('Não foi possivel encontrar os dados, as informações estão incorretas ou não exitem'))
    voltar = input('Digíte qualquer valor para voltar ao MENU PRINCIPAL: ')
    print('-'*100)
    return False
  else:
    voltar = input('Digíte qualquer valor para voltar ao MENU PRINCIPAL: ')
    return True


# A função abaixo recebe os parametros nomeArquivop e novosDados, abre o arquivo e escreve o valor da variável novosDados dentro dele.
def colocaDadosArquivo(nomeArquivo, novosDados):
  try:
    a = open(nomeArquivo, 'at')
    a.write(f'\n{novosDados[0]},{novosDados[1]},{novosDados[2]},{novosDados[3]},{novosDados[4]},{novosDados[5]}')
    print(verde(f'NOVA DATA ADICIONADA \n{novosDados[0]},{novosDados[1]},{novosDados[2]},{novosDados[3]},{novosDados[4]},{novosDados[5]}\n'))
  except:
    print(vermelho('Houve um erro ao salvar os valores!'))
  finally: 
    a.close()


# A função proximaData recebe o parâmetro data, e utilizando métodos da biblioteca datetime ela retorna a proxima data.
def proximaData(data):
  try: 
    dataAtual = datetime.strptime(data, '%d/%m/%Y')
    proximaData = dataAtual + timedelta(days=1)
    return proximaData.strftime('%d/%m/%Y')
  except:
    print(vermelho('ocorreu um erro ao obter a data'))
    return False



# Essa função recebe o nome do arquivo pergunta ao usuário quais são os novos dados que ele deseja anexar no arquivo, caso os dados sejam válidos, ele chamará a função colocaDadosArquivo
def adicionaDado(nomeArquivo):
  try:
    primeiraData = '22/03/2024'
    print('-'*50)
    bairro = pegaBairro(nomeArquivo, primeiraData)
    a = abrirArquivo(nomeArquivo)
    for linha in a:
      dado = linha.split(',')
      if dado[1].upper() == bairro:
        ultimaData = dado
    ct = True
    while ct:
      novosSuspeitos = int(input(f'novos Suspeiros no bairro {bairro}: '))
      novosNegativos = int(input(f'novos Negativos no bairro {bairro}: '))
      novosConfirmados = int(input(f'novos Confirmados no bairro {bairro}: '))
      if(novosSuspeitos > int(ultimaData[2]) or novosNegativos > int(ultimaData[2]) or novosConfirmados > int(ultimaData[2])):
        print(vermelho('OS VALORES INFORMADOS INFORMADOS SÃO MAIORES QUE A POPULAÇÃO ATUAL!'))
        continue
      if not(novosSuspeitos < 0 or novosNegativos < 0 or novosConfirmados < 0):
        ct = False
        continue
      print(vermelho('VOCÊ NÃO PODE INFORMAR DADOS NEGATIVOS!'))
      time.sleep(2)
    suspeitos = int(ultimaData[3])-novosConfirmados-novosNegativos 
    if suspeitos < 0:
      suspeitos = 0
    novosDados = [proximaData(ultimaData[0]), ultimaData[1], ultimaData[2], suspeitos + novosSuspeitos, int(ultimaData[4])+novosNegativos, int(ultimaData[5])+novosConfirmados]
  
    a.close()
    print('-'*50)
    print(verde(f'Foram adiconados {novosSuspeitos} casos suspeitos no bairro {bairro}'))
    print(verde(f'Foram adiconados {novosNegativos} casos negativos no bairro {bairro}'))
    print(verde(f'Foram adiconados {novosConfirmados} casos confirmados no bairro {bairro}'))
    colocaDadosArquivo(nomeArquivo, novosDados)
  except:
    print('-'*50)
    print(vermelho('DADOS INVÁLIDOS'))
    time.sleep(2)
    return 


# Essa função recebe três parâmetros nomeArquivo, bairro, data1 e data2, ele percorre o arquivo e retorna a diferença total e percentual do bairro selecionado entre as datas selecionadas.
def calcularDiferencaDia(nomeArquivo, bairro, data1, data2): 
  try:
    a = abrirArquivo(nomeArquivo)
    for linha in a:
      dado = linha.split(',')
      if (dado[0] == data1) and (dado[1].upper() == bairro):
        metricas1 = [dado[3], dado[4], dado[5]]
      if (dado[0] == data2) and (dado[1].upper() == bairro):
        metricas2 = [dado[3], dado[4], dado[5]]
    diferenca = []
    for i in range(3):
      diferenca.append(int(metricas2[i]) - int(metricas1[i]))
    print('='*50)
    print(f'{bairro} Diferença entre os dias {data1} e {data2}:')
    print('='*50)

    print(verde(f'Diferença de casos suspeitos: {diferenca[0]} | percentual: {int(metricas2[0])/(int(metricas1[0])/100)-100:.2f}%'))
    print(verde(f'Diferença de casos negativos: {diferenca[1]}   | percentual: {int(metricas2[1])/(int(metricas1[1])/100)-100:.2f}%'))
    print(verde(f'Diferença de casos confirmados: {diferenca[2]} | percentual: {int(metricas2[2])/(int(metricas1[2])/100)-100:.2f}%'))
  except:
    print(vermelho('OCORREU UM ERRO, O BAIRRO QUE VOCE DESEJA NÃO TEM DADOS NA DATA INFORMADA! '))
    return   


# A função mostraMenu1 printa o menu1 na tela
def mostraMenu1(): 
  print('#'*50)
  print('----------Sistema Dengue Free Feira---------------')
  print('#'*50)
  print('-------------------MENU---------------------------')
  print('[1]-->Sobre a Dengue')
  print('[2]-->Dados da Dengue em Feira de Santana-Ba')
  print('[3]-->Sair')


# A função mostraMenu1 printa o menu2 na tela
def mostraMenu2():
  print('----------------DADOS DO MUNICÍPIO----------------')
  print('[1]--> Total de habitantes cadastrados') 
  print('[2]--> Dados totais de Feira de Santana-Ba') 
  print('[3]--> Visualizar dados do bairro')
  print('[4]--> Diferença entre dias especificos')
  print('[5]--> Visualizar todas as informações') 
  print('[6]--> Adicionar novos dados')
  print('[7]--> Voltar')