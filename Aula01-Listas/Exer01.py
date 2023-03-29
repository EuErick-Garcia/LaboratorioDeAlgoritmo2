my_list = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print(f'1 -> 9: {my_list[1:10]}')
print(f'8 -> 13: {my_list[8:14]}')

pair_list = []

for item in my_list:
    if item % 2 == 0:
        pair_list.append(item)
print(f'\nPair item: {pair_list}')

not_pair_list = []
for item in my_list:
    if not item % 2 == 0:
        not_pair_list.append(item)
print(f'\nNot pair item: {not_pair_list}')

multiples_list = []
for item in my_list:
    if item % 2 == 0 or item % 3 == 0 or item % 5 == 0:
        multiples_list.append(item)
print(f'\nMultiples: {multiples_list}')

'''reversed_values = []
for index in range(len(my_list)):
    print(f'Index: {my_list[(index + 1)*1]}')
    reversed_values.append(index)
print(f'Reversed: {reversed_values}')'''
