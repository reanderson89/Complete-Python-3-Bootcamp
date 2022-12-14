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



