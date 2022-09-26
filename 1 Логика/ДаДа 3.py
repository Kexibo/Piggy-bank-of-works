x=int(input())
y=int(input())
z=int(input())
S=x+y+z
if x<y<z:
    print('Акция!', S/2)
elif x>y>z:
    print('Акция!',S/3)
else: print('К оплате: ',S)