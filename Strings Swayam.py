'''
 
print('How\'s the josh')               #'\' works as a escape character

print("Hello,\"How are you?\"")

print('Hey!\nHow are you?')            # '\n' is used to creat newline 
 
print('Hey! \t How are you')           #'\t' creates a tab space

print(R"How\'s the josh!!")            #'R' is used to print raw string

'''


'''
x = 'Hello'
print('{:^20}'. format(x))

print('Hello', format('-','-<10'), 'World!')   #formatting strings
'''

'''
str1 = 'Hello '
str2 = 'world!!!'
#str1 += str2                          #appending the string to the end.
#print(str1)

fstring = f"{str1}{str2}"              #fstring is used to format the string 
print(fstring)
'''

'''
for x in 'Hello':                      #loop through a string
    print(x)



str1 = "Hello Suraj, How are you?"
if 'Suraj' in str1:                    #'in' to know if the word is present in a sentence 
    print('Correct')
'''

'''
str1 = "Hello Suraj, How are you?"
if 'Suraj' not in str1:                #'not in' is opposite of 'in'
    print(True)
else:
    print(False)
'''

str = 'Hello Suraj!, How are you'
tofind = 'you'
#print(str.index('o'))                  #to find the index of a character

#print(str[1])                          #to get just each character from the word

#print(str[0:3])                        #slicing of the string 

#print(str.endswith("!"))               #endswith() string method

#print(str.split())                     #split() method 

#print(str.find('you'))                 #find() - to find the index of the character or word & it gives -1 if the string word is not present or False

#print(str.strip())                     #removes the gaaps of left and right from a string 

#print(str.count('u'))                  #counts the number of charcters appears in the string 

#print(str.isalnum())                    #lets us know if alpha numeric is present or not, if present True, if not False



