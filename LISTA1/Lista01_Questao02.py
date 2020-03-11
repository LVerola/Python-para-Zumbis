#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
metros=float(input('Escreva o valor em metros:'))
conversao=metros*1000
print(f'O valor de {metros:.2f} metros em milímetros é equivalente a: {conversao:.2f}')

#Explicação do código:
#metros é uma variável que recebe um valor decimal(float) que o usuário determina(input)
#conversão é a variável que transforma metros em milímetros
#o comando f antes da string permite formatarmos o texto de maneira mais simples
#a variável dentro de um string com a letra f no começo fica entre chaves '{ }'
#o parâmetro ':.2f' determina que depois do valor das variáveis serão exibidos apenas dois números após o '.'
#exemplo: 18.2654895 passa a ser 18.26
