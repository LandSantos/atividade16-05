def media(num1, num2, num3, num4):
    return (num1 + num2 + num3 + num4)/4

num1 = float(input('Digite o primeiro numero : '))
num2 = float(input('Digite o segundo numero : '))
num3 = float(input('Digite o terceiro numero : '))
num4 = float(input('Digite o quarto numero : '))

print(f'A media das somas dos numeros {num1}, {num2}, {num3} e {num4} tem como resultado {media(num1, num2, num3, num4)}')