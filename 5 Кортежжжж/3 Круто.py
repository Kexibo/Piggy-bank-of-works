"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""
trek={}
while True:
    x = input('Введите место и исполнителя - ')
    if x!='off':
        trek[x]=input('Введите трек - ')
    else:
        break
print(trek)