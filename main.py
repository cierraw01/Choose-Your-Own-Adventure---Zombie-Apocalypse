#Intro
print("Welcome to Choose Your Own Adventure - Zombie Apocalypse!")
print("\nTo Chose an Option, Type in the Number Next to The Option")

#Food Options
print("\nYou are almost out of food at your house and need to get More. Do you...")

print("\n1 Go to a neighbor's house")
print("2 Go to a small convenience store")
print("3 Go to the supermarket\n")

foodChoice = input()

#Neighbor's House Options
if foodChoice == "1":
  print("\nYou have chosen to go to your neighbor's house. You knock, but there's no answer. You think that they are probably a zombie or left town, and you decide to break in. You are in the living room, and your zombie neighbor approaches you. Do you...")

  print("\n1 Run out of the house")
  print("2 Run to the kitchen and hope to grab whatever you can while you avoid the zombie")
  print("3 Stand your ground and fight the zombie\n")
  
  neighborChoice = input()

  if neighborChoice == "1":
    print("\nIn your haste to get out of the house, you run run into zombies on the porch and are bitten. You turn into a mindless zombie.")
  
  if neighborChoice == "2":
    print("\nYou take a small bounty of food. You have to jump out the window to escape and twist your ankle. You make it back home, but your ankle will need a long time to heal.")

  if neighborChoice == "3":
    print("\nCongratulations, you have won the fight against the zombie! You take a big bounty of food home.")

#Convenience Store option
if foodChoice == "2":
  print("\nYou have arrived at the convenience store and notice zombies inside. Do you...")

  print("\n1 Not enter the store and catch some pidgeons nearby to bring home")
  print("2 Enter the store quietly and hope to gather supplies without notice")
  print("3 Kill all the zombies in the store to get as much as you want")

  convenienceChoice = input()

  if convenienceChoice == "1":
    print("\nYou catch a disease from the pidgeons and die.")
  
  if convenienceChoice == "2":
    print("\nYou successfully leave the store with some supplies. The zombies chase you home for a while, but you eventually lose them and go home.")
  
  if convenienceChoice == "3":
    print("\nYou are overwhelmed by the zombies and eaten.")

#Grocery Store Options
if foodChoice == "3":
  print("\nThe grocery store is overrun by zombies, but you and other survivors successfully clear the store. You gather a big bounty and decide to teamup with other survivors. There are three survivors, all going in different directions: an experienced survivalist, a doctor, and a scientist.")

  print("\n1 The survivalist is going to the forest to get away from the zombies. She grew up in a survivalist family and spent her entire life training.")
  print("2 The doctor is staying in a house with top tier security. He is able to provide medical assistance.")
  print("3 The scientist is going to a research lab in the middle of the city. They claim that they can make an airborne zombie cure, but they need a partner to help them survive for now.\n")

  groceryChoice = input()

  if groceryChoice == "1":
    print("\nYou are happy with the survivalist. However, you die in your middle ages from an infection that was easily curable before the Apocalypse.")

  if groceryChoice == "2":
    print("\nAfter a few months, you and the doctor go on another raid. It goes wrong, and zombies are closing in, so he injures and leaves you to be a distraction for the zombies.")
  
  if groceryChoice == "3":
    print("\nAfter two years of research and meeting a research team from the next city over, an airborne cure is made. All the zombies with no mortal wounds, return to humans. At first, it was only the city cured, but soon it spreads to the rest of the country, the continent, and then the world.")