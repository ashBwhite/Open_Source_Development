import random

input_planet = input("Please enter name of the planets in solar system separated by space: ")
print('\n')
Solar_System = input_planet.split()

list_length = len(Solar_System)
element_length = [len(i) for i in Solar_System]

print("The list is: ", Solar_System)
print("Number of elements in the list: ", list_length)
print("Length of each element in the list is: ", element_length)
rand_index = random.randint(0, len(Solar_System) - 1)
print("The index number generated at random is: ", rand_index)
print('\n')
input_char = input("Please enter a single character: ")

index = 0
for c in Solar_System[rand_index]:
    index = index + 1
    if c.lower() == input_char.lower():
        print("Your input character ", input_char, " is exist in index ", rand_index)
        break
if index == len(Solar_System[rand_index]):
    print("Your input character ", input_char, " is not exist in index ", rand_index)
