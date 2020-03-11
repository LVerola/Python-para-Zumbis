#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário. 
salario=float(input("Digite o salário: "))
porcentagem=float(input("Digite a porcentagem do aumento: "))
ajuste=salario*(porcentagem/100)
novo=salario+ajuste
print (f"O aumento foi de R${ajuste:.2f} e o novo salário é de R${novo:.2f}")
