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
# Importa o módulo funcoes
import funcoes

# Bloco com variáveis que são setadas antes do loop
nomeArquivo = 'dados-dengue.csv' # Variavel recebe o nome do arquivo que o codigo irá ler
sair = False # Variavel de controle 
funcoes.mensagemInicial()
# Enquanto sair tiver valor False:
while not sair:
  funcoes.mostraMenu1() # Chama a função mostraMenu1
  escolaMenu1 = input('Informe sua escolha: ') # Escolha do usuário no menu 1
  if escolaMenu1.isnumeric(): # Se a escolha for um numero ele vai virar inteiro
    escolaMenu1 = int(escolaMenu1)
  print('='*50)

  # Bloco que faz a verificação da escolha feita pelo usuário
  if escolaMenu1 == 1: # Caso a escolha seja 1 a função infosDengue é executada
    funcoes.infosDengue()

  elif escolaMenu1 == 2: # Caso a escolha seja 2 a função mostraMenu2 é executada
    funcoes.mostraMenu2()
    escolaMenu2 =  input('Informe sua escolha: ') # Escolha do usuário no menu 2
    if escolaMenu2.isnumeric(): # Se a escolha for um numero ele irá ser tranformado em inteiro
      escolaMenu2 = int(escolaMenu2)
    print('='*50)

    if(escolaMenu2 == 1): # Caso no menu2 a escolha seja 1, a fução pegaData e totalHabitantes são executadas em sequência
      data = funcoes.pegaData(nomeArquivo) 
      funcoes.totalHabitantes(nomeArquivo, data)

    elif(escolaMenu2 == 2): # Caso a escolha no menu2 seja 2, a função pegaData é dadosTotais são executadas
      data = funcoes.pegaData(nomeArquivo)
      funcoes.dadosTotais(nomeArquivo, data)
  
    elif(escolaMenu2 == 3): # Caso a escolha no menu2 seja 3, as funções pegaData, pegaBairro e vizualizarDadosBairro são executadas
      data = funcoes.pegaData(nomeArquivo) 
      bairro = funcoes.pegaBairro(nomeArquivo, data)
      funcoes.vizualizarDadosBairro(nomeArquivo, data, bairro)

    elif(escolaMenu2 == 4): ###########################################################
      data1 = funcoes.pegaData(nomeArquivo)
      bairro = funcoes.pegaBairro(nomeArquivo, data1)
      print('='*50)
      print('Agora escolha a segunda data: ')
      data2 = funcoes.pegaData(nomeArquivo)
            
      funcoes.calcularDiferencaDia(nomeArquivo,bairro, data1, data2)

    elif(escolaMenu2 == 5): # Caso a escolha no menu2 seja 5, a função vizualizarTodasInformacoesSemData é executada
      funcoes.vizualizarTodasInformacoesSemData(nomeArquivo)

    elif(escolaMenu2 == 6): # Caso a escolha menu2 seja 6, a função adicionaDado é executada
      funcoes.adicionaDado(nomeArquivo)
    elif(escolaMenu2 == 7): # Caso a escolha menu2 seja 7, um 'continue' é executado
      continue

    else: # Caso nenhum valor seja aceito uma mensagem de erro é printado e um 'continue' também é executado
      print('escolha um valor valido')
      continue

  elif(escolaMenu1 == 3): # Caso a escolha do menu1 seja 3, a variavél sair recebe True e o programa sai do looping
    sair = True 
    print('saindo...')

  else: # Caso um valor seja inválido será printado um erro e o fluxo retornara para o inicio 
    print(funcoes.vermelho('ESCOLHA INVÁLIDA'))
    