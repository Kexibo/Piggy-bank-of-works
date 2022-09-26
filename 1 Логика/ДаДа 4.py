Kat=input('Категория - ')
Kat=Kat.lower()
if Kat=='продукты':
    Sum=input('Цена - ')
    if Kat in range(0, 100):
        print('Попробуйте нашу выпечку')
    elif Kat in range(100, 500):
        print('Как насчёторехов в шоколаде')
    else:
        print('Попробуйте экзотческие фрукты')
else:
    print('Загляните в товары для дома')