# type casting -- converting from one datatype to another,, eg; a float to string to boolean,int

#num1 = 5/6
#print(num1, 'its of type', type(num1))

#num2 = 2.0
#print(num2, 'is of type', type(num2)) #class float

#num3 = 1 + 2j
#print(num3, 'is of type', type(num3)) # class complex

#create a new string called inside a variable called name
#name = 'Pyhon'
#print(name)

print("Below are top programming languages")
language = ["php","java","python","c#","swift"]

#acess element in index 0
print(language[4])
#mutable = can be changed
#immutable = can't be changed
#append syntax "list.append("c+")"  place the elemnt to the last place ..


language.insert(4,"C#")
print (language[4])

#sytax fo remove list name.remove(element)
#create a new language first to hold the two extra language
new_languages = ["Go", "SQL"]
print(new_languages[1])
#extend the list to the original

language.extend(new_languages)
print(len(language))
print(language)