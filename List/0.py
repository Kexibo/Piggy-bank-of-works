list1=[]
while True:
    list2=str(input())
    if list2!='0':
        if list2 not in list1:
            list1.append(list2)
            print('Dobavil')
        else:
            print('Takoe ushe est')
    else:
        list1.sort()
        print('Cpasibo')
        break
print(list1)


