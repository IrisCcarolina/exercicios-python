#Enunciado: Imagina-se que você e sua equipe foram contratados por um restaurante que serve feijoada para desenvolver a solução de software. Você ficou encarregado da parte de retirar pedido por parte do cliente. 
#O valor que a empresa cobra por feijoada é dado pela seguinte equação: 
#total=(volume∗opção)+adional(is)
# 𝒕𝒐𝒕𝒂𝒍=(𝒗𝒐𝒍𝒖𝒎𝒆∗𝒐𝒑çã𝒐)+𝒂𝒅𝒊𝒐𝒏𝒂𝒍(𝒊𝒔)
 
# COMEÇO DA FUNÇÃO volumeFeijoada 

def volumeFeijoada(): 
    #Função que calcula o valor do volume escolhido pelo usúario de acordo com a quantidade de mls que ele deseja 
    while True: 
        try: 
            print('Menu volume Feijoada') 
            volumes = int(input('Entre com a quantidade que deseja (ml): ')) 
            if volumes >= 300 and volumes <= 5000: 
                return 0.08 * volumes #Aqui é realizado o calculo do volume pelo multiplicador  
            else: 
                print('Não aceitamos porções menores que 300ml ou maiores que 5l. Tente novamente!') 
        except ValueError: #É utilizado um except caso o usúario digite qualquer valor não númerico  
            print('Não digite valores não númericos. Tente novamente!') 
            continue 
# FIM DA FUNÇÃO volumeFeijoada 

# COMEÇO DA FUNÇÃO opcaoFeijoada 

def opcaoFeijoada(): 
    #Função que informa o cardápio de opções e retorna o multiplicador de acordo com a opção escolhida pelo cliente 
    while True: 
        print('Menu opção Feijoada:') 
        opcoes = input('''Entre com a opção de Feijoada: 
        b - Básica (Feijão + Paiol + Costelinha) 
        p - Premium (Feijão + Paiol + Costelinha + Partes de porco) 
        s - Suprema (Feijão + Paiol + Costelinha + Partes de porco + Charque + Calabresa + Bacon) 
        >>> ''') 
        if opcoes == 'b': 
            return 1.00 
        elif opcoes == 'p': 
            return 1.25 
        elif opcoes == 's': 
            return 1.50 
        else: 
            print('Você não digitou uma opção válida. Tente novamente!') #Caso seja digitada opção inválida o programa retorna ao seu inicio  
            continue 
# FIM DA FUNÇÃO opcaoFeijoada 

# COMEÇO DA FUNÇÃO acompanhamentoFeijoada 

def acompanhamentoFeijoada(): 
    #Função que informa e acumula os valores dos acompanhamentos escolhidos até que o usúario opte em encerrar o pedido digitando 0  
    acumulador = 0 
    while True: 
        acompanhamentos = input('''Deseja mais algum acompanhamento:  
        0 - Não desejo mais acompanhamentos (encerrar pedido) 
        1 - 200g de Arroz 
        2 - 150g de Farofa Especial 
        3 - 100g de Couve Cozida  
        4 - 1 Laranja Descascada 
        >>> ''') 
        if acompanhamentos == '1': 
            acumulador += 5 
        elif acompanhamentos == '2': 
            acumulador += 6 
        elif acompanhamentos == '3': 
            acumulador += 7 
        elif acompanhamentos == '4': 
            acumulador += 3 
        elif acompanhamentos == '0': 
            return acumulador  
        else: 
            print('Não digite acompanhamentos inexistentes. Tente de novo! ') 
            continue 
# FIM DA FUNÇÃO acompanhamentoFeijoada 

#COMEÇO DA MAIN 

print('-------Bem vindo ao Programa de Feijoada da Iris Carolina Da Silva Cruz-------') 
volume = volumeFeijoada() 
opcao = opcaoFeijoada() 
acompanhamento = acompanhamentoFeijoada() 
total = (volume * opcao) + acompanhamento #Fórmula do total, o calculo é realizado com base no retorno das funções  
print('O valor total a pagar é de R$ {:.2f}. (volume = {:.2f} * opcao = {} + acompanhamento = {:.2f}.)'.format(total, volume, opcao, acompanhamento))  
# FIM DA MAIN
