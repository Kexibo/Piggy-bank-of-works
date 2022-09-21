while True:
    price = int(input())
    if price==0:
        break
    print(price%2==0)
    if price%2==0:
        while price%2==0:
            price/=2
            print(price)
    elif price%2!=0:
        price=price-(price/100)*15
    print('К оплате:',price)

