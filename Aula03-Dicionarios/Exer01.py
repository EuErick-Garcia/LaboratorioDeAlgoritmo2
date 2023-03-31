''' 1. Escreva uma função que recebe uma lista de números e crie um dicionário que seja estruturado
como sendo o número a chave e a quantidade de vezes que o número está presente o valor.
Exemplo: [1, 2, 3, 4, 5, 4, 3] => { 1: 1, 2: 1, 3: 2, 4: 2, 5: 1 }'''

def main():
    list_number = list()
    for i in range (0, 15):
        number = int(input('Enter a number from 1 to 10: '))
        list_number.append(number)
    print(list_number)

    dict_number = {
        'number_1': 0,
        'number_2': 0,
        'number_3': 0,
        'number_4': 0,
        'number_5': 0,
        'number_6': 0,
        'number_7': 0,
        'number_8': 0,
        'number_9' : 0,
        'number_10' : 0,}

    for index in list_number:




main()

