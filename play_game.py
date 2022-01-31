import random

f = open("sgb-words.txt", "r")
words = []
counter = 0
for x in f:
  words.append(x)

answers = []
exclude_letters = []
include_letters = []
perfect_letters = {}

answers = [0] * 6

guess_index = 0
candidates = words
current_guess = 'audio'
for guess_index in range(0, 6):
    guess = current_guess
    answer = input("Value for this guess: {} (0: no, 1: wrong_place, 2: perfect)\n".format(guess))
    answers.append(answer)
    
    for index in range(0, 5):
        a = answer[index]
        character = guess[index]
        if a == '0':
            exclude_letters.append(character)
        elif a == '1':
            include_letters.append(character)
        else:
            perfect_letters[index] = character
    
    print("exclude_letters: {}".format(exclude_letters))
    print("include_letters: {}".format(include_letters))
    print("perfect_letters: {}".format(perfect_letters))
    
    new_candidates = []
    for word in candidates:
        should_exclude = False
        reason = ""
        
        for excludee in exclude_letters:
            if excludee in word:
                should_exclude = True
                reason = "excluded"
                break
                
        for includee in include_letters:
            if not (includee in word):
                should_exclude = True
                reason = "not incuded"
                break
                
        for index in range(0, 5):
            if index in perfect_letters:
                if perfect_letters[index] != word[index]:
                    should_exclude = True
                    reason = "not perfect"
                    break

        # print("word: {} => {} (reason: {})".format(word, should_exclude, reason))
        if should_exclude:
            continue
        
        new_candidates.append(word)
    
    print("new_candidates: {}".format(new_candidates))
    if len(new_candidates) == 0:
        print("no word matches")
        exit(0)
    elif len(new_candidates) == 1:
        print("Answer is {}".format(new_candidates[0]))
        exit(0)
    else:
        if guess_index == 5:
            print("out of guesses")
            exit(0)
        current_guess = random.choice(new_candidates)
        
    
    
    
  