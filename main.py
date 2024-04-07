one_word = input('Введите текст для массива по одному. В случае отправки пустого значения ввод закроется: ')
my_array = []
final_array = []
while one_word != '':
    my_array.append(one_word)
    one_word = input('Введите текст для массива: ')

for word in my_array:
    if len(word) <= 3:
        final_array.append(word)

print(f'{my_array} -> {final_array}')