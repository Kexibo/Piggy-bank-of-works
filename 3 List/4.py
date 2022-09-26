inp = input().split(' ');
x = True
n1 = 0
if len(inp) == 1:
  x = False
else:
  for i in inp:
    n2 = int(i)
    if n2 > n1:
      n1 = n2
    else:
      x = False
      break
if x:
  print('Да')
else:
  print('Нет')
