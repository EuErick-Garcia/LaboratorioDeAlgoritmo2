#Testes da Aula....
'''dicionario = {
    'nome': 'Erck',
    'idade': 20,
    'cidade_natal': 'Restinga Sêca',
    'teste': 'teste'}
print(dicionario)

dicionario['cidade_natal'] = input("Informe a sua nova cidade: ")
print(dicionario)
dicionario.update(nome='NIck')
#del dicionario['teste']
print(dicionario)

dicionario.clear()
print(dicionario)
print(dicionario.get('nome', 'nome não incontrado'))'''
#///////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////

def create_dictionary():
    # Forma simples de fazer
    data = dict()

    data['name'] = input("Name: ")
    data['age'] = input("Age: ")
    data['sexo'] = input("sexo: ")
    data['city'] = input("city: ")
    return data
def main():
    persona = create_dictionary()
main()