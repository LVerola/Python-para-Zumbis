# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
cigarrosDia=float(input('Quantos cigarros você fuma por dia?: '))
Anos = float(input('A quantos anos você fuma cigarros?(Obs: 0 não é uma quantidade de Anos válida): '))
diasPerdidos=((cigarrosDia*10)*(Anos*365))/1440
if Anos ==0: print('Poxa cara eu ainda avisei na pergunta que não era válido!')
else: print(f'Você já perdeu {diasPerdidos:.2f} Dias de vida, sua chaminé!')
