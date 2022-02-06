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


print("Guess a letter!")
letter_1 = input("(a-z): ").lower()

if letter_1



















  #this is just for the parachute I designed, just for giggles :D)
  if parachute == 'full':
    print('____   ~~~~~~~   ____')
    print("/  |    |  _V~~ ~~V_  |    |  \ ")
    print("\ _\_~~ \             / ~~_/_ / ")
    print("\         /")
    print("\     /")
    print("\O/")
    print("I")
    print("/ \ ")

elif parachute == 'minus_one':
    print("/  |    |  _V~~ ~~V_  |    |  \ ")
    print("\ _\_~~ \             / ~~_/_ / ")
    print("\         /")
    print("\     /")
    print("\O/")
    print("I")
    print("/ \ ")

elif parachute == 'minus_two':
    print("\ _\_~~ \             / ~~_/_ / ")
    print("\         /")
    print("\     /")
    print("\O/")
    print("I")
    print("/ \ ")
  

elif parachute == 'minus_three':
    print("\         /")
    print("\     /")
    print("\O/")
    print("I")
    print("/ \ ")  



elif parachute == 'minus_four':
    print("\     /")
    print("\O/")
    print("I")
    print("/ \ ")


elif parachute == 'minus_five':
    print("x")
    print("/I\ ")
    print("/ \ ")
