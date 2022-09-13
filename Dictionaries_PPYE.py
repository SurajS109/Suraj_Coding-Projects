'''
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1                                            #adding to the dictionaries
print(ccc)
'''



'''
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:                                               #finding how many times the words have repeated using in and not in
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)        
'''



'''
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']                           #finding how many times the words have repeated using get() method
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)
'''


'''
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()                                                    #to count the words in a line of txt is to split() the line       

print('Words', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)    
'''
      
      
counts = {'Suraj':10, 'Pluto': 20, 'Baba': 40}
for keys in counts:                                                     #Definit loops in dictionary
    print(keys,counts[keys])
          

        

