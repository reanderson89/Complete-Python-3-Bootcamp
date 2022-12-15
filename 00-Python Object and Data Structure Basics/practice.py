# # write some arithmetic that equals 100
# print(50+50)

# # create some variables and do math with them
# a = 5
# b = 10
# print(a+b)

# my_income = 100

# my_tax_rate = 0.1

# taxes_due = my_income * my_tax_rate

# print(type(taxes_due))

# print(taxes_due)

# # working with strings
# word = "hello \n world"
# print(word[0])
# print(word[-1])
# print(word[0:4:1])
# # if no value is given for start and end, by default it will begin at the start of the string and go to the end of the string
# print(word[::2])
# print(word)
# # reverse a string
# print(word[::-1])
# print(word.upper())

# # strings are immutable, so if we want to change a part of a string we have to slice out what we need and add it to something else
# name = "Sam"
# # we want to make the name = "Pam"
# name = "P"+name[1:]
# print(name)


# different ways to do string interpolation, instead of having to concatenate everywhere.
# .format

# # you can use indexes from the list on the right to insert into the curly braces for placement
# print("You are {2} {0} {1}".format("the", "cat's", "pajamas"))
# # you can also assign variables to the values from the list on the right, and then use the variables in the curly braces
# print("You are {t} {c} {p}".format(t="the", c="cat's", p="pajamas"))
# result = 77/100
# # format the result by doing result:width.precision f
# print("The result is: {r:1.3f}".format(r=result))

# f-strings, very much like template literals in javascript. Instead of using backticks(``), you just put an "f" in front of the string you are going to be inserting variables to.
# name = "Robert"
# print(f"Hello, my name is {name}")
# print(f"The result is: {result:1.3f}")

# Lists, lists are mutable, they can hold many objects and can hold different types of them at the same time
# Lists have built in methods that can be used like .pop(), .append(), sort(), reverse()
# Lists are very similar to Arrays from javascript
# my_list = [1,2,3,4,5,6]
# print(my_list)
# my_list[0] = 23
# print(my_list)
# popped_obj = my_list.pop()
# print(popped_obj)
# print(my_list)
# selected_popped_obj = my_list.pop(1)
# print(selected_popped_obj)
# print(my_list)
# my_list.sort()
# print(my_list)
# my_list.append(86)
# print(my_list)
# my_list.reverse()
# print(my_list)


# Dictionaries in python, created with {}, can be accessed using bracket[] notation, data stored as "key": "value" pairs, dictionaries are not ordered, can not be sorted, and are accessed by their keys. Much like javascript objects. Numbers can also be used as keys.
# dict = {1: 100, "k2": "Hello World", "k3": [1,2,3,4]}
# print(dict[1])
# print(dict["k2"][6:])
# print(dict["k3"][2])
# # you can add new key value pairs and also re-assign existing keys to new values
# dict["k4"] = "This was not here when the dictionary was first made"
# print(dict)
# dict[1] = "This used to be the number 100"
# print(dict)
# # create a list of all keys and/or values from a dictionary, by using the list() to wrap around the dict.keys() we actually get back a list we can work with, if we don't do it we get back something that is read-only
# dict_keys = list(dict.keys())
# print(dict_keys[2])

# # turning a list into a tuple, tuples are designated with parenthesis (), they are immutable, and have minimal built in methods
# new_list = [1,2,3,4]
# print(new_list.count(2))
# list_into_tuple = tuple(new_list)
# print(new_list)
# print(list_into_tuple)
# print(type(new_list))
# print(type(list_into_tuple))

# Sets in python, sets are unordered collections of unique elements, this means that if the string "hello" was added twice it would only keep 1 of them. This also means if we have a list of objects that could have some duplicates and we want to easily get rid of them and only keep unique values then we could add the list to a "set" and it would handle it.

# sets are created like this
# new_set = set()
# new_set.add(1)
# new_set.add(1)
# new_set.add(1)
# # sets are shown with {}, but they do not have key:value pairs and can therefor be distinguished from dictionaries. Notice that we add(1) three times, but when we print() we only see it in their once.
# print(new_set)
# var_one = 1
# var_two = 1
# new_set.add(var_one)
# new_set.add(var_two)
# # notice that even though we have different variables created with the value 1 on it, they are still not added to the "set"
# print(new_set)

# create a new .txt file in the same working directory is the .py file
# first argument is the name of the file and extension, second argument is the mode. "w" creates a new file and adds text, it will overwrite anything there. "a" creates a new file and writes to it, it will append to anything that already exists. "x" creates a new file, unless one already exists and then it does nothing. "r" is for reading, it will fail if no file already exists
with open("hello.txt", "w") as f: 
    f.write("This is a new text file! \nAnd this is on a new line!!!")

# log to the contents to the terminal
my_file = open("hello.txt")
print(my_file.read())
# .seek() resets the cursor back to the start of the file
my_file.seek(0)
# creates a list of each line of the text file
print(my_file.readlines())
my_file.close()


