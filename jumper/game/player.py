#might add later, but code first

#def print_1(text):
    #words = text
    #time.sleep(.8)
    #for char in words:
        #time.sleep(0.03)
        #sys.stdout.write(char)
       #sys.stdout.flush()
   #print('')
    #prints out the words slower, making it readable to user. Make sure to use the 'print_1' instead of 'print'

parachute_list[full]

class Player:
    """
    This class will create a player that guess a letter to resolve the puzzle. 
    """
    def __init__(self) -> None:
        pass
    
#starting off with simple rules and greetings
print("Welcome to JUMPER!")
print("Would you like to play?")
play = input("(y/n): ").lower()
while play != 'y' and play != 'n':
  print("Sorry, please pick one of the options.")
  play = input("(y/n): ").lower()
if play == 'y':
  print("Wonderful!")
elif play == 'n':
  print("Sorry to hear that. Press 'enter' to exit.")
  input(" ")
  exit()

print("Would you like to hear the rules of the game?")
rules = input("(y/n): ").lower()
while rules != 'y' and rules != 'n':
  print("Sorry, please pick one of the options.")
  rules = input("(y/n): ").lower()
if rules == 'y':
  print("RULES:")
  print("There is a man (or... jumper) who has leapt out of an airplane, and is now using a parachute to get down.")
  print("Your job is to figure out the secret word by guessing the letters in the word.")
  print("If the guess is correct, the letter is revealed.")
  print("If the guess is incorrect, a line is cut on the man's parachute.")
  print(" ")
  print("If the man's parachute disappears before the word is guessed, you lose.")
  print("If you guess the word before the parachute disappears, you WIN!")
  print("Press 'enter' when you feel you are ready to begin.")
  input(" ")
 elif rules == 'n':
  print("Right to it then! Press 'enter' to begin.")
  input(" ")

  


#this needs some SERIOUS HELP!!! The game itself needs to be intagrated and I doubt I have the brains needed for that kind of shenanagans
#Also I can't seem to figure out how to keep it going 

while parachute != 'minus_five':
    print("Guess a letter!")
    letter_1 = input("(a-z): ").lower()
    if (letter_1 in letters):
        #letters = the list I made in the other class
        print("That letter is in this word!")

    else:
        print("Sorry, that letter is not in this word.")
        parachute_list.remove(full)
        parachute_list.append(minus_one)
        print("Guess another letter.")

    



















  #this is just for the parachute I designed, just for giggles :D)
if 'full' in parachute_list:
    print('____   ~~~~~~~   ____')
    print("/  |    |  _V~~ ~~V_  |    |  \ ")
    print("\ _\_~~ \             / ~~_/_ / ")
    print("\         /")
    print("\     /")
    print("\O/")
    print("I")
    print("/ \ ")

elif 'minus_one' in parachute_list:
    print("/  |    |  _V~~ ~~V_  |    |  \ ")
    print("\ _\_~~ \             / ~~_/_ / ")
    print("\         /")
    print("\     /")
    print("\O/")
    print("I")
    print("/ \ ")

elif 'minus_two' in parachute_list:
    print("\ _\_~~ \             / ~~_/_ / ")
    print("\         /")
    print("\     /")
    print("\O/")
    print("I")
    print("/ \ ")
  

elif 'minus_three' in parachute_list:
    print("\         /")
    print("\     /")
    print("\O/")
    print("I")
    print("/ \ ")  



elif 'minus_four' in parachute_list:
    print("\     /")
    print("\O/")
    print("I")
    print("/ \ ")


elif 'minus_five' in parachute_list:
    print("x")
    print("/I\ ")
    print("/ \ ")
