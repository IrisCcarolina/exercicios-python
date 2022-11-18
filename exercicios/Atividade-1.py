#Enunciado 1: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma 
# determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores 
# por unidade:

print('Bem vindo(a) a loja da Iris Carolina Da Silva Cruz') 

valor = float(input('Informe o valor do produto: ')) #valor do produto   
qtd = int(input('Informe a quantidade do produto: ')) #quantidade do produto 
subtotal = valor * qtd #valor sem considerar calculo do desconto 

if qtd <= 4: #sem desconto para essa quantidade 
  valorFinal = subtotal 
elif qtd >= 5 and qtd <= 19: #desconto de 3% 
  valorFinal = subtotal - subtotal * 0.03 
elif qtd >= 20 and qtd <= 99: #desconto de 6% 
  valorFinal = subtotal - subtotal * 0.06 
else:  #desconto de 10% 
  qtd >= 100 
  valorFinal = subtotal - subtotal * 0.10  

print('Valor sem desconto: R$ {:.2f}. ' .format(subtotal)) 
print('Valor com desconto: R$ {:.2f}. ' .format(valorFinal)) 
