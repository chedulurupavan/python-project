import random

def number_game():
    while True:
        try:
            # Input for guessing range
            n1, n2 = map(int, input("Set the value of range (1 < n < 100) and you have 6 chances back enter  0 0 : ").split())
            
            # Check if the user wants to exit
            if n1 == 0 and n2 == 0:
                return
            
            # Validate range input
            if not (1 <= n1 <= 100 and 1 <= n2 <= 100 and n1 < n2):
                print("Invalid range. Make sure 1 <= n1 < n2 <= 100.")
                continue
            
            chance = 6
            while chance > 0:
                random_number = random.randint(n1, n2)
                try:
                    user_input = int(input("Enter your guess: "))
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    continue
                
                if random_number == user_input:
                    print("Congratulations, you win!")
                    break
                else:
                    print("Try again.")
                
                chance -= 1
            
            print("Game completed.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

def word_game():
    while True:
        try:
            sentence = input("Enter a sentence (minimum 10 words and maximum 50 words) or enter '*' to exit: ").split()
            
            # Check if the user wants to exit
            if '*' in sentence:
                print("Exiting the game.")
                return
            
            # Validate sentence length
            if not (10 <= len(sentence) <= 50):
                print("Sentence must contain between 10 and 50 words.")
                continue
            
            chance = 6
            target_word = random.choice(sentence)
            print("Try to guess the word from the sentence.")
            
            while chance > 0:
                guess = input("Guess the word or enter '*' to exit: ").lower()
                
                if guess == target_word or guess == '*':
                    if guess == '*':
                        print("Exiting the game.")
                        return
                    print("Congratulations, you guessed correctly!")
                    break
                else:
                    print("Try again.")
                
                chance -= 1
            
            print("Game completed.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    while True:
        print("___________ Hello, welcome to the group game ______________")
        try:
            input_programstart = int(input("To start the group game, enter 1. To stop, enter 2: "))
            
            if input_programstart == 1:
                try:
                    input_listgame = int(input("Select a game:\n1. Number Game\n2. Word Game\n3. Exit\nEnter your choice: "))
                    
                    if input_listgame == 1:
                        m=number_game()
                        if m==None:
                            pass
                        
                    elif input_listgame == 2:

                        w=word_game()
                        if w==None:
                            pass
                        
                    elif input_listgame == 3:
                        print("Exiting...")
                        break
                    else:
                        print("Invalid option. Please try again.")
                
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif input_programstart == 2:
                print("____________ Exit ________________")
                break
            else:
                print("Invalid input. Please enter 1 or 2.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

# Call the main function to start the game
main()
