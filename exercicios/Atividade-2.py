#Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma pizzaria. 
# Você ficou com a parte de desenvolver a interface do cliente para retirada do produto. 
#A Pizzaria possui tabela própria de sabores de pizzas listados com sua descrição, códigos e valores

valorPizza = 0 # Acumulador se iniciando em zero para receber o valor das pizzas conforme o usúario informa o código e o tamanho 

print('Bem vindo(a) à pizzaria da Iris Carolina Da Silva Cruz') 

print(30 * '-' + 'CARDÁPIO' + 29 *'-') 
print('|  Código    ' + '|    Descrição  ' + '|  Pizza Média    ' + '|  Pizza Grande    |') 
print('|    21      ' + '|   Napolitana  ' + '|    R$ 20,00     ' + '|     R$ 26,00     |') 
print('|    22      ' + '|   Margherita  ' + '|    R$ 20,00     ' + '|     R$ 26,00     |') 
print('|    23      ' + '|   Calabresa   ' + '|    R$ 25,00     ' + '|     R$ 32,50     |') 
print('|    24      ' + '|    Toscana    ' + '|    R$ 30,00     ' + '|     R$ 39,00     |') 
print('|    25      ' + '|   Portuguesa  ' + '|    R$ 30,00     ' + '|     R$ 39,00     |') 
print(67 * '-') 

 
while True: 

    tam = input('Qual tamanho de pizza deseja (M ou G): ').upper().strip() #Entrada para informar TAMANHO desejado 
    if 'M' in tam or 'G' in tam: 
        sabor = input('Entre com o código da pizza: ') 
    else: 
        print('Opção inválida...') #Caso o usúario informe um TAMANHO inexistente 
        continue 
    if sabor == '21' and tam == 'M': 
        valorPizza += 20 
        print('O sabor escolhido foi Napolitana') #Pizza Napolitana Média 
    elif sabor == '22' and tam == 'M': 
        valorPizza += 20 
        print('O sabor escolhido foi Margherita') #Pizza Margherita Média 
    elif sabor == '23' and tam == 'M': 
        valorPizza += 25 
        print('O sabor escolhido foi Calabresa')  #Pizza Calabresa Média 
    elif sabor == '24' and tam == 'M': 
        valorPizza += 30 
        print('O sabor escolhido foi Toscana') #Pizza Toscana Média 
    elif sabor == '25' and tam == 'M': 
        valorPizza += 30 
        print('O sabor escolhido foi Portuguesa') #Pizza Portuguesa Média 
    elif sabor == '21' and tam == 'G': 
        valorPizza += 26 
        print('O sabor escolhido foi Napolitana') #Pizza Napolitana Grande 
    elif sabor == '22' and tam == 'G': 
        valorPizza += 26 
        print('O sabor escolhido foi Margherita') #Pizza Margherita Grande 
    elif sabor == '23' and tam == 'G': 
        valorPizza += 32.5 
        print('O sabor escolhido foi Calabresa') #Pizza Calabresa Grande 
    elif sabor == '24' and tam == 'G': 
        valorPizza += 39 
        print('O sabor escolhido foi Toscana') #Pizza Toscana Grande 
    elif sabor == '25' and tam == 'G': 
        valorPizza += 39 
        print('O sabor escolhido foi Portuguesa') #Pizza Portuguesa Grande 
    else: 
        print('Código inválido. Vamos tentar novamente!') #Caso o usúario informe um código de pizza inexistente 
        continue 


    new_pedido = input('''Deseja pedir mais alguma coisa?  
    1 > Sim 
    2 > Não 
    >>> ''') #Entrada que verifica se o usúario deseja realizar um novo pedido ou finalizar 

    if new_pedido == '1': 
        continue 
    else: 
        print('O total a ser pago é de R$ {:.2f}.' .format(valorPizza)) #Valor total do pedido obtido pelo acumulador 
        break
    