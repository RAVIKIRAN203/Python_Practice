total_sum = 0 
for num in range (1,11):
    
    if num % 2 == 0:
        print(num)
        total_sum += num
print("Sum of even numbers from 1 to 10 :" , total_sum)



''' TO ITERATE OVER A STRING AND CHECK FOR THE VOWEL AND CONVERT IT INTO UPPERCASE'''

for char in "Python Programming":
    print(char)
    if char.lower() in 'aeiou':
        # check for each character in the string and change it to uppercase 
        print(char.upper(), end = '')
    else:
        # print  non vowel characters in lowercase 
        print(char.lower(), end='')
    
''' Printing a triange '''

for i in range (1,6):
    for j in range (i):
        print('*', end = ' ')
    print()
# Prints a  triangel

''' To print the generated numbers in descending order '''

number = 5

while number > 0 :
    print(number)
    number -= 1

'''To print characters '''

word = ""

char = 'a'

while len(word) < 5 :
    word += char
    char = chr(ord(char)+1)         
    print(word)





