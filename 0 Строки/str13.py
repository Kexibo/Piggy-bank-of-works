str=input()
list1 = [i for i in str.split(' ')]
for i in list1:
    if '@' in i:
        print(i)
        break