#
# import random
#
# low = 1;
# high = 50;
#
# correct_answer = random.randrange(low, high);
# user_input = int(input("Enter a Number from 1 to 50: "));
# while user_input > 5:
#     if correct_answer > user_input:
#         print("Correct answer is greater!");
#         print("Guess Number Was", correct_answer);
#     elif correct_answer < user_input:
#         print("Correct answer is smaller!");
#         print("Guess Number Was", correct_answer);
#     elif correct_answer == user_input:
#         print(" You Win");
#         print("Guess Number Was", correct_answer);
#         break;
#     print("You Lose!")

from random import randint

low = 1
high = 50


def play():
    limit = 5
    correct_answer = randint(low, high)

    while limit > 0:
        try:
            user_input = int(input("Input a number 1 to 50: "))
        except ValueError as e:
            print("Please Input a Number instead of String.")
            play()
        if user_input < correct_answer:
            print("Correct answer is greater!")
        elif user_input > correct_answer:
            print("Correct answer is smaller!")
        elif user_input == correct_answer:
            print("You win!")
        limit -= 1
    print("You Lose!")


if __name__ == "__main__":
    play()
