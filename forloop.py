#for number in range(5):
#    print(number)

# X = "Hello"
# for i in X:
#     print(i)

# using  astart and stop value for our loop
#print value between 101 to 115
    
# n = list(range(113,234,5))
# for i in n:
#     print(i)

# n = list(range(10,60,10))
# for x in n:
#     print(x)

#     if x == 40:
#      break

#list of coceries

# groceries = ["cabbage","carrots","potatoes","onions","okra","mango","oranges"]
# for i in groceries:
#     print(i)

#     if i == "okra":
#         continue

# num1 = [10,30,200,50,30,60]
# for x in num1:
#     if x >30:
#         continue
#     print(x)

#we have 2 list, pople and their age, we want to print each person with age

# people = ["Hayan","Bronson","Erick"]
# age = [21,24,25]
# hometown = ['tudor','nyali','mathira']

# #usee the for loop to find the lrnght of our list using the len function
# print("person","age","Hometown")
# for position in range(len(people)):
#     person = people[position]
#     ages = age[position]
#     town = hometown[position]
#     print(person,ages,town)

#the code ubove is not efficint we use enumerste to make more efficient

# people = ["Hayan","Bronson","Erick"]
# age = [21,24,25]
# hometown = ['tudor','nyali','mathira']

# #usee the for loop to find the lrnght of our list using the len function
# print("person","age","Hometown")
# for position,person in enumerate(people):
#     ages = age[position]
#     town = hometown[position]
#     print(person,ages,town)

#the zip function to replacr the positional indexing
# people = ["Hayan","Bronson","Erick"]
# age = [21,24,25]
# hometown = ['tudor','nyali','mathira']

# print("person","age","Hometown")
# for person, age, hometown, in zip(people,age,hometown):

#     print(person,age,hometown)

