import random
from my_words import word_list

#1.we have to obtain words
def obtain_word():
    word = random.choice(word_list)
    #return either in upper or lower , so system won't confuses
    return word.lower()
#2.Now lets create a function and a loop until the player has won or lost
def lets_play(word):
    #print the word as *******
    hidden_word = "*" * len(word)
    guessed = False
    #create variables for guesses
    guessed_letters = []
    guessed_words = []
    #no of tries are ur choice
    tries = 5
    print("Let's play Hangman......")
    print(hidden_word)
    print("\n")
    #loop
    while not guessed and tries > 0:
        #we can guess a word or letter 
        guess = input("guess a letter or word: ").lower()
        #if we input a word
        if len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                #for every wrong attempt decreement tries
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                hidden_word = word
        #if we input a letter
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Great job,", guess, "is in the word")
                guessed_letters.append(guess)
                #convert word into list and compare each letter
                #if guess matches with word letter then replace * with the guess.
                word_into_list = list(hidden_word)
                #enumerate a list
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_into_list[index] = guess
                hidden_word = "".join(word_into_list)
                #if there are no **** then guess is true
                if "*" not in hidden_word:
                    guessed = True
        
        else:
            print("Not a valid guess.")
        print("remaing tries",tries)
        print(hidden_word)
        print("\n")
    #if guess is true print win
    if guessed:
        print("Congrats, You win!")
    else:
        print("Sorry, you ran out of tries.")
        print("The word was " + word +".")
#3.create a main function to call all functions
def main():
    word = obtain_word()
    lets_play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = obtain_word()
        lets_play(word)

#code fragment
if __name__ == "__main__":
    main()
