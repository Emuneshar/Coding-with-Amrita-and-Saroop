import random, time

fish = {
  "sea bass": 1,
  "blobfish": 2,
  "trout": 3,
  "hammerhead Shark": 100,
  "goldfish": 2, 
  "lion fish": 40,
  "catfish": 10,
  "megalodon": 4000000000,
  "salmon": 5
}

score = 0


while True:
    print(f"\nYou have {score} points")
    fishList = list(fish)
    catch = random.choice(fishList)

    input("Press enter to cast your line!\n")  
    print("bloop!")