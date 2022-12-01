from random import randint

def rollDice(sides):
  roll = randint(1,sides)
  return roll

def rollDice2():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = (roll_6_sided_dice * roll_8_sided_dice)
  return health

print("⚔️ Character Stats Generator ⚔️")
print()

while True:
  warrior_name = input("Name your warrior: ")
  health = str(rollDice2())
  print(f"Their health is: {health}hp")
  print()
  while True:
    another_character = input("Generate another character? y or n: ")
    if another_character == 'y':
      print()
      break
    elif another_character == 'n':
      print()
      print("Game Ended")
      exit()
    else:
      print("Enter a valid response.")
      print()
      continue