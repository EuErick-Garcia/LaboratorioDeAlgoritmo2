''' 1. Escreva uma função que recebe uma lista de números e crie um dicionário que seja estruturado
como sendo o número a chave e a quantidade de vezes que o número está presente o valor.
Exemplo: [1, 2, 3, 4, 5, 4, 3] => { 1: 1, 2: 1, 3: 2, 4: 2, 5: 1 }'''
def my_funcion(number_list):
    number_dict = {}

    for number in number_list:
        '''Método alterntivo'''
        #number_dict[number] = number_dict.get(number, 0) + 1
        if number not in number_dict:
            number_dict[number] = 1
        else:
            number_dict[number] += 1
            
    return number_dict
def main():

     my_list = [1, 2, 3, 4, 6, 4, 3, 4]
     my_variable = my_funcion(my_list)

     print(my_variable)

main()

