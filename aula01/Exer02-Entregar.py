import os

def menu():
    print("\033[92mExercises to deliver")
    print("\n\033[92m0 -> \033[94mExit")
    print("\033[92m1 -> \033[94mLer uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista")

    print("\033[92m2 -> \033[94mLer uma lista de 10 números reais e mostre-os na ordem inversa")

    print("\033[92m3 -> \033[94mLer uma lista de 4 números e mostre o menor e maior número da lista;")

    print("\033[92m4 -> \033[94mCrie uma programa que crie uma lista de números aleatórios e exiba. O tamanho da lista deve ser informado pelo usuário;")
    opc = int(input("\n\033[92mOption: "))
    return opc

def main():
    while True:
        option = menu()
        if option == 0:
            break
        elif option == 1:
            exercise_01()
        elif option == 2:
            exercise_02()

def exercise_01():
    #Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista


    list_number = []
    for index in range (0,5):
        item = int(input('\033[94mEnter a number: '))
        list_number.append(item)
    for item in range (len(list_number)):
        print(f"{item + 1}°: {list_number[item]}")
    input("Press enter to continue")
    os.system("cls")

def exercise_02():
    #Ler uma lista de 10 números reais e mostre-os na ordem inversa

    list_number = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    reversed_values = []
    for index in range (len(list_number)):
        reversed_values.append(list_number[(index + 1) * - 1])
    print(f'List number: {list_number}')
    print(f'Reversed List: {reversed_values}')
    input("\nPress enter to continue")
    os.system("cls")

def exercise_03():
    #Ler uma lista de 4 números e mostre o menor e maior número da lista
    list_number = []
    for i in list_number:
        

def exercise_04():
    print()
main()