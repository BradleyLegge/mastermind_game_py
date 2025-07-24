import random

def generate_random_number():
    return random.randint(1, 9999)

def check_guess(guess, number):
    for digit in str(guess):
        if digit == str(number):
            return digit
        else:
            return

        

def main():
    mastermind_number = generate_random_number()
    print(mastermind_number)

    user_input = input("Guess the 4 digit number: ")

    is_correct = check_guess(user_input, mastermind_number)

    print(is_correct)

    # print(f"Not quite the number. But you did get {} digit(s) correct!")
    print("Also these numbers in your input were correct.")
    print(f"")


if __name__ == "__main__":
    main()