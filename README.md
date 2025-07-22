# Cows and Bulls

Simple command-line implementation of the classic "Cows and Bulls" number guessing game.

**Game rules**
- The computer generates a secret 4-digit number with unique digits (digits may start with 0).
- You guess 4-digit numbers. After each guess you receive:
	- a "bull" for every correct digit in the correct position
	- a "cow" for every correct digit in the wrong position

The goal is to get 4 bulls.

**Files**
- `cows-and-bulls.py`: the game script (run with Python 3).
- `LICENSE`: project license.

**Requirements**
- Python 3.8+ (works on 3.7 as well).

## Quick Start

Run the game directly:

```bash
python3 cows-and-bulls.py
```

Optional flags:

- `-m NUM`, `--max-attempts NUM` : limit the number of attempts (default: unlimited)
- `-s`, `--show-secret` : show the secret at start (debug mode)

Examples:

```bash
# Play with unlimited attempts
python3 cows-and-bulls.py

# Play with at most 10 attempts
python3 cows-and-bulls.py --max-attempts 10

# Start and show secret (for debugging)
python3 cows-and-bulls.py --show-secret
```

During play you can type `Q` to quit early. After each game you'll be asked if you want to play again.

## How it works (brief)

The script generates a random 4-digit secret with unique digits using `random.sample`. For each valid guess it counts bulls (same digit same position) and cows (digit present elsewhere). The player repeats guesses until they get 4 bulls or run out of attempts.

## Optional Enhancements

- Allow the player to choose a difficulty level at the start of the game, which changes the length of the secret number or the number of attempts allowed.
- Implement a system that offers hints after a certain number of incorrect guesses, providing more guidance to the player.

## Contributing

Contributions are welcome. Fork the repo, make changes, and open a pull request. Keep changes focused and include tests if adding features.

## License

See the `LICENSE` file for license terms.


