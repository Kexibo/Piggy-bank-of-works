su=int(input())
ti=int(input())
#if ti == range(10,20):
if ti>=10 and ti<=20:
    print(su/2,ti)
#elif ti == range(20,22):
elif ti>=20 and ti<=22:
    print(su/4,ti)
elif 8<=ti or ti>=22:
    print(su,ti)
else: print('Уходи')