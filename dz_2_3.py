list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in list_1:
    if i.isdigit() and len(i) == 1:
        i = '"' + i.zfill(2) + '"'
    elif i.isdigit() and len(i) > 1:
        i = '"' + i + '"'
    else:
        for j in i:
            if j == '+' or j == '-':
                i = '"' + i.zfill(3) + '"'
    print(''.join(i), end=' ')



