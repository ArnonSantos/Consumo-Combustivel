g = float(input('Digite o valor da gasolina onde você custuma abastecer: '))
km = float(input('Digite quantos Km/L sua moto faz: '))
dis = float(input('Digite a quilometragem que será percorrida: '))
cus = (dis / km) * g
print ('Sua moto convencional irá gastar: ', cus, 'reais')

# voltz
carga1 = 120
carga2 = (dis / carga1)
recar = 2.16 * carga2
print ('Com a motocileta convencional será gasto: ', cus, 'Em uma Voltz será gasto: ',recar, 'reais')
