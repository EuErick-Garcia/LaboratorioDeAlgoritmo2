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
        item = int(input('Enter a number: '))
        list_number.append(item)
    for item in (list_number):
        print(item)


def exercise_02():
    print("fazer")
def exercise_03():
    print("Fazer")
def exercise_04():
    print()
main()