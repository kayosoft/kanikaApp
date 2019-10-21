i = 0
real_value = 8
while i <= 3:
  guess = int(input('Guess: '))
  if guess == real_value:
    print('You Win!')
    break
   else:
    print('You lose')
  
