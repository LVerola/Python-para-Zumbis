# Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
a=str(2**1000000)
b=len(a)
print('A conta 2 elevado a 1.000.000 possui', b,'digitos.')
