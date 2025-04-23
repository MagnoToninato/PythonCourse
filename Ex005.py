n1= int(input('Type the first value: '))
n2= int(input('Type the second value: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
Id = n1//n2
P = n1 ** n2
print('The sum is {}, the product is {} and the division is {:.3f}'.format(s,m,d), end=' >>>> ')
# To format a long number, use the command {:.The number, put 'f'if it is a float}
# To perform a line break, use the command "\n"
# To leave the print commands on the same line, use the command 'end = 'sOnly double space leaves a common space, but you ca use any form'
print('Integer division is {} and power is {}'.format(Id, P))

