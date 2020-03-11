#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
km=float(input('Escreva a quantidade de KM porcorridos com o carro alugado: '))
dias=float(input('Escreva a quantidade de dias pelos quais o carro foi alugado: '))
total=60*dias+0.15*km
print(f'O preço a ser pago é de R${total:.2f}')
