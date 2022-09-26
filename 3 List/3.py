sur='1.Фамилия: '
job='2.Должность: '
cout='3.Количество студентов во всех группах: '
N=[]
while True:
    kuku=input()
    if kuku=='0':
        break
    kuku=kuku.split(' ')
    kuku.insert(0,[sur])
    kuku.insert(2, [job])
    kuku.insert(4, [cout])
    print(kuku)
    N+=kuku
    print(N)
