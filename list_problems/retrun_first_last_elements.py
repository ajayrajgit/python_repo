my_list = [1, 2, 3, 5, 6]

# No loops and index

# first_element = my_list[0]
# last_element = my_list[-1]

# print("First element:", first_element)
# print("Last element:", last_element)

first, *remaining, last = my_list

print("First element:", first)
print("Last element:", last)
print("Remaining elements:", remaining)


# numbers = [1, 2, 3]

# *number, = numbers. (No single variable , add common after the variable name,
# * does not know how to unpack the list into a single variable,
# it needs to know how many elements to unpack.  )
# # print(*numbers)

# print(type(number))

# Notes

# remaining returns the list of elements between the first and last elements.
#  a [1,2,3,5,6]  =>  remaining = [2,3,5]  or a,b,c -ValueError: too many values to unpack
# Can we use two * variables? No,
# you cannot use two `*` variables in a single unpacking assignment.
# In Python, the `*` operator is used to capture multiple elements
# into a list, but you can only have one `*` variable in the unpacking assignment.
