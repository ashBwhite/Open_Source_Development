import random
lower = int(input("Enter lower bound (Number should greater than 0): "))
if lower == 0:
    lower = int(input("You have entered 0, please enter another number:"))
else:
    pass
upper = int(input("Enter upper bound: "))
rand_num = random.randint(lower, upper)

incorrect_answers = []
count = 0
while count >= 0:
    count += 1

    guess = int(input("Guess a number or if you want to escape please enter number 0: "))
    incorrect_answers.append(guess)

    if rand_num == guess:
        print("Congratulation! You have got the right answer! You took", count, "attempts! Your guess numbers were:",
              incorrect_answers)
        break
    elif guess == 0:
        break
    elif rand_num - 3 <= guess <= rand_num + 3:
        print("Getting Warmer! You are close to the target number!")
    elif rand_num != guess and count >= 5:
        print("Hint! Twice the value of this number is:", rand_num*2)
    else:
        print("Not even Close! Take another guess!")