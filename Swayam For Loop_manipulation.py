
'''
#break_Statement - can be used for both for and while loop, to break the loop using (IF)

i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i = i + 1
'''

'''
s = input('Enter a stringe : ')
for letter in s:
    print(letter)
    if letter == 'a' or letter =='i':                          
        break
print("Out of Loop")    
'''


'''
#continue_statement - can be used for both for and while loop
i = 0
while i <=10:
    i = i + 1
    if i == 5:
        continue
    print(i)
'''

'''
for letters in "python":
    if letters == 'h':
        continue
    print(letters, end =" ")
'''

'''
#pass_statement - acts as an indicator and as no operation.
for letter in "Python":
    if letter == 'h':
        pass
        print('This is the pass block')
    print('Letter :', letter)
'''
    
#else_statement - used for both for and while loop
'''
for letter in "Python":
    print(letter)
else:
    print("Complete")
'''
'''
count = 0
while count > 1:
    count = count + 1
    print(count)
    break
else:
    print("No Break")
    '''
    
i=1
sum = 0
while(i<=10):
    sum = sum + i   
    i= i + 1
print("Sum of first ten numbers: ",sum)
