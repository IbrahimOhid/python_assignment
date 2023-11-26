from random import randint;

for x in range(1, 6):
    low = 1;
    high = 50;

    guessNumber = int(input("Enter a Number 1 to 50: "));
    correct_answer = randint(low, high);
    if guessNumber < correct_answer:
        print("Correct answer is greater!");
        print("Guess Number Was", correct_answer)
    elif guessNumber > correct_answer:
        print("Correct answer is smaller!")
        print("Guess Number Was", correct_answer)
    elif guessNumber == correct_answer:
        print("You Win");
        print("Guess Number Was", correct_answer)
    else:
        print("You Lose!")