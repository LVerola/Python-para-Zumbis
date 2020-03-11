#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem. 
distancia=float(input('Escreva a distancia a ser percorrida em KM: '))
velocidade=float(input('Escreva a velocidade média esperada para a viagem em KM/h: '))
tempoHora=distancia/velocidade
tempoMinutos=tempoHora*60
print(f'O tempo gasto na viagem é de {tempoMinutos:.2f} Minutos, que equivale a {tempoHora:.2f} Horas.')
