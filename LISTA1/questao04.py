#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário. 
salario=float(input("Digite o salário: "))
porcentagem=float(input("Digite a porcentagem do aumento: "))
ajuste=salario*(porcentagem/100)
novo=salario+ajuste
print (f"O aumento foi de R${ajuste:.2f} e o novo salário é de R${novo:.2f}")

#Explicação do código:
#Duas variáveis que coletam o salário e a porcentagem que o usuário definir(input)
#as duas possuem valores decimais(float)
#Uma variavel que multiplica o valor de salário pela variável porcentagem divido por 100 para obter o ajuste
#Uma variável para obter o novo salário somando a variável salário + ajuste
#(print) contendo o ajuste e o novo salário. Ambas as informações formatas com
#f antes da string e com os parametros :.2f depois das variáveis.
