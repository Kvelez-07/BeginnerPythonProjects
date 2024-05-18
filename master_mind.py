import random

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
ATTEMPTS = 10
LENGTH = 4

def generate_code():
    code = []
    for _ in range(LENGTH):
        code.append(random.choice(COLORS))
    return code

def guess_code():
    while True:
        guess = input('Enter your guess (e.g., R G B Y): ').upper().split()
        if len(guess) != LENGTH:
            print(f'Invalid guess. Please enter a {LENGTH}-color code.')
            continue

        for color in guess:
            if color not in COLORS:
                print(f'Invalid guess. Please use colors from {COLORS}.')
                break
        else:
            return guess

def evaluate_guess(guess, code):
    color_counter = {}
    valid_position = 0
    invalid_position = 0

    for color in code:
        if color not in color_counter:
            color_counter[color] = 0
        color_counter[color] += 1
    
    # First pass: Count valid positions and decrease the counter
    for guess_color, real_color in zip(guess, code):
        if guess_color == real_color:
            valid_position += 1
            color_counter[real_color] -= 1
    
    # Second pass: Count invalid positions without counting already matched colors
    for guess_color, real_color in zip(guess, code):
        if guess_color != real_color and guess_color in color_counter and color_counter[guess_color] > 0:
            invalid_position += 1
            color_counter[guess_color] -= 1
    
    return valid_position, invalid_position

def game():
    print(f"You have {ATTEMPTS} attempts to guess the {LENGTH}-color code.")
    print('The available colors are: ', ' '.join(COLORS))

    code = generate_code()
    for attempts in range(1, ATTEMPTS + 1):
        guess = guess_code()
        valid_position, invalid_position = evaluate_guess(guess, code)
        print(f'Valid position: {valid_position}. Invalid position: {invalid_position}.')

        if valid_position == LENGTH:
            print(f'You guessed the color code in {attempts} attempts!')
            return
    else:
        print('You ran out of attempts. The code was:', ' '.join(code))

if __name__ == '__main__':
    game()