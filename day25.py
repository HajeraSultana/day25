print("⚔CHARACTER STAT GENERATOR⚔")
print()
def rolldice(side1, side2):
  health = side1 * side2
  return health

health = rolldice(6,8)
warrior3 = input("Name your warrior:\033[34m ")
print("\033[0mTheir Health is", health, "hp")
print()

def rolldice(sides):
  import random
  health = random.randint(1, sides)
  return health

while True:
  health = rolldice(10000)
  warrior1 = input("Name your warrior:\033[32m ")
  print("\033[0mTheir Health is", health, "hp")
  print()
    
  health = rolldice(100)
  warrior2 = input("Name your warrior:\033[33m ")
  print("\033[0mTheir Health is", health, "hp")
  print()
  again = input("Do you want to create another character?: ")
  print()
  if again == "yes":
    continue
  else:
    print("Thanks for playing!")
    break
  