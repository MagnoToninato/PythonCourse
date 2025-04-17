n1 = int(input('Type the first number:'))
n2 = int(input('Type the second number:'))
s = n1+n2
# print('The sum between', n1, 'and', n2, 'is equal to', s)
# Formatação antiga, ainda utilizada porém iremos usar a nova para melhores praticas.
print('The sum between {} and {} equal to {}'.format(n1,n2,s))
