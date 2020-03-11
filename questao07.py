#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32 
celsius=float(input('Insira a temperatura em ºC: '))
conversao=1.8*celsius+32
print(f'{celsius:.2f}ºC é igual a {conversao:.2f}ºF')
