# task 1
MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins'
}
print(MLB_team['Minnesota'])
del MLB_team['Boston']
print(MLB_team)

# task 2
char = str(input("Please enter a character: "))
print("The ASCII value of " + char + " is: ", ord(char))

# task 3
choose_num = (input("Please enter a number: "))
if not choose_num.isdigit():
    print("This number is not a digit!")

else:
    print("The ASCII value of " + choose_num + " is: ", ord(choose_num))

# task 4
str_input = str(input("Please enter a title: "))
if not str_input.istitle():
    print("The proper title for " + str_input + "is: ", str_input.title())
else:
    print("You have entered a proper title!")

# task 5
word_input = str(input("Please enter a word: "))
char_input = str(input("Please enter a character that you want to find in the word: "))
if char_input in word_input:
    print("Yes! Character " + char_input + "is located at: ", word_input.find(char_input))
else:
    print("No")
