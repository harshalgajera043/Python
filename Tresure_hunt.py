
#find trasure
print("Welcome to our game, Hope you will enjoy it alot.")
First = input("You are at cross do you want to go left or right?\n")
first = First.lower()
if first == "left":
  print("You arrieve at lake!")
  Second = input("Now do you want to swim or wait for boat\n")
  second = Second.lower()
  if second == "wait for boat":
    print("you are arrieve at island!!")
    Last = input("Their is three door, which one do you want to open? Red, Yellow or Blue\n")
    last = Last.lower()
    if last == "yellow":
      print("Congratulations!! You won the game!!\nI know since the begining that you are a champion and you prove me right.")
    elif last == "red" or last == "blue":
      print("Game over!!\nBetter luck next time!")
    else:
      print("You made some unvalide choise")
  elif second == "swim":
    print("Game over!!\nBetter luck next time!")
  else:
    print("You made some unvalide choise")
elif first == "right":
  print("Game over!!\nBetter luck next time!")
else:
  print("You made some unvalide choise")
