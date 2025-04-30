Name = input('What is your name? ')
Age = int(input('How old are you? '))
Gender = input('What is your gender? ')

if Age == 18 and Gender == 'M':
    print('Hello {} Report for compulsory military service'.format(Name))
else:
    print('{} You are exempted from compulsory military service'.format(Name))