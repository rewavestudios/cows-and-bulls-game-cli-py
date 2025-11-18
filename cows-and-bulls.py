
# Standard library imports
# - `argparse` for command-line flags
# - `random` to generate the secret number
# - `sys` available for future use (kept for completeness)
import argparse
import random
import sys


# Generate a secret number
# Returns a 4-digit string containing unique digits (can start with 0).
def generate_secret() -> str:
    """Generate a 4-digit secret with unique digits."""
    return ''.join(str(d) for d in random.sample(range(10), 4))


# Compare a guess to the secret
# Returns a tuple (cows, bulls):
# - bull: same digit in the same position
# - cow: digit exists in secret but in a different position
def calculate_cows_and_bulls(secret: str, guess: str) -> tuple:
    """Return (cows, bulls) for a given guess against the secret."""
    bulls = sum(1 for i in range(4) if guess[i] == secret[i])
    cows = sum(1 for i in range(4) if guess[i] in secret) - bulls
    return cows, bulls


# Validate user input
# Ensures guess is 4 digits, numeric, and all digits are unique
def is_valid_guess(guess: str) -> bool:
    return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4


# Play a single game session
# - generates a secret
# - runs the input loop tracking attempts
# - validates guesses and prints cows/bulls
# - respects `max_attempts` and `show_secret` for debug
def play_once(max_attempts: int | None = None, show_secret: bool = False) -> None:
    secret = generate_secret()
    attempts = 0

    print('\nI have generated a 4-digit number with unique digits. Try to guess it!')
    if show_secret:
        print(f'(Debug) Secret: {secret}')

    try:
        while True:
            if max_attempts is not None and attempts >= max_attempts:
                print(f"Out of attempts! The secret was {secret}")
                break

            guess = input('Guess (or type Q to quit): ').strip()
            if not guess:
                continue

            if guess.lower() == 'q':
                print('Quitting game.')
                break

            if not is_valid_guess(guess):
                print('Invalid guess. Enter a 4-digit number with unique digits.')
                continue

            attempts += 1
            cows, bulls = calculate_cows_and_bulls(secret, guess)
            print(f'{cows} cows, {bulls} bulls')

            if bulls == 4:
                print(f'Congratulations! You guessed the correct number in {attempts} attempts.')
                break

    except KeyboardInterrupt:
        print('\nInterrupted. Goodbye!')


# Entry point: parse CLI args and run the play loop
def main(argv=None):
    parser = argparse.ArgumentParser(description='Play Cows and Bulls (4-digit guessing game)')
    parser.add_argument('-m', '--max-attempts', type=int, default=None,
                        help='maximum number of attempts (default: unlimited)')
    parser.add_argument('-s', '--show-secret', action='store_true', help='show the secret (debug)')
    args = parser.parse_args(argv)

    while True:
        play_once(max_attempts=args.max_attempts, show_secret=args.show_secret)

        try:
            again = input('\nPlay again? [y/N]: ').strip().lower()
        except KeyboardInterrupt:
            print('\nGoodbye!')
            return

        if again != 'y':
            print('Thanks for playing!')
            break


# If launched as a script, start the program
if __name__ == '__main__':
    main()

