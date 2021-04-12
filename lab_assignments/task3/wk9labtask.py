import os
import platform

# task 1
print(os.name)
# task 2
path = os.getcwd()
print(path)
# task 3
curr_dir = os.listdir(path)
for i in curr_dir:
    print(i)
    print()
# task 4
os.mkdir('sub_directory')
# task 5
os.mkdir('d1')
os.mkdir('d2')
os.mkdir('d3')
a ='d1'
b ='d2'
c ='d3'
location = os.path.join(path, a)
t1 = 'file1.txt'
t2 = 'file2.txt'
with open(os.path.join(location, t1), 'w') as fp:
    pass
with open(os.path.join(location, t2), 'w') as fp:
    pass
location = os.path.join(path, b)
t3='file3.txt'
t4='file4.txt'
with open(os.path.join(location, t3), 'w') as fp:
    pass
with open(os.path.join(location, t4), 'w') as fp:
    pass
location = os.path.join(path, c)
t5='file5.txt'
t6='file6.txt'
with open(os.path.join(location, t5), 'w') as fp:
    pass
with open(os.path.join(location, t6), 'w') as fp:
    pass
# task 6
we = "./5.Epsilon NFA"
'''for root,d_names,f_names in os.walk(we):
   print(root, d_names, f_names)
   print()'''
for root, dirs, files in os.walk(we,topdown=True):
    print(files)
    print("*********")
    print(dirs)
    print("*********")
    print(root)
# task 7
try:
    x = input("Enter a word or characters: ")
    if(len(x) <= 5):
        raise ValueError
    else:
        print("Your value has been accepted")
except ValueError:
    print("Your word of character length should be great or equal to 5")
finally:
    print("Finished")
# task 8
try:
    read = open("fill.txt", "r")
    try:
        read.write("Hello, good afternoon")
    except IOError:
        print("IO Error")
    except FileNotFoundError:
        print("File not found")
    except:
        print("This is general error")
finally:
     print("There is no error in this file")