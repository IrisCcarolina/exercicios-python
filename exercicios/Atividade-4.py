#Enunciado: Imagina-se que você está desenvolvendo um software de controle de estoque para uma mercearia. Este software deve ter o seguinte menu e opções: 
#Cadastrar Produto 
#Consultar Produto(s) 
#Consultar Todas as Produto 
#Consultar Produto por Código 
#Consultar Produto(s) por Fabricante 
#Retornar  
#Remover Produto 
#Sair 

listaProdutos = [] #Lista que irá receber os dicionários/produtos cadastrados pela primeira função  

#COMEÇO DA FUNÇÃO cadastrarProduto
#Função utilizada para realizar o primeiro comando do menu, que é cadastrar o produto desejada na lista que será criada  
def cadastrarProduto(codigo): 
  print(f'Código do Produto: {codigo}') 
  nome = input('Entre com o NOME do produto: ') 
  fabricante = input('Entre com o FABRICANTE do produto: ') 
  valor = float(input('Entre com o VALOR do produto R$: ')) 
  dicionarioProduto = {'Código': codigo, 
                       'Nome': nome, 
                       'Fabricante': fabricante, 
                       'Valor': valor} #Dicionário criado para armazenar as respectivas chaves e os seus valores 
  listaProdutos.append(dicionarioProduto.copy()) 
#FIM DA FUNÇÃO cadastrarProduto  

#COMEÇO DA FUNÇÃO consultarProduto  
#Função criada para que seja possível consultar os dicionários que foram armazanados  
def consultarProduto(): 
  while True: #Laço de repetição para informar as opções de menu secundário dentro do menu principal 
    try: 
      opConsultar = int(input('''Escolha a opção desejada: 
      1 - Consultar todos os produtos 
      2 - Consultar produtos por Código 
      3 - Consultar produtos por Fabricante 
      4 - Retornar 
      >>> ''')) 
      if opConsultar == 1: 
        print('-----------------------') 
        for produto in listaProdutos: #Selecionar cada dicionário da minha lista (Ou seja, cada produto da minha lista de produtos) 
          for key, value in produto.items(): #Selecionar cada chave/valor do dicionário  
            print(f'{key}: {value}') 
        print('-----------------------') 
      elif opConsultar == 2: 
        entrada = int(input('Digite o CÓDIGO do produto: ')) 
        print('-----------------------') 
        for produto in listaProdutos: #Selecionar cada dicionário da minha lista (Ou seja, cada produto da minha lista de produtos) 
          if(produto['Código'] == entrada): #Selecionar chave/valor com base no código digitado (Que é uma das chaves) 
            for key, value in produto.items(): 
              print(f'{key}: {value}') 
        print('-----------------------') 
      elif opConsultar == 3: 
        entrada = input('Digite o FABRINCANTE do produto: ')
        print('-----------------------') 
        for produto in listaProdutos: #Selecionar cada dicionário da minha lista (Ou seja, cada produto da minha lista de produtos) 
          if(produto['Fabricante'] == entrada): #Selecionar chave/valor com base no fabricante digitado (Que é uma das chaves) 
            for key, value in produto.items(): 
              print(f'{key}: {value}') 
        print('-----------------------') 
      elif opConsultar == 4: 
        return #Faz a função retornar ao menu do programa principal 
      else: 
        print('Digite alguma das opções do menu. Vamos tentar novamente!') 
        continue 
    except ValueError: 
      print('Precisamos que digite valores correspondentes ao menu.') 
#FIM DA FUNÇÃO consultarProduto   

#COMEÇO DA FUNÇÃO removerProduto  
#Função criada para remover um produto escolhido pelo usúario, com base em seu código, essa função retira o dicionário correspondente da lista 
def removerProduto(): 
  entrada = int(input('Digite o CÓDIGO do produto a ser removido: ')) 
  for produto in listaProdutos: #Selecionar cada dicionário da minha lista (Ou seja, cada produto da minha lista de produtos) 
    if(produto['Código'] == entrada): #Selecionar o dicionário (produto) que será removido  
      listaProdutos.remove(produto) 
#FIM DA FUNÇÃO removerProduto  

#COMEÇO MAIN 
print('Bem vindo ao Controle de Estoque da Mercearia da Iris Carolina Da Silva Cruz') 
codigoProduto = 0 #Acumulador utilizado na fórmula que gera um código para cada produto 
while True: 
  try: 
    opcao = int(input('''Escolha a opção desejada:  
    1 - Cadastrar Produto 
    2 - Consultar Produto(s) 
    3 - Remover Produto 
    4 - Sair 
    >>> ''')) 
    if opcao == 1: 
      codigoProduto += 1 
      print('Você selecionou a opção Cadastrar Produto') 
      cadastrarProduto(codigoProduto) 
    elif opcao == 2: 
      print('Você selecionou a opção Consultar Produto(s)') 
      consultarProduto() 
    elif opcao == 3: 
      print('Você selecionou a opção Remover Produto') 
      removerProduto() 
    elif opcao == 4: 
      print('Programa finalizado.') 
      break 
    else: 
      print('Digite alguma das opções do menu. Vamos tentar novamente!') 
      continue 
  except ValueError: 
    print('Precisamos que digite valores correspondentes ao menu.') 
#FIM MAIN 
