str=input()
str1=''
for i in str:
    if i.isdigit():
        str1=str1+i
print(int(str1)+1)