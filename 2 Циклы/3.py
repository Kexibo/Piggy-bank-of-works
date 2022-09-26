login = input()
forb = '=?*^$№@_ '
count = 0
for i in login:
    if i in forb:
        print('Недопустимый символ: ', i)
        break
    else:
        count += 1
    if count == len(login):
        print('Все супер')
        break
