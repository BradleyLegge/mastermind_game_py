import random

def validate_input():
    while True:
        try:
            guess = int(input("Guess the 4 digit number: "))
            return guess
        except ValueError:
            print("Invalid input!")

def main():
    mastermind_num = random.randint(1, 99)
    print(mastermind_num)
    guess = validate_input()
    print("")

    attempts = 1

    while(mastermind_num != guess):
        mastermind_num_str = str(mastermind_num)
        guess_str = str(guess)
        count = 0
        answer = []
        
        max_len = max(len(mastermind_num_str), len(guess_str))
        mastermind_num_str = mastermind_num_str.zfill(max_len)
        guess_str = guess_str.zfill(max_len)

        for i, (d1, d2) in enumerate(zip(mastermind_num_str, guess_str)):
            if d1 == d2:
                answer.append(d1)
                count += 1
            else:
                answer.append("X")

        attempts += 1
        print(answer)
        correct = " ".join(answer)
        print(f"Not quite the number. But you did grt {count} digit(s) correct!")
        print("Also these numbers in your input were correct.")
        print(correct)
        print("")

        guess = validate_input()

    print("You've become a Mastermind.")
    print(f"It took you only {attempts} tries")

if __name__  == "__main__":
    main()