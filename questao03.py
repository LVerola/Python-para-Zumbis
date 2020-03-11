#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias= int(input('Insira a quantidade de dias: '))
horas= int(input('Insira a quantidade de horas: '))
minutos= int(input('Insira a quantidade de minutos: '))
segundos= int(input('Insira a quantidade de segundos: '))
totalSegundos=dias*86400+horas*3600+minutos*60+segundos
print('O total dessa quantidade em segundos é equivalente a: ',totalSegundos,'Segundos.')
