mBlock = [[1,0,0,0,1],[1,1,0,1,1],[1,1,0,1,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1]]
sBlock = [[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,0],[0,1,1,1,0],[0,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]]

for column in range(7):
  print('')
  for row in range(5):
    if(mBlock[column][row] == 1):
      print('M', end='')
    else:
      print(' ', end='')

  for row in range(5):
    if(sBlock[column][row] == 1):
      print('S', end='')
    else:
      print(' ', end='')
  