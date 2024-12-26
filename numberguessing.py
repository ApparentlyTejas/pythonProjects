import random
top_of_range= input("type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range<=0:
        print('please type an integer greater than 0')
        quit()
else:
    print('please type a number')
    quit()

random_number=random.randint(0, top_of_range)
guesses=0

while True:
    guesses+=1
    user_guesses = input('make a guess: ')
    if user_guesses.isdigit():
        user_guesses=int(user_guesses)

    else:
        print('type a number')
        continue
    if user_guesses==random_number:
        print('lesgooo')
        break
    elif user_guesses>random_number:
        print('your guess is larger')
    else:
        print('your guess is smoller')

print('you got it in', guesses, 'guesses')

