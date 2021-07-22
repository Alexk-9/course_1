prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

# A.

for i in prices:
    print(int(i // 1), 'руб', f'{int(round(i * 100 % 100)) :02}', 'коп, ', end='')

# B.

print('')
print('id до сортировки', id(prices))
prices.sort()
print('id после сортировки', id(prices))
print(prices)

# C.

prices_new = sorted(prices, reverse=True)
print(prices_new)

# D.

print(list(reversed(prices_new[:5])))