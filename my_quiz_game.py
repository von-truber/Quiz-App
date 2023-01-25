#This is my very first attempt on a real life project based off of a tutorial with the same idea.
#I will be making a lot of modifications after this version based on the multiple comments I will be making on here.
#It is also my attempt to practise what I've learned so far as far programming concepts in Python are concerned



print("Greetings and welcome to my general quiz!")

#Here is a prompt for the user to make an input. Note the space left between the word 'play' and the qt marks(" ") in the string
playing = input("Do you want to play ")

#Here is a condition. Note the indentation after the colon. Typically, Python in general relies on indentation for neat code.
#To indent, I use tab(tab key).
if playing == "yes":
	print("Okay! Let's play! :D")

if playing != "yes":							#This block of code can be optimized with an "else" statement as seen on line 26
	print("Alright. Maybe some other time :)")	#Note that this is sort of an epanded form of a typical "if...else" statement.
	quit()

answer = input("What is the highest mountain on earth called? ")

"""The '.lower()' next to the line of code changes the answers (to the inputs) to lowercase letters regardless of how they are typed.
 	If there is a '.upper()' instead, it is changed to uppercase. Alternatively, it/they can be typed in the conditonals for instance;

 	 if answer.lower() == "Mt. Everest" or answer == "Mt Everest" or answer == "Mount Everest" or answer == "Everest":
	print("Correct!")
"""

if answer == "Mt. Everest" or answer == "Mt Everest" or answer == "Mount Everest" or answer == "Everest":
	print("Correct!")
else:
	print("Incorrect!")


answer = input("What is the seventh planet in our Solar System called? ")

if answer == "Uranus":
	print("Correct")
else:
	print("Incorrect!")


answer = input("What is the deepest part of the ocean called? ")

if answer == "The Mariana Trench" or answer == "Mariana Trench":
	print("Correct")
else:
	print("Incorrect!")	


answer = input("What is the fastest land animal? ")

if answer == "Cheetah":
	print("Correct")
else:
	print("Incorrect!")	