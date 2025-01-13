#Victoria Adoni
#12/9/24
#MadLibs

#Initial

print("""Welcome to Victoria's super cool and fun adlib game!
Fill in the boxes with the corresponding type of word and we'll make up a funny story for you! """)

#Functions
name = input("To play, first give us a name (ex: Ben): ")
place = input("Now give us a place (ex: McDonald's): ")
relative = input("Please give a noun for a relative (ex: Brother, Mother): ")
magicalAnimal = input("Input a mythical creature (ex: Fairy): ")
adjective = input("Give us an adjective (ex: Sleepy): ")
place2 = input("Please give us another place (ex: Porch): ")
food = input("Please input a food dish (ex: Pancakes) ")
movie = input("Give us a movie (ex: Superbad) ")

#Main
print("Your Madlib is ready! Here it is:")
print("On a hot summer day," + name + " decided to go out to " + place + " to see their " + relative +".")
print("On the way to there they came across a " + magicalAnimal + " and had to run away from it!")
print("The " + magicalAnimal + " was thankfully very " + adjective + " and couldn't catch up to "+ name + " who went to hide in a "+ place2 + ".")
print(name + " was finally able to get to their " + relative + "'s house. They had " + food + " and watched " + movie + " the rest of the day. The end :)")


