import random

def generate_random_number():
    return random.randint(1, 9999)

def check_guess(guess, number):
    guess_str = str(guess)
    number_str = str(number)
    count = 0
    guess_amount = 0

    max_len = max(len(guess_str), len(number_str))
    guess_str = guess_str.zfill(max_len)
    number_str = number_str.zfill(max_len)
    answer = []

    for i, (d1, d2) in enumerate(zip(guess_str, number_str)):
        if d1 == d2:
            answer.append(d1)
            count += 1
        else:
            answer.append("X")

    correct = " ".join(answer)
    print(f"Not quite the number. But you did get {count} digit(s) correct!")
    print("Also these numbers in your input were correct.")
    print(correct)

def main():
    generated_number = generate_random_number()
    mastermind_number = str(generated_number).zfill(4)
    print(mastermind_number)

    
    user_input = int(input("Guess the 4 digit number: "))
    check_guess(user_input, mastermind_number)

if __name__ == "__example__":
    main()