n = int(input("Start game (1) or go back (any other key): "))
if n == 1:
    print("fruits  : ",fruits)
    print("numbers :",numbers)
    print("tools  :",tools)
    print("Categories: fruits, tools, numbers")
    
    category = input("Choose a category (fruits, tools, numbers): ").lower()
    
    if category == "fruits":
        word_list = fruits
    elif category == "tools":
        word_list = tools
    elif category == "numbers":
        word_list = numbers
    else:
        print("Invalid category")
        exit()

    chosen_word = random.choice(word_list)
    lives = len(chosen_word) + 2
    display = ['_'] * len(chosen_word)
    
    print(" ".join(display))
    
    game_over = False
    while not game_over:
        guessed_letter = input("Guess a letter: ").lower()
        
        if guessed_letter in chosen_word:
            for position in range(len(chosen_word)):
                if chosen_word[position] == guessed_letter:
                    display[position] = guessed_letter
        else:
            lives -= 1
            print(f"Incorrect guess! Lives left: {lives}")
        
        print(" ".join(display))
        
        if guessed_letter not in chosen_word:
            if lives == 0:
                game_over = True
                print("You lose!")
        
        if '_' not in display:
            game_over = True
            print("You win!")
else:
    print("Goodbye!")