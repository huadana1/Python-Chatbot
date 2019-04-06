#imports the ability to get a random number (we will learn more about this later!)
#taken from randomHaiku.py for the say_haiku function
from random import *

greetings = ["hi", "hello", "hey", "howdy", "wasssup", "yo", "how's it going",
"hey boo", "hey buddy", "hola", "sup", "yeehaw"]
# --- Define your functions below! ---

#Chatbot introduces itself and gives user instructions
def intro():
    print("Hi, my name is Wall-E. Let's talk! I can also 'RECITE A HAIKU', 'HELP WITH MATH', or 'PLAY HANGMAN'")
    print("Type something and hit enter")

#chatbot processes user input
def process_input(answer):
    if is_valid_input(answer, greetings):
        say_greeting()
    elif answer == "recite a haiku":
        say_haiku()
    elif answer == "help with math":
        operation = input("OK! Add, subtract, multiply or divide? ")
        operation == operation.lower
        while True:
            num_1 = input("What is the first number? ")
            num_2 = input("What is the second number? ")
            if (num_1.isalpha() == True or num_2.isalpha() == True):
                print("That's not a number!")
                continue
            num_1 = float(num_1)
            num_2 = float(num_2)
            break
        if operation == "add":
            add_math(num_1, num_2)
        elif operation == "subtract":
            subtract_math(num_1, num_2)
        elif operation == "multiply":
            multiply_math(num_1, num_2)
        elif operation == "divide":
            divide_math(num_1, num_2)
        else:
            print("Sorry, I don't know how to '", operation, "'")
    elif answer == "play hangman":
        play_hangman()
    elif answer == "bye":
        print("Bye")
        print("...oh, you're still here?")
    else:
        say_default()

#displays a greeting messsage to the user
def say_greeting():
    print("Hello there! I've been expecting you")

#displays a deafult message to the user
def say_default():
    defaults = ["That's cool!", "Wow", "Nice!", "Uh-huh", "If you say so",
    "I believe you", "Cool story, bro!", "XD", "I LOVE IT", "Great!", "AMAZING!", "hmmm",
    "I agree", "oh..tell me more", "How was that?", "oh no!"]
    print(defaults[randint(0, len(defaults)-1)])

#checks if user_input matches one of the elements in valid_responses
def is_valid_input(user_input, valid_responses):
    for i in valid_responses:
        if i == user_input:
            #if you find a matching response, the input is valid
            return True
    return False

#displays a random 3-5-3 haiku, copied from randomHaiku.py
def say_haiku():
    #Create the list of words you want to choose from.
    threeSyllableList = ["I love food", "Food is great", "He is nice", "I love her",
    "Wow, just wow", "Everywhere", "Cool story", "Haiku? What?", "How are you?",
    "Please help me", "I love you", "I hate you", "What is this", "Take care please",
    "You are great!"]
    fiveSyllableList = ["You are amazing", "I am so hungry", "Do you not love me?",
    "I am so confused", "Where is Everywhere?", "Nice job, my good friend!",
    "This is a haiku", "What is a haiku?", "My mom is missing", "Peaches are yummy!",
    "Steaks taste amazing"]

    #Generates a random integer.
    aRandomIndex = randint(0, len(threeSyllableList)-1)
    randomIndex = randint(0, len(fiveSyllableList)-1)

    #prints first 2 lines
    print(threeSyllableList[aRandomIndex])
    print(fiveSyllableList[randomIndex])

    #changes the random index
    aRandomIndex = randint(0, len(threeSyllableList)-1)

    #prints last line
    print(threeSyllableList[aRandomIndex])

#displays the sum of two given numebrs
def add_math(number1, number2):
    print(number1 + number2)

#displays difference of 2 given numbers
def subtract_math(number1, number2):
    print(number1 - number2)

#displays product of 2 given numbers
def multiply_math(number1, number2):
    print(number1 * number2)

#displays quotient of 2 given numbers
def divide_math(number1, number2):
    print(number1 / number2)

#sets up a 1-player hangman game against chatbot
#edited from Hangman.property
def play_hangman():
    while True:
        vocab = ["apple", "pie", "music", "love", "hard", "club", "core", "pope", "Pokemon"]
        word = vocab[randint(0, len(vocab)-1)]

        # Converts the word to lowercase
        word = word.lower()

        #creates lines for each letter in the word
        underscores = []
        for i in word:
            underscores += "_"
        break

    guesses = []
    maxfails = 7

    #Guessing letters part, 7 tries max
    while True:
        print(underscores)
        print("Letters guessed:", guesses)
        print("Tries Left:", str(maxfails) + '''
         ''')

        #Lose Condition
        if maxfails == 0:
            print("You lost all your lives! You lose! The word was", word, '''...
             ''')
            break

        #Win condition
        if "_" not in underscores:
            print("Congratulations! You guessed the word! You win!")
            break

        guess = input("Guess a letter: ")

        if (guess.isalpha() == False):
            print('''That's not a letter!
             ''')
            continue
        elif len(guess) > 1:
            print('''That's more than one letter, you cheater!
             ''')
            continue
        elif guess in guesses:
            print('''You already guessed that letter!
             ''')
            continue
        elif guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    print('''NICE! You guessed right!
                     ''')
                    underscores[i] = guess
                    continue
        else:
            maxfails -= 1
            guesses += guess
            print('''Sorry, wrong letter!
             ''')
            continue



# --- Put your main program below! ---
def main():
    intro()
    while True:
        reply = input("(What will you say?) ")
        reply = reply.lower()
        process_input(reply)


# DON'T TOUCH! Setup code that runs your main() function.
#calls main()
if __name__ == "__main__":
    main()
