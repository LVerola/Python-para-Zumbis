#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar. 
Mercadoria=float(input("Digite o preço da mercadoria: "))
percentualDesconto=float(input("Digite o percentual de desconto: "))
Desconto=percentualDesconto*Mercadoria/100
PrecoFinal=Mercadoria-Desconto
print (f"O desconto foi de R${Desconto:.2f} e o preço a ser pago é de R${PrecoFinal:.2f}")
