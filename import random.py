import random
def guess(x):
  random_number = random.randint(1,x)
  guess = 0
  while guess != random_number:
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < random_number:
      print("Sorry guess again. The number you chose is too low.")
    elif guess > random_number:
      print("The number you picked is too high. Guess Again.")
  print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

def computer_guess(x):
  low = 1
  high = x
  z = ""
  while z != 'c':
    if low != high:
      guess = random.randint(low,high)
    else:
      guess = low
    z = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
    if z == 'h':
      high = guess - 1
    elif z == 'l':
      low = guess + 1
  print(f'Yay! The computer guessed your number, {z}, correctly!')
guess(10)