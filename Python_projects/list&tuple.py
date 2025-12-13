# List in python 

# A built-in data type that stored set of values
#  It can store element of different types (integer, float, string, etc.)

# Marks = [64, 43, 55, 54, 67,74]  - marks[0], marks[1]
# Student  = ["Karan", 74, "subhash"] - student[0], student[1]
# student[0] = "Arjun"  - allowed in python  
# len(student) = return lenght 

# string is mutable (changeble)
# list is immutable (unchangeble)


marks = [94.4, 23.5, 65.5, 37.3, 29.0]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])


my_list = [2, 1, 3]

my_list.append(4)           # adds one element at the end
print(my_list)

my_list.sort()              # sorts in ascending order
print(my_list)

my_list.sort(reverse=True)  # sorts in descending order
print(my_list)

my_list.reverse()           # reverses list
print(my_list)

my_list.insert(1, 5)        # inserts element at index 1
print(my_list)

my_list.remove(1)           # removes first occurrence of 1
print(my_list)

print(my_list.pop(3))       # removes and returns element at index 3
print(my_list)

print(my_list.index(5))     # returns index of first occurrence of 5

print(my_list.count(5))     # counts total occurrences of 5


list1 = input("What is your first movie ? ")
list2 = input("What is your second movie ? ")
list3 = input("What is your Third movie ? ")

moive = [list1, list2, list3]
print(moive)


# plaindrome mean back and upper side are same example :- (ma,am, racecar,).    




 