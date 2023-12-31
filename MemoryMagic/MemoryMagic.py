import time, random

def print_displays():
  print("\033c")
  print("A:", display_a)
  print("B:", display_b)

levels = ["a", "b", "c", "d", "e"]
empty = "."

level = 3

while level <= len(levels):
  list_a = [] 
  for i in range(level):
    symbol = levels[i]
    list_a.append(symbol)

  # List b is a copy of list a
  list_b = list_a.copy()

  random.shuffle(list_a)
  random.shuffle(list_b)

  display_a = [empty] * len(list_a)
  display_b = [empty] * len(list_b)

  while True:
    print_displays()

    # input for list a 
    print("Enter an index for list a")
    index_a = input(">> ")
    index_a = int(index_a)
    display_a[index_a] = list_a[index_a]

    print_displays()

     # input for list a 
    print("Enter an index for list b")
    index_b = input(">> ")
    index_b = int(index_b)
    display_b[index_b] = list_b[index_b]

    print_displays()

    if display_a[index_a] == display_b[index_b]:
      print("correct!")
    else:
      print("Incorrect!")
      display_a[index_a] = empty
      display_b[index_b] = empty
    
    time.sleep(1)

    if empty not in display_a:
      print(f"You beat level {level}!!")
      level = level + 1
      break

print("You win!")


