from chacter_sle import *
from cave_expl import cavee
xp = 0
aj = aj()
sam = sam()
welc = input("Welcome to my terminal game made in python. Would you like to play? (yes/no?)")
end =  print("To end the game type -1 ")

yes = True
no = False

start = None
if welc == "yes":
    start = True



print("Lets begin first chooes your chacter")

slect = input("You can choose these people: AJ, Sam , Sally: ")

if slect == "aj":
    print("these are aj's stats " + aj.print_stats())

if slect == "sam":
    print("these are sam's stats " + sam.print_stat())

print("Now you choose your chacter lets start the game ")



while start == True:


    print("You spawn in a grass bio with tress near you")
    tree =input("Do you interact with tree? ")

    if tree == "yes":
        print("you now broke a tree and gained 1xp! ")
        xp += 1
    elif tree == "-1":
        break
    else: print("you leave the tree alone and contiune to explore the area ")
    river = input("You come across a river. DO you interact with river? ")
    if river == "yes":
        decide = input("you go in the river,its cold. After a little you get out and dry off. What should you do now? (explore,rest or nothing)")
    if decide == "explore":
        cave = input("You go on to explore the area you find a cave. Do you explore the cave? (yes/no)")
    elif decide == "rest":
        print("You rest and begin to look at the sky. It's a betaful sunny down with a nice breeze. You see the clouds and wonder how it feels to be a cloud. ")
    else: chest = input("you decide to do nothing and you just stand there. after a little you get bored and find a chest. Do you open the chest? (yes/no?): ")
    if cave == "yes":
        cavee()

print("Game has ended. ")           





        
        
    


