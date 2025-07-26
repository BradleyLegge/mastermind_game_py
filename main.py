import random

def main():
    mastermind_num = random.randint(1, 99)
    print(mastermind_num)
    guess = int(input("Guess the 4 digit number: "))
    print("")

    mastermind_num_str = str(mastermind_num)
    guess_str = str(guess)

    max_len = max(len(mastermind_num_str), len(guess_str))
    mastermind_num_str = mastermind_num_str.zfill(max_len)
    guess_str = guess_str.zfill(max_len)

    while(mastermind_num != guess_str):
        attempts = 0
        count = 0
        answer = []
        for i, (d1, d2) in enumerate(zip(mastermind_num_str, guess_str)):
            if d1 == d2:
                print(mastermind_num_str)
                print(guess_str)
                answer.append(d1)
                count += 1
            else:
                answer.append("X")

        attempts += 1
        correct = " ".join(answer)
        print(f"Not quite the number. But you did grt {count} digit(s) correct!")
        print("Also these numbers in your input were correct.")
        print(correct)
        print("")

        guess = int(input("Enter your next choice of numbers: "))



if __name__  == "__main__":
    main()