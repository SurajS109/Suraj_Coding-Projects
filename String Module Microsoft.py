"""
fact = 'Suraj'
fact_2 = fact + ' is a good boy'   #string concatenation
print(fact_2)
"""


'''
multiline = """Moon is :
Bad
Good                                 #Multiline
Restful
bright """
print(multiline)
'''
'''
temp = 'Suraj'                  #to find the letter index
print(temp.find('r'))
'''
'''
temp = 'Suraj'                  #to find the count of letter in the string
print(temp.count('r'))
'''

'''
temp = 'Suraj is a good boy'
print(temp.replace('good','Bad'))      #replacing the word 
'''

#in is used to find the word

sentences = ' Moon is full today'
for letter in sentences:
    if "Moon" in sentences:
        print(letter)