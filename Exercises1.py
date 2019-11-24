

# Write a python program to check whether given number is prime


number = int(input("Enter any number :"))
if number > 1:
    for i in range (2, number):
        if(number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
              

# Write a program to show the table of given number

num = int(input("Enter a Number: "))
for i in range(1,11):
    print(num, 'x', i, '=', num*i)

    

    #Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
    
s = []
for i in range(1500,2700):
    if (i%7==0) and (i%5==0):
        s.append(str(i))
print(s)


#Write a Python program which accepts the radius of a circle from the user and compute the area.

radius = int(input("enter radius: "))
print('area = ', 3.14*radius)


#Write a Python script to check if a given key already exists in a diction

n = {'c':1, 'd':2, 'e':3, 'f':4, 'g':5,}
key = input("enter key: ")

if key in n.keys():
    print('Key is present in the dictionary')
else:
    print('Key is not present in the dictionary')



#Write a Python program to get the largest number from a list.

list1 = [1,2,3,5,6,55,6,7,8,9,99,9999,44444]

print("Largest number is: ",max(list1))


#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

str1 = input("Enter a str: ")  # sample inputs (abc,string)
length = len(str1)

if length > 2:
    if str1[-3:] == 'ing':
        str1 += 'ly'
        print(str1)
    else:
        str1 += 'ing'
        print(str1)

    # Write a Python program to count the number of characters (character frequency) in a string.

input_string = "codekul.com"
freq = {} 
  
for char in input_string: 
   if char in freq: 
      freq[char] += 1
   else: 
      freq[char] = 1
    
print ("Per char frequency in '{}' is :\n {}".format(input_string, str(freq)))



#Write a Python program that accepts a string and calculate the number of digits and letters.

string = input("Enter a string: ")
digits=letters=0
for i in string:
    if i.isdigit():
        digits=digits+1
    elif i.isalpha():
        letters=letters+1
    else:
        pass
print("Letters", letters)
print("Digits", digits)
