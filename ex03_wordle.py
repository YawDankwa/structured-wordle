"""EX03 - structured wordle - A cute step toward Wordle."""

__author__ = "730607126"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret_word: str, char: str) -> bool:
    """A function was defined to check if a in b."""
    assert len(char) == 1
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == char:
            return True
        idx += 1  
    return False


def emojified(guess: str, secret_word: str) -> str:
    """A function to produce an emoji."""
    assert len(guess) == len(secret_word)
    ind: int = 0
    emoji: str = ""
    while ind < len(guess):
        if guess[ind] == secret_word[ind]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret_word, guess[ind]) is True:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        ind += 1       
    return emoji


def input_guess(length: int) -> str:
    """A function to prompt the user for a guess and keep on prompting until they provide a guess of expected length."""
    inp: str = input(f"Enter a {length} character word: ") 
    while len(inp) != length:
        inp = input(f"That wasn't {length} chars! Try again:")
    return inp


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    max_length: int = 6
    secret_word: str = "codes"
    number_of_turns: int = 1
    won: bool = False
    while number_of_turns <= max_length and won is False:
        print(f"=== Turn {number_of_turns:}/{max_length}===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            won = True
        number_of_turns += 1
    
    if won is True:
        print(f"You won in {number_of_turns-1}/{max_length} turns!")
    else:
        print(f"X/{max_length} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()