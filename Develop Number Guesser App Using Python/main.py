
import random

for x in range(1, 6):
    low = 1;
    high = 50;

    correct_answer = random.randrange(low, high);
    user_input = int(input("Enter a Number from 1 to 50: "));

    if correct_answer > user_input:
        print("Correct answer is greater!");
        print("Guess Number Was", correct_answer);
    elif correct_answer < user_input:
        print("Correct answer is smaller!");
        print("Guess Number Was", correct_answer);
    elif correct_answer == user_input:
        print(" You Win");
        print("Guess Number Was", correct_answer);
        break;
print("You Lose");
