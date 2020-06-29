import random

guesses = 1

while guesses == 1:
    high = int(input(f'What is the upper limit? '))
    low = int(input(f'What is the lower limit? '))
    num = int(input(f'What is your number? '))

    while num < low or num > high:
        print(f'Invalid! Try again.')
        num = int(input(f'What is your number?'))

    guess_num = random.randint(low, high)
    print(f'\nMy guess is %d' % guess_num)

    while guesses <= 10:
        if guess_num < num:
            low = guess_num
            print(f'Hum! My guess is low?')
            guess_num = random.randint(low + 1, high - 1)
            print(f'How about %d?' % guess_num)
            guesses += 1

        elif guess_num > num:
            high = guess_num
            print(f'What? My guess is too high?')
            guess_num = random.randint(low + 1, high - 1)
            print(f'How about %d?' % guess_num)
            guesses += 1

        else:
            print(f'Correct? I got it after %d try! How smart!' % guesses)
            again = str(input(f'\nDo you want to play again?'))
            if again.startswith('y') or again.startswith('Y'):
                guesses = 1
                print()
                break
            else:
                guesses = 0
                break

    if guesses > 10:
        print(f'I lost!')
        again = str(input(f'\nDo you want to play again?'))
        if again.startswith('y') or again.startswith('Y'):
            guesses = 1
            print()
        else:
            break
