# task1
numbers_list = []

for i in range(0, 5):
    number = int(input("Please enter number: "))
    numbers_list.append(number)

print(numbers_list)

# task2
print(9 < 25)
print(9 < 3)
print(9 > 14)
print(9 <= 17)
print(9 >= 25)
print(9 == 13)

# task 3
print(25 < 7 or 15 > 36)
print(15 > 36 or 3 < 7)
print(4 > 3 and 17 <= 7)
print(not False)
print(not (13 != 7))
print(14 > 7 and 5 <= 5)

# task 4
user_string = str(input("Please enter a string: "))

if len(user_string) > 3 and len(user_string):
    pass
else:
    print("Thank you for your input")

# task 5
# same as task 1

# task 6
import random
lower = int(input("Enter lower bound(Greater than 0): "))
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




