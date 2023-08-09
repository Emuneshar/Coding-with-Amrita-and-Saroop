import time, random

def print_displays():
  print("\033c")
  print("A:", display_a)
  print("B:", display_b)

levels = ["a", "b", "c", "d", "e"]
empty = "."

while level <= len(levels):
  list_a = [] 
  for i in range(level):
    symbol = levels[i]
    
